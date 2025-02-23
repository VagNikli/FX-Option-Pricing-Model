import numpy as np
import pandas as pd
from black_scholes import BlackScholes
from synthetic_market_data import MarketDataSimulation
import numpy as np
from black_scholes import BlackScholes

# Vanna-Volga pricing model for FX options.
class VannaVolga:
    def __init__(self, spot_price, strike_price, time_to_maturity, domestic_rate, foreign_rate, 
                 alpha=0.015, beta=0.5, rho=-0.3, nu=0.2):
        """ 
        Parameters:
        spot_price (float): Current FX spot price (e.g., EUR/USD ~ 1.20).
        strike_price (float): Strike price of the option.
        time_to_maturity (float): Time to expiration in years.
        domestic_rate (float): Domestic risk-free rate (e.g., USD risk-free rate).
        foreign_rate (float): Foreign risk-free rate (e.g., EUR risk-free rate).
        alpha (float): SABR volatility parameter (vol of vol).
        beta (float): SABR skew parameter (controls dependency on forward price).
        rho (float): SABR correlation (correlation between spot and vol).
        nu (float): SABR volatility of volatility.
        """
        self.S = spot_price
        self.K = strike_price
        self.T = time_to_maturity
        self.rd = domestic_rate
        self.rf = foreign_rate
        self.market_data = MarketDataSimulation(spot_price, alpha, beta, rho, nu)

    def get_implied_vol(self):
        """Computes implied volatility using the SABR model for realistic FX pricing."""
        vol = self.market_data.sabr_volatility(self.K, self.T) 
        return vol if not np.isnan(vol) else 0.10  # Default to a reasonable FX vol if NaN

    def black_scholes_price(self, option_type="call"):
        """Computes the Black-Scholes price using SABR-implied volatility."""
        vol = self.get_implied_vol()
        bs = BlackScholes(self.S, self.K, self.T, vol, self.rd, self.rf)
        return bs.calculate_vanilla_price(option_type)

    def compute_vanna_volga_corrections(self):
        """Computes Vanna and Volga corrections based on FX market-implied volatilities."""
        atm_vol = self.get_implied_vol()

        # Simulating FX Risk Reversal (RR) and Butterfly (BF) volatilities
        rr_vol = 0.05  # Lower RR vol for FX (~0.5% vs. higher values in equities)
        bf_vol = 0.02  # Lower Butterfly vol for FX (~0.2%)

        # Compute implied volatilities for OTM call and put
        vol_call_otm = atm_vol + rr_vol / 2 + bf_vol / 2
        vol_put_otm = atm_vol - rr_vol / 2 + bf_vol / 2

        # Compute Vanna & Volga Greeks
        vanna = (vol_call_otm - vol_put_otm) / 2  # Measures skew sensitivity
        volga = bf_vol  # Measures convexity sensitivity

        return vanna, volga

    def vanna_volga_price(self, option_type="call"):
        """Computes the Vanna-Volga price correction for FX options."""
        bs_price = self.black_scholes_price(option_type)

        # Get Vanna & Volga corrections
        vanna, volga = self.compute_vanna_volga_corrections()

        #  Fixed weights for now - can be optimized later
        alpha, beta = 0.2, 0.5  
        vv_price = bs_price + alpha * vanna + beta * volga # formual for adjustments
        return vv_price

# Example usage:
if __name__ == "__main__":
    # Define  FX parameters for EUR/USD option
    vv_model = VannaVolga(spot_price=1.20,
                          strike_price=1.10, 
                          time_to_maturity=2, 
                          domestic_rate=0.06, 
                          foreign_rate=0.04, 
                          alpha=0.015, beta=0.5,rho=0.0, nu=0.2)

    print(f"Black-Scholes Price: {vv_model.black_scholes_price('call'):.4f}")
    print(f"Vanna-Volga Adjusted Price: {vv_model.vanna_volga_price('call'):.4f}")
