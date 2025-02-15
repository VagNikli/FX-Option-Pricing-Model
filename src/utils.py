import numpy as np
from scipy.stats import norm

def normal_cdf(x):
    return norm.cdf(x)

def normal_pdf(x):
    return norm.pdf(x)

def format_price(price):
    return f"${price:.2f}"
