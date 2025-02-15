import numpy as np
import pandas as pd

# Define FX spot price range
spot_prices = np.linspace(160, 200, 1000)

# Simulated market-implied volatilities
atm_vols = 0.15 + 0.012 * np.sin(spot_prices / 10)  # Simulated ATM volatility
rr_vols = 0.12 + 0.05 * np.cos(spot_prices / 15)   # Simulated Risk Reversal
bf_vols = 0.11 + 0.009 * np.sin(spot_prices / 12)  # Simulated Butterfly Spread

# Create DataFrame
market_data = pd.DataFrame({
    "Spot": spot_prices,
    "ATM_Vol": atm_vols,
    "RR_Vol": rr_vols,
    "BF_Vol": bf_vols
})

# Save to CSV file
market_data.to_csv("market_vol_data.csv", index=False)
print("Market volatility data saved to market_vol_data.csv")
