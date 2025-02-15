import sys
import os

# Ensure `src/` is included in Python's search path
project_dir = os.getcwd()  # ✅ Works in Jupyter Notebooks too
sys.path.append(os.path.join(project_dir, "src"))  # Add src/ to path

# Import our models
from black_scholes import BlackScholes
from barrier_options import BarrierOptionMC
from vanna_volga import VannaVolga

# Define common parameters for FX options
spot_price = 100         # Spot FX rate
strike_price = 100       # Strike price
time_to_maturity = 1     # 1 year to expiry
volatility = 0.2         # 20% annualized volatility
domestic_rate = 0.05     # 5% risk-free rate (domestic)
foreign_rate = 0.02      # 2% risk-free rate (foreign)

# ----- Test Black-Scholes Model -----
bs_model = BlackScholes(spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate)
call_price_bs = bs_model.calculate_vanilla_price("call")
put_price_bs = bs_model.calculate_vanilla_price("put")
print(f"✅ Black-Scholes Call Price: {call_price_bs:.4f}")
print(f"✅ Black-Scholes Put Price: {put_price_bs:.4f}")

# ----- Test Barrier Option Pricing (Monte Carlo) -----
barrier_level = 110  # Set a barrier level
barrier_type = "up-in"
barrier_option = BarrierOptionMC(spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate, barrier_level, barrier_type, num_simulations=10000)

barrier_call_price = barrier_option.calculate_barrier_price(option_type="call")
print(f"✅ Barrier Call Option Price (Monte Carlo): {barrier_call_price:.4f}")

# ----- Test Vanna-Volga Pricing -----
vv_model = VannaVolga(spot_price, strike_price, time_to_maturity, volatility, domestic_rate, foreign_rate)
vv_adjusted_price = vv_model.vanna_volga_price()
print(f"✅ Vanna-Volga Adjusted Call Price: {vv_adjusted_price:.4f}")

# ----- Summary -----
print("\n✅ All models executed successfully!")
