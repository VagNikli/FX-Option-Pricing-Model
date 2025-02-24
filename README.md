# **FX Barrier Option Pricing**
A detailed implementation of **Black-Scholes, Binomial Tree, and Vanna-Volga Methods** for FX Option Pricing.

## **Project Overview**
This project provides an in-depth **FX options pricing framework**, implementing **vanilla options, barrier options, and Vanna-Volga pricing adjustments**. It includes:

- **Black-Scholes Model** for **vanilla FX options**.
- **Binomial Tree Model** for **pricing FX barrier options**.
- **Vanna-Volga Model** for **market-implied volatility adjustments**.
- **Synthetic Market Data Generator** using the **SABR model** to simulate realistic FX volatility surfaces.

### **Key Features**
✔ **Mathematical foundation** for all pricing models.  
✔ **Python-based efficient implementations**.  
✔ **Visualizations and comparison of different models**.  
✔ **Custom market data simulation** to mimic real FX volatility behavior.  

---

## **Mathematical Background**
This project relies on well-established mathematical models for option pricing.

### **1️. Black-Scholes Model**
The **Black-Scholes formula** is used to price European options:

- $C = S_0 e^{-r_f T} N(d_1) - K e^{-r_d T} N(d_2)$

- $P = K e^{-r_d T} N(-d_2) - S_0 e^{-r_f T} N(-d_1)$

where:
$d_1 = \frac{\ln(S_0 / K) + (r_d - r_f + \frac{1}{2} \sigma^2) T}{\sigma \sqrt{T}}$, 
$d_2 = d_1 - \sigma \sqrt{T}$

where:  
- $C, P$ = Call and Put option price  
- $S_0$ = Spot price of the underlying asset  
- $K$ = Strike price  
- $T$ = Time to expiration  
- $r_d$ = Domestic risk-free rate  
- $r_f$ = Foreign risk-free rate  
- $\sigma$ = Volatility  
- $N(\cdot)$ = Cumulative normal distribution function  



### **2️. Binomial Tree for FX Barrier Options**
The **binomial model** builds a **lattice** of possible price evolutions:

- At each step, the price can **go up** $( u $) or **down** $(d$):
  - $S_u = S_0 \cdot u, \quad S_d = S_0 \cdot d$

- Risk-neutral probability: $q = \frac{e^{(r_d - r_f) \Delta t} - d}{u - d}$

where:
- $\Delta t = \frac{T}{n}$ (time step per period)
- $u = e^{\sigma \sqrt{\Delta t}}$
- $d = \frac{1}{u}$

For **barrier options**, we apply the following conditions:
- **Knock-In**: Becomes active if the barrier is reached.
- **Knock-Out**: Becomes worthless if the barrier is breached.

At expiration, payoffs are:

- $V_T = \max(S_T - K, 0) \quad \text{(for call)}$

- $V_T = \max(K - S_T, 0) \quad \text{(for put)}$

For **knock-out options**, if at any step $S_t$ crosses the barrier $B$, the option value is set to **zero**.


### **3️. Vanna-Volga Pricing for FX Options**
The **Vanna-Volga method** adjusts **Black-Scholes prices** by incorporating **market-implied volatility skews**.

#### **Vanna and Volga Corrections**
- $\text{Vanna} = \frac{\partial^2 C}{\partial S \, \partial \sigma}$

- $\text{Volga} = \frac{\partial^2 C}{\partial \sigma^2}$

Final **Vanna-Volga adjusted price**:

- $C_{VV} = C_{BS} + \alpha \cdot \text{Vanna} + \beta \cdot \text{Volga}$

where:
- $C_{BS}$ = Black-Scholes price  
- $\alpha, \beta$ = fixed weights  
- Vanna measures **sensitivity to volatility and spot price changes**.  
- Volga measures **sensitivity to volatility shifts**.  


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

## ⚠️**Limitations**
### **🔹 No Real FX Option Quotes**
- The model simulates **volatility surfaces using SABR**, but **real market quotes** would provide **more precise pricing**.

### **🔹 Fixed Vanna & Volga Weights**
- The **Vanna-Volga model** currently **uses fixed weights (α, β)** instead of **dynamically calibrated values**.

### **🔹 Performance Issues for Large Steps in Binomial Tree**
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
- **Black-Scholes Model**: Black, F., & Scholes, M. (1973). *The Pricing of Options and Corporate Liabilities*. *Journal of Political Economy*.  
- **Binomial Tree Model**: Cox, J. C., Ross, S. A., & Rubinstein, M. (1979). *Journal of Financial Economics*.  
- **Vanna-Volga Method**: Castagna, A., & Mercurio, F. (2007). *International Journal of Theoretical and Applied Finance*.  
- **SABR Model for Implied Volatility**: Hagan, P. S., Kumar, D., Lesniewski, A. S., & Woodward, D. E. (2002). *Wilmott Magazine*.

## 📩 **Contact Information**
👤 **Author**: Evangelos Niklitsiotis  
📧 **Email**: vagelisnikli@gmail.com  







