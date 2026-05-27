#AsianPricer.py
#By Siddhant Dhoot

import numpy as np

if __name__ == "__main__":

    initial_price = 100
    strike_price = 100
    rfr = 0.05
    vol = 0.2
    time_to_maturity = 1
    time_steps = 252
    num_simulations = 100000

    dt = time_to_maturity/time_steps

    shocks = np.random.normal(0,1,(time_steps, num_simulations))

    daily_returns = np.exp((rfr - 0.5 * vol**2) * dt + vol * np.sqrt(dt) * shocks)

    price_paths = np.vstack([np.ones(num_simulations), daily_returns])

    price_paths = initial_price * np.cumprod(price_paths, axis=0)

    mean_prices = np.mean(price_paths[1:], axis=0)

    payoff = np.ones((time_steps, num_simulations))

    payoff = np.maximum(0, mean_prices-strike_price)

    mean_payoff = np.mean(payoff)

    option_price = mean_payoff * np.exp(-rfr*time_to_maturity)

    print(f"Asian Call Option Price: {option_price:.4f}")