import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate):
        """
        Initializes the Black-Scholes model parameters.
        :param spot_price: Current price of the underlying asset.
        :param strike_price: Strike price of the option.
        :param time_to_maturity: Time to expiration in years.
        :param volatility: Volatility of the underlying asset (annualized).
        :param domestic_rate: Domestic risk-free interest rate (annualized).
        :param foreign_rate: Foreign risk-free interest rate (annualized).
        """
        self.S = spot_price
        self.K = strike_price
        self.T = time_to_maturity
        self.sigma = volatility
        self.rd = domestic_rate
        self.rf = foreign_rate

    def compute_d1(self):
        """
        Computes d1 for the Black-Scholes formula.
        :return: d1 value.
        """
        return (np.log(self.S / self.K) + (self.rd - self.rf + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def compute_d2(self):
        """
        Computes d2 for the Black-Scholes formula.
        :return: d2 value.
        """
        return self.compute_d1() - self.sigma * np.sqrt(self.T)

    def calculate_vanilla_price(self, option_type="call"):
        """
        Calculates the price of a vanilla European option.
        :param option_type: 'call' for call option, 'put' for put option.
        :return: Option price.
        """
        d1 = self.compute_d1()
        d2 = self.compute_d2()
        
        if option_type == "call":
            price = np.exp(-self.rf * self.T) * self.S * norm.cdf(d1) - np.exp(-self.rd * self.T) * self.K * norm.cdf(d2)
        elif option_type == "put":
            price = np.exp(-self.rd * self.T) * self.K * norm.cdf(-d2) - np.exp(-self.rf * self.T) * self.S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Choose 'call' or 'put'.")
        
        return price
