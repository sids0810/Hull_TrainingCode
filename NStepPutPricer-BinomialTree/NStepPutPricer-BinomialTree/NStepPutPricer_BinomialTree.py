#BinomialTreeEngine.py
#By Siddhant Dhoot
#A recursive N-Step Binomial Pricer for American Options

import numpy as np
import math

def price_american_put(S: float, K: float, r: float, q: float, sigma: float, T: float, N: float) -> float:
    """
    Prices an American Put Option using an N-Step Binomial Tree.
    
    Parameters:
    S (float): Spot price of the underlying asset
    K (float): Strike price
    r (float): Risk-free interest rate (continuous)
    sigma (float): Volatility of the underlying asset
    T (float): Time to maturity in years
    N (int): Number of binomial steps
    
    Returns:
    float: The calculated present value of the American Put Option
    """

    dt = T / N
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp((r-q) * dt) - d) / (u - d)
    discount_factor = math.exp(-r * dt)
    
    stock_path = np.zeros(N+1)

    for j in range(N+1):
        stock_path[j] = S * (u**(j)) * d**(N-j)

    for l in range(N+1):
        stock_path[l] = max(K-stock_path[l],0)

    for m in range(N-1,-1,-1):
        for n in range(m+1):
            continuation_value = discount_factor * ((p*stock_path[n+1])+((1-p)*stock_path[n]))
            current_spot = S * u**n * d**(m-n)
            intrinsic_value = K - current_spot
            stock_path[n] = max(continuation_value, intrinsic_value)
    
    return stock_path[0]


if __name__ == "__main__":
    
    spot = 100
    strike = 100
    rate = 0.05
    continuous_yield = 0.0
    vol = 0.20
    time = 1.0
    steps = 1000
    
    calculated_price = price_american_put(spot, strike, rate, continuous_yield, vol, time, steps)
    
    print("--- Binomial Tree Pricer ---")
    print(f"Calculated American Put Price: ${calculated_price:.4f}")
