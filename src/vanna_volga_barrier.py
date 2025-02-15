import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes
from barrier_options import FXBarrierOption
from vanna_volga import VannaVolga

class VannaVolgaBarrier(FXBarrierOption):
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility, 
                 domestic_rate, foreign_rate, barrier_level, barrier_type, 
                 market_volatility_atm, market_volatility_rr, market_volatility_bf):
        """
        Implements Vanna-Volga adjustment for FX Barrier Options.
        
        :param barrier_level: The price level of the barrier.
        :param barrier_type: Type of barrier ('up-in', 'up-out', 'down-in', 'down-out').
        :param market_volatility_atm: At-the-money implied volatility.
        :param market_volatility_rr: Risk reversal volatility.
        :param market_volatility_bf: Butterfly spread volatility.
        """
        super().__init__(spot_price, strike_price, time_to_maturity, volatility, 
                         domestic_rate, foreign_rate, barrier_level, barrier_type)
        
        self.market_volatility_atm = market_volatility_atm
        self.market_volatility_rr = market_volatility_rr
        self.market_volatility_bf = market_volatility_bf

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
        Computes the Vanna-Volga adjusted FX Barrier Option price.
        
        :return: Vanna-Volga adjusted barrier option price.
        """
        vanilla_vv_price = self.compute_vanna_volga_adjustment()
        P_barrier_adj = self.compute_barrier_probability_adjustment()
        
        # Compute base barrier price
        barrier_price = self.calculate_barrier_price()
        
        # Apply VV correction to the barrier option price
        barrier_price_vv = barrier_price + P_barrier_adj * (vanilla_vv_price - barrier_price)
        
        return barrier_price_vv
