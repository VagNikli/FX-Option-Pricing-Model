# **FX Barrier Option Pricing**
A detailed Implementation of Black-Scholes, Binomial Tree, and Vanna-Volga Methods for FX Option Pricing.

## **Project Overview**
This project provides an in-depth **FX options pricing framework**, implementing **vanilla options, barrier options, and Vanna-Volga pricing adjustments**. It includes:

- **Black-Scholes Model** for vanilla FX options.
- **Binomial Tree Model** for pricing FX barrier options.
- **Vanna-Volga Model** for incorporating **market-implied volatility corrections**.
- **Synthetic Market Data Generator** using the **SABR model** to simulate realistic FX volatility surfaces.

**Key Features:**
- Mathematical foundation for all pricing models.
- Python-based efficient implementations.
- Visualizations and comparison of different models.
- Custom market data simulation to mimic real FX volatility behavior.

---

## **Repository Structure**
Vanna-Volga-FX-Barrier-Option-Pricing/ │── notebooks/ # Jupyter notebooks for tests and visualization │ ├── 01_black_scholes_basics.ipynb │ ├── 02_barrier_options.ipynb │ ├── 03_vanna_volga_method.ipynb │ │── src/ # Python modules for different models │ ├── black_scholes.py │ ├── binomial_barrier_option.py │ ├── vanna_volga.py │ ├── vanna_volga_barrier.py │ ├── synthetic_market_data.py │ ├── main_script.py │ ├── utils.py │ │── fx_volatility_surface.png # Sample FX volatility surface visualization │── README.md # Project documentation │── requirements.txt # Required Python dependencies │── .gitignore # Git ignored files

---

## **Model Assumptions**
Each model in this project operates under specific assumptions:

### **1️. Black-Scholes Model**
✔ Assumes **constant volatility**, which is unrealistic in real-world FX markets.  
✔ Uses a **lognormal price distribution**, meaning prices follow a geometric Brownian motion.  
✔ Suitable only for **European-style options** (cannot handle early exercise or barriers).  

### **2️. Binomial Tree for FX Barrier Options**
✔ Models the **price evolution in discrete time steps**, allowing more flexibility.  
✔ Can handle **American and exotic options** (e.g., knock-in/knock-out barrier options).  
✔ Assumes **lognormal distribution at each step**, which may not perfectly match FX market behavior.  

### **3️. Vanna-Volga Pricing for FX Options**
✔ Adjusts **Black-Scholes pricing** using **market-implied volatility corrections**.  
✔ Assumes **fixed volatility weights** instead of dynamically calibrated values.  
✔ Requires **synthetic or market-implied volatilities**, meaning **real market quotes improve accuracy**.  


## **Implemented Models**
### **1️. Black-Scholes Model**
The **Black-Scholes model** is used for **pricing European vanilla options** in the FX market. 

**Implemented Features:**
- Computes **call and put option prices**.
- Computes **Greeks (Delta)**.
- Plots **option price vs. strike price**.

🔹 **Limitations:**
- Does not handle **barrier options**.
- Assumes **constant volatility**, which is unrealistic for FX markets.


### **2️. Binomial Tree for FX Barrier Options**
Barrier options are knock-in or knock-out when the price crosses a defined level. The binomial tree method accurately prices these options.

**Implemented Features:**
- Supports **all types of barrier options**.
- Allows **custom number of steps for accuracy**.
- Visualizes the **binomial tree structure**.

🔹 **Limitations:**
- **Computationally expensive** for large step sizes.
- Assumes **lognormal price distribution**, which may not capture FX market behavior.


## **3️. Vanna-Volga Pricing for FX Options**
The **Vanna-Volga model** is a **market-consistent approach** to pricing FX options by incorporating **market-implied volatility corrections** beyond Black-Scholes.

### **Implemented Features:**
- Computes **Black-Scholes price** for vanilla options.
- Adjusts prices using **Vanna-Volga corrections** to account for **market skew**.
- Supports **FX pairs with SABR-implied volatilities**.

### **Limitations:**
- Uses **fixed Vanna & Volga weights (α, β)** instead of **dynamically calibrated values**.
- No **real FX market quotes**; relies on **simulated SABR volatilities**.

## **Synthetic Market Data Simulation**
The **synthetic market data module** simulates **realistic FX implied volatility surfaces** using the **SABR model**.

### **Implemented Features:**
- Generates **FX volatility smiles** using the **SABR model**.
- Simulates **realistic forward and implied volatility curves**.
- Supports **various FX pairs (EUR/USD, GBP/USD, USD/JPY, etc.)**.

### **Limitations:**
- Does not use **real market quotes** (relies on **simulated volatilities**).
- Assumes **lognormal distribution**, which may **not fully capture FX market behavior**.

## **Visualizations**
### **Implemented Visualizations**
- **FX Volatility Smile** (SABR Model).
- **Black-Scholes vs. Vanna-Volga Pricing**.
- **Binomial Tree for Barrier Options**.

### **Example Graphs**
- **FX Volatility Smile:** `fx_volatility_surface.png`
- **Binomial Tree Visualization**.
- **Comparison of Pricing Models for EUR/USD, GBP/USD, USD/JPY**.

---

## **Limitations**
### **🔹 No Real FX Option Quotes:**
- The model simulates **volatility surfaces using SABR**, but **real market quotes** would provide **more precise pricing**.

### **🔹 Fixed Vanna & Volga Weights:**
- The **Vanna-Volga model** currently **uses fixed weights (α, β)** instead of **dynamically calibrated values**.

### **🔹 Performance Issues for Large Steps in Binomial Tree:**
- **Large binomial steps** increase **computation time**, making it **slower for high precision pricing**.

---

## **Future Research & Enhancements**
### **🔹 Dynamic Calibration of Vanna-Volga Weights**
- Instead of **fixed α and β**, **calibrate weights dynamically** based on **market data**.

### **🔹 Integration with Real FX Market Data**
- Retrieve **live implied volatility quotes** from **Bloomberg or Reuters**.

### **🔹 Alternative Models (Jump-Diffusion, Heston, Local Volatility)**
- Compare **Vanna-Volga vs. Local Volatility models** for **FX options**.


## **References & Further Reading**
This project is based on well-established **financial models** and **research papers**. Below are some useful references:

- **Binomial Tree Model**:  
  Cox, J. C., Ross, S. A., & Rubinstein, M. (1979). "Option Pricing: A Simplified Approach." *Journal of Financial Economics*.

- **Vanna-Volga Method**:  
  Castagna, A., & Mercurio, F. (2007). "Consistent Pricing of FX Options with the Vanna-Volga Method." *International Journal of Theoretical and Applied Finance*.

- **SABR Model for Implied Volatility**:  
  Hagan, P. S., Kumar, D., Lesniewski, A. S., & Woodward, D. E. (2002). "Managing Smile Risk." *Wilmott Magazine*.


## **Contact Information**
For any inquiries or contributions, feel free to reach out:

👤 **Author**: Evangelos Niklitsiotis  
📧 **Email**: vagelisnikli@gmail.com  






