# Barrier Option using Binomial
import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes

# Binomial tree for pricing barrier options
class BinomialBarrierOption:
    def __init__(self, spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate, 
                 barrier_level, barrier_type, option_type="call", steps=100):
        """
        Parameters:
        spot_price (float): Initial stock price (S0).
        strike_price (float): Strike price (K).
        time_to_maturity (float): Time to expiration in years (T).
        volatility (float): Annualized volatility (σ).
        domestic_rate (float): Domestic risk-free interest rate (rd).
        foreign_rate (float): Foreign risk-free interest rate (rf).
        barrier_level (float): Barrier price level (B).
        barrier_type (str): 'up-in', 'up-out', 'down-in', or 'down-out'.
        option_type (str): 'call' or 'put'.
        steps (int): Number of steps in the binomial tree.
        """
        self.S = spot_price
        self.K = strike_price
        self.T = time_to_maturity
        self.sigma = volatility
        self.rd = domestic_rate
        self.rf = foreign_rate
        self.B = barrier_level
        self.barrier_type = barrier_type
        self.option_type = option_type
        self.steps = steps

        if barrier_type not in ["up-in", "up-out", "down-in", "down-out"]:
            raise ValueError("Invalid barrier type. Choose 'up-in', 'up-out', 'down-in', or 'down-out'.") # Error Handling

    def price(self):
        """Computes the price of the barrier option using the binomial tree method."""
        dt = self.T / self.steps
        u = np.exp(self.sigma * np.sqrt(dt))  # Probability going up 
        d = 1 / u  # Probability going down 
        q = (np.exp((self.rd - self.rf) * dt) - d) / (u - d)  # Risk neutral probability
        discount = np.exp(-self.rd * dt)

        # Initialize  price tree
        stock_tree = np.zeros((self.steps + 1, self.steps + 1))
        survival_tree = np.ones((self.steps + 1, self.steps + 1))  

        for i in range(self.steps + 1):
            for j in range(i + 1):
                stock_tree[i, j] = self.S * (u ** (i - j)) * (d ** j)

                if self.barrier_type == "down-out" and stock_tree[i, j] <= self.B:
                    survival_tree[i, j] = 0
                elif self.barrier_type == "up-out" and stock_tree[i, j] >= self.B:
                    survival_tree[i, j] = 0

        # Initialize option price tree
        option_tree = np.zeros((self.steps + 1, self.steps + 1))

        # Compute final payoffs at maturity
        for j in range(self.steps + 1):
            if self.option_type == "call":
                option_tree[self.steps, j] = max(stock_tree[self.steps, j] - self.K, 0)
            elif self.option_type == "put":
                option_tree[self.steps, j] = max(self.K - stock_tree[self.steps, j], 0)

            option_tree[self.steps, j] *= survival_tree[self.steps, j] 

        # Backward induction
        for i in range(self.steps - 1, -1, -1):
            for j in range(i + 1):
                survival_prob = (q * survival_tree[i + 1, j] + (1 - q) * survival_tree[i + 1, j + 1])
                survival_tree[i, j] = survival_prob

                if self.barrier_type in ["down-out", "up-out"]:
                    option_tree[i, j] = survival_prob * discount * (
                        q * option_tree[i + 1, j] + (1 - q) * option_tree[i + 1, j + 1]
                    )
                else:
                    option_tree[i, j] = discount * (q * option_tree[i + 1, j] + (1 - q) * option_tree[i + 1, j + 1])

        return option_tree[0, 0] # Price of binomial tree at last node
