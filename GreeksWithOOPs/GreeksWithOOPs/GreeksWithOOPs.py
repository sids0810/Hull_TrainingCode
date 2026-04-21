
import math
from scipy.stats import norm
from EuropeanOption import EuropeanOption
from CallOption import CallOption
from PutOption import PutOption
from Portfolio import Portfolio

if __name__ == "__main__":

    S = 100       # Current stock price: $100
    K_call = 105  # Out-of-the-money Call strike
    K_put = 95    # Out-of-the-money Put strike
    T = 0.5       # 6 months to expiration
    r = 0.05      # 5% risk-free rate
    q = 0.0       # 0% dividend yield
    sigma = 0.20  # 20% implied volatility

    call_leg = CallOption(S, K_call, T, r, q, sigma)
    put_leg = PutOption(S, K_put, T, r, q, sigma)

    trading_desk = Portfolio()

    trading_desk.add_position(call_leg, 5)
    trading_desk.add_position(put_leg, -3)

    book_delta = trading_desk.net_delta()
    book_gamma = trading_desk.net_gamma()

    print("--- End of Day Risk Report ---")
    print(f"Net Portfolio Delta: {book_delta:.2f} shares")
    print(f"Net Portfolio Gamma: {book_gamma:.4f}")