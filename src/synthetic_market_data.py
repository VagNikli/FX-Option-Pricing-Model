#
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class MarketDataSimulation:
    def __init__(self, forward_price, alpha, beta, rho, nu):
        """
        Simulates an FX implied volatility surface using the SABR model
        Parameters:
        forward_price (float): FX spot price (e.g., EUR/USD ~ 1.20).
        alpha (float): SABR model volatility of volatility parameter.
        beta (float): SABR model skew parameter (controls dependency on forward price).
        rho (float): Correlation between asset price and volatility.
        nu (float): Volatility of volatility.
        """
        self.F = forward_price
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.nu = nu

    def sabr_volatility(self, strike_price, time_to_maturity):
        """Computes implied volatility using the SABR model, ensuring realistic FX volatility behavior."""
        if strike_price <= 0 or self.F <= 0 or time_to_maturity <= 0:
            return np.nan  # Ensure no invalid values

        FK = (self.F * strike_price) ** ((1 - self.beta) / 2)
        log_FK = np.log(self.F / strike_price)
        log_FK = np.where(np.abs(log_FK) < 1e-10, 1e-10, log_FK)  # Prevent zero log values

        z = (self.nu / self.alpha) * FK * log_FK
        x_z = np.where(np.abs(z) < 1e-10, 1e-10, np.log((np.sqrt(1 - 2 * self.rho * z + z**2) + z - self.rho) / (1 - self.rho)))

        sigma = (self.alpha / (FK * (1 + ((1 - self.beta) ** 2 / 24) * log_FK ** 2 +
                                     ((1 - self.beta) ** 4 / 1920) * log_FK ** 4))) * (z / x_z)

        return np.maximum(0.001, sigma)  # Ensure positive volatility

    def generate_vol_surface(self, strikes, maturities):
        """Generates the implied volatility surface for given strike prices and maturities."""
        vol_surface = np.zeros((len(maturities), len(strikes)))
        for i, T in enumerate(maturities):
            for j, K in enumerate(strikes):
                vol_surface[i, j] = self.sabr_volatility(K, T)
        return vol_surface

    def plot_volatility_surface(self, strikes, maturities, save_path=None):
        """Visualizes the FX volatility surface in 3D and saves the image."""
        X, Y = np.meshgrid(strikes, maturities)
        Z = self.generate_vol_surface(strikes, maturities)

        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111, projection="3d")
        surface = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="black", alpha=0.9)

        # Labels & Title
        ax.set_title("FX Volatility Surface (SABR Model)", fontsize=14, fontweight="bold")
        ax.set_xlabel("Strike Price", fontsize=12, fontweight="bold")
        ax.set_ylabel("Time to Maturity (Years)", fontsize=12, fontweight="bold")
        ax.set_zlabel("Implied Volatility", fontsize=12, fontweight="bold")

        # Color bar to indicate option price levels
        fig.colorbar(surface, ax=ax, shrink=0.6, aspect=10, label="Implied Volatility")

        # Improve viewing angle
        ax.view_init(elev=25, azim=-45)

        # Save the plot if a save path is provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"FX volatility surface saved to: {save_path}")

        plt.show()

if __name__ == "__main__":
    # Define realistic FX market conditions (EUR/USD-like)
    strikes = np.linspace(0.90, 1.60, 20)  # Strike prices (e.g., EUR/USD)
    maturities = np.linspace(0.1, 3.0, 15)  # Maturities (1 month to 3 years)

    # Initialize market simulation with SABR parameters
    market_sim = MarketDataSimulation(
        forward_price=1.20,  # EUR/USD Spot price
        alpha=0.015,
        beta=0.5,
        rho=0.0,
        nu=0.2   
    )

    # Save the 3D volatility surface image
    save_path = "fx_volatility_surface.png"
    market_sim.plot_volatility_surface(strikes, maturities, save_path=save_path)

