import numpy as np
from scipy.stats import norm

# Black Scholes model for Vanilla options
class BlackScholes:
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate):
        """
        spot_price: Current price of the underlying asset (S)
        strike_price: Strike price of the option (K)
        time_to_maturity: Time to expiration in years (T)
        volatility: Volatility of the underlying asset (sigma, annualized)
        domestic_rate: Domestic risk-free interest rate (rd, annualized)
        foreign_rate: Foreign risk-free interest rate (rf, annualized)
        """
        self.S = spot_price
        self.K = strike_price
        self.T = max(time_to_maturity, 1e-10)  # Prevent division by zero
        self.sigma = volatility
        self.rd = domestic_rate
        self.rf = foreign_rate

    def compute_d1(self):
        """Computes d1 for the Black-Scholes formula."""
        return (np.log(self.S / self.K) + (self.rd - self.rf + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def compute_d2(self):
        """Computes d2 for the Black-Scholes formula."""
        return self.compute_d1() - self.sigma * np.sqrt(self.T)

    def calculate_vanilla_price(self, option_type="call"):
        """
        Calculates the price of a European vanilla option (Either call or put).
        
        option_type: 'call' for call option, 'put' for put option
        :return: Option price
        """
        d1 = self.compute_d1()
        d2 = self.compute_d2()

        if option_type.lower() == "call":
            price = np.exp(-self.rf * self.T) * self.S * norm.cdf(d1) - np.exp(-self.rd * self.T) * self.K * norm.cdf(d2)
        elif option_type.lower() == "put":
            price = np.exp(-self.rd * self.T) * self.K * norm.cdf(-d2) - np.exp(-self.rf * self.T) * self.S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Choose 'call' or 'put'.") # Error handling
        
        return price

    def delta(self, option_type='call'): #Function to calculate the delta of the Vanilla option
        """
        Computes the delta of a European option.

        option_type: 'call' or 'put'
        :return: Delta value
        """
        d1 = self.compute_d1()
        if option_type.lower() == 'call':
            return np.exp(-self.rf * self.T) * norm.cdf(d1)
        elif option_type.lower() == 'put':
            return np.exp(-self.rf * self.T) * (norm.cdf(d1) - 1)
        else:
            raise ValueError("Invalid option type. Choose 'call' or 'put'.")
