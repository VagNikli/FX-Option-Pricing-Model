# Barrier Option PDE file (empty for now)
import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes

class FXBarrierOption(BlackScholes):
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate, barrier_level, barrier_type):
        """
        Initializes an FX Barrier Option.
        :param barrier_level: The barrier price level.
        :param barrier_type: One of ['up-in', 'up-out', 'down-in', 'down-out'].
        """
        super().__init__(spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate)
        self.B = barrier_level
        self.barrier_type = barrier_type

    def N(self, x):
        """ Standard normal cumulative distribution function """
        return norm.cdf(x)

    def calculate_barrier_price(self):
        """
        Computes the price of an FX barrier option using closed-form formulas.
        """
        if self.barrier_type not in ["up-in", "up-out", "down-in", "down-out"]:
            raise ValueError("Invalid barrier type. Choose 'up-in', 'up-out', 'down-in', or 'down-out'.")

        vanilla_price = self.calculate_vanilla_price()
        d1 = self.compute_d1()
        d2 = self.compute_d2()
        mu = (self.rd - self.rf - 0.5 * self.sigma ** 2) / self.sigma ** 2
        lambd = np.sqrt(d1**2 + 2 * mu * np.log(self.B / self.S))

        # Reflective price calculations
        refl_call = self.S * np.exp(-self.rf * self.T) * self.N(-lambd) - self.K * np.exp(-self.rd * self.T) * self.N(-lambd + self.sigma * np.sqrt(self.T))
        
        if self.barrier_type == "down-out":
            return max(vanilla_price - refl_call, 0)
        elif self.barrier_type == "down-in":
            return refl_call
        elif self.barrier_type == "up-out":
            return max(vanilla_price - refl_call, 0)
        elif self.barrier_type == "up-in":
            return refl_call

