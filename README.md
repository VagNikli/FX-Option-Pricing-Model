# **FX Barrier Option Pricing**
A detailed Implementation of Black-Scholes, Binomial Tree, and Vanna-Volga Methods for FX Option Pricing

## **Project Overview**
This project provides an in-depth **FX option pricing framework**, implementing **vanilla options, barrier options, and Vanna-Volga pricing adjustments**. It includes:

- **Black-Scholes Model** for vanilla FX options.
- **Binomial Tree Model** for pricing FX barrier options.
- **Vanna-Volga Model** for incorporating **market-implied volatility corrections**.
- **Synthetic Market Data Generator** using the **SABR model** to simulate realistic FX volatility surfaces.

**Key Features:**
- **Mathematical foundation** for all pricing models.
- **Python-based efficient implementations**.
- **Visualizations and comparison of different models**.
- **Custom market data simulation** to mimic real FX volatility behavior.

---

## **Repository Structure**
Vanna-Volga-FX-Barrier-Option-Pricing/ │── notebooks/ # Jupyter notebooks for tests and visualization │ ├── 01_black_scholes_basics.ipynb │ ├── 02_barrier_options.ipynb │ ├── 03_vanna_volga_method.ipynb │ │── src/ # Python modules for different models │ ├── black_scholes.py │ ├── binomial_barrier_option.py │ ├── vanna_volga.py │ ├── vanna_volga_barrier.py │ ├── synthetic_market_data.py │ ├── main_script.py │ ├── utils.py │ │── fx_volatility_surface.png # Sample FX volatility surface visualization │── README.md # Project documentation │── requirements.txt # Required Python dependencies │── .gitignore # Git ignored files

---

## ** Implemented Models**
### **1️. Black-Scholes Model**
The **Black-Scholes model** is used for **pricing European vanilla options** in the FX market. 

**Implemented Features:**
- Computes **call and put option prices**.
- Computes **Greeks (Delta)**.
- Plots **option price vs. strike price**.

🔹 **Limitations:**
- Does not handle **barrier options**.
- Assumes **constant volatility**, which is unrealistic for FX markets.

🔹 **Run the Black-Scholes Model:**
```python
from black_scholes import BlackScholes

bs_model = BlackScholes(spot_price=1.20, strike_price=1.10, time_to_maturity=1, 
                         volatility=0.2, domestic_rate=0.05, foreign_rate=0.02)

call_price = bs_model.calculate_vanilla_price("call")
print(f"Call Option Price: {call_price:.4f}")

### **2️. Binomial Tree for FX Barrier Options**
Barrier options **knock-in** or **knock-out** when the price crosses a defined level. The **binomial tree method** is used to accurately price these options.

**Implemented Features:**
- Supports **all types of barrier options**.
- Allows **custom number of steps for accuracy**.
- Visualizes the **binomial tree structure**.

🔹 **Limitations:**
- **Computationally expensive** for large step sizes.
- Assumes **lognormal price distribution**, which may not capture FX market behavior.

🔹 **Run the Binomial Barrier Model:**
```python
from binomial_barrier_option import BinomialBarrierOption

barrier_option = BinomialBarrierOption(spot_price=1.20, strike_price=1.10, time_to_maturity=1, 
                                       volatility=0.2, domestic_rate=0.05, foreign_rate=0.02, 
                                       barrier_level=1.10, barrier_type="down-out", option_type="call", steps=500)

print(f"Barrier Option Price: {barrier_option.price():.4f}")
