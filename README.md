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
