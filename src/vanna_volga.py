import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes
import numpy as np
from black_scholes import BlackScholes
from black_scholes import BlackScholes
from volatility_surface import VolatilitySurface
from black_scholes import BlackScholes
from volatility_surface import VolatilitySurface

class VannaVolga:
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility_surface, 
                 domestic_rate, foreign_rate, alpha=0.5, beta=0.5):
        """
        Implements the Vanna-Volga pricing model with dynamic volatility extraction.

        Parameters:
        spot_price (float): Current FX rate.
        strike_price (float): Strike price of the option.
        time_to_maturity (float): Option maturity (years).
        volatility_surface (VolatilitySurface): Market-implied vol surface.
        domestic_rate (float): Domestic risk-free rate.
        foreign_rate (float): Foreign risk-free rate.
        alpha (float): Initial weight for Vanna correction.
        beta (float): Initial weight for Volga correction.
        """
        self.S = spot_price
        self.K = strike_price
        self.T = time_to_maturity
        self.vol_surface = volatility_surface  # Store the volatility surface
        self.rd = domestic_rate
        self.rf = foreign_rate
        self.alpha = alpha
        self.beta = beta

        # Extract volatilities dynamically from the surface
        self.atm_vol = self.vol_surface.get_volatility(self.K, self.T)
        self.call_vol = self.vol_surface.get_volatility(self.K * 1.05, self.T)  # OTM Call Volatility
        self.put_vol = self.vol_surface.get_volatility(self.K * 0.95, self.T)  # OTM Put Volatility

        # Compute RR and BF volatilities
        self.rr_vol = self.call_vol - self.put_vol
        self.bf_vol = (self.call_vol + self.put_vol) / 2 - self.atm_vol

    def black_scholes_price(self, option_type="call"):
        """Computes the Black-Scholes price using dynamically extracted volatility."""
        bs = BlackScholes(self.S, self.K, self.T, self.atm_vol, self.rd, self.rf)
        return bs.calculate_vanilla_price(option_type)

    def vanna_volga_price(self, option_type="call"):
        """
        Computes the Vanna-Volga price correction using dynamically extracted volatilities.
        """
        bs_price = self.black_scholes_price(option_type)
        vanna = self.rr_vol / 2  # Approximate Vanna
        volga = self.bf_vol  # Approximate Volga
        return bs_price + self.alpha * vanna + self.beta * volga
