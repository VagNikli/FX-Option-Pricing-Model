# Vanna-Volga FX Barrier Option Pricing

## 📌 Overview
This project implements **Vanna-Volga pricing for FX barrier options**, incorporating **market-implied volatilities** from real or simulated data.

**Why use Vanna-Volga?**
- The **Black-Scholes model** does not account for **volatility smiles**.
- **FX options traders** rely on **market-implied volatilities** instead of assuming constant volatility.
- The **Vanna-Volga method** corrects **Black-Scholes pricing** by incorporating **Vega, Vanna, and Volga** adjustments.

### 📊 **Key Features**
✔ **Black-Scholes Model** for vanilla FX options  
✔ **Barrier Option Pricing** (Up-In, Up-Out, Down-In, Down-Out)  
✔ **Vanna-Volga Adjustments** for market-consistent pricing  
✔ **Uses real or simulated market volatilities from a CSV file**  
✔ **Visualizes pricing differences between Black-Scholes and Vanna-Volga methods**  

---

## 📌 Project Structure


---

## 📌 Installation Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/Vanna-Volga-FX-Barrier-Option-Pricing.git
cd Vanna-Volga-FX-Barrier-Option-Pricing

## 📌 How to Run

### 📌 1️⃣ Generate Market-Implied Volatility Data  
Before running the pricing models, generate a simulated market volatility dataset:

```bash
python generate_market_data.py



## 📌 Pricing Methodology

### 📌 1️⃣ Black-Scholes Model  
The **Black-Scholes model** is used to price **European vanilla options**, but **it assumes constant volatility**, which does not reflect real-world **FX markets**.

---

### 📌 2️⃣ FX Barrier Options Pricing (Reiner-Rubinstein)  
Barrier options are priced using **closed-form solutions** from **Reiner and Rubinstein (1991)**:

- **Up-in / Down-in** → Option **only exists** if the underlying crosses a barrier.  
- **Up-out / Down-out** → Option **deactivates** if the underlying crosses a barrier.  

---

### 📌 3️⃣ Vanna-Volga Pricing for FX Options  
The **Vanna-Volga method** corrects Black-Scholes by incorporating **market-implied volatility smiles**:

- **Vega** → Sensitivity to volatility.  
- **Vanna** → Sensitivity to volatility & spot price.  
- **Volga** → Sensitivity to volatility convexity.  

---

### 📌 4️⃣ Vanna-Volga for FX Barrier Options  

- **Compute the vanilla VV price** as a base.  
- **Adjust the probability of hitting the barrier** using market volatility skews.  
- **Apply corrections to the barrier option price.**  

## 📌 Future Improvements

**Use real market data from Bloomberg, Reuters, or other sources**   
**Implement Monte Carlo simulations for path-dependent options**   
**Support multiple currency pairs (EUR/USD, USD/JPY, etc.)**  
**Add calibration methods for better fitting of the volatility smile**  
**Optimize the computation for real-time trading applications**   
