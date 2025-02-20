import numpy as np
import pandas as pd
from scipy.stats import norm
from black_scholes import BlackScholes
from src.binomial_barrier_option import FXBarrierOption
from vanna_volga import VannaVolga

class VannaVolgaBarrierMarket(FXBarrierOption):
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility, 
                 domestic_rate, foreign_rate, barrier_level, barrier_type, market_data_path):
        """
        Implements Vanna-Volga correction for FX Barrier Options using real/simulated market data.

        :param market_data_path: Path to the CSV file containing market-implied volatilities.
        """
        super().__init__(spot_price, strike_price, time_to_maturity, volatility, 
                         domestic_rate, foreign_rate, barrier_level, barrier_type)
        
        self.market_data = pd.read_csv(market_data_path)
        self.market_volatility_atm, self.market_volatility_rr, self.market_volatility_bf = self.get_market_vols(spot_price)

    def get_market_vols(self, spot_price):
        """
        Retrieves market-implied volatilities for the given spot price.

        :return: ATM Volatility, Risk Reversal, Butterfly Spread
        """
        closest_spot = self.market_data.iloc[(self.market_data["Spot"] - spot_price).abs().argsort()[:1]]
        return closest_spot["ATM_Vol"].values[0], closest_spot["RR_Vol"].values[0], closest_spot["BF_Vol"].values[0]

    def compute_vanna_volga_adjustment(self):
        """
        Computes the Vanna-Volga correction for the vanilla FX option.

        :return: Vanna-Volga adjusted vanilla option price.
        """
        vv_model = VannaVolga(self.S, self.K, self.T, self.sigma, 
                              self.rd, self.rf, self.market_volatility_atm, 
                              self.market_volatility_rr, self.market_volatility_bf)
        
        return vv_model.vanna_volga_price()

    def compute_barrier_probability_adjustment(self):
        """
        Adjusts the risk-neutral probability of hitting the barrier using Vanna-Volga.

        :return: Adjusted probability of hitting the barrier.
        """
        d1 = self.compute_d1()
        d2 = self.compute_d2()
        
        mu = (self.rd - self.rf - 0.5 * self.sigma ** 2) / self.sigma ** 2
        lambda_term = np.sqrt(d1**2 + 2 * mu * np.log(self.B / self.S))

        # Adjusted probability of barrier activation
        P_adj = norm.cdf(-lambda_term) * self.market_volatility_rr  

        return P_adj

    def calculate_vanna_volga_barrier_price(self):
        """
        Computes the Vanna-Volga adjusted FX Barrier Option price using market data.

        :return: Vanna-Volga adjusted barrier option price.
        """
        vanilla_vv_price = self.compute_vanna_volga_adjustment()
        P_barrier_adj = self.compute_barrier_probability_adjustment()
        
        # Compute base barrier price
        barrier_price = self.calculate_barrier_price()
        
        # Apply VV correction to the barrier option price
        barrier_price_vv = barrier_price + P_barrier_adj * (vanilla_vv_price - barrier_price)
        
        return barrier_price_vv
