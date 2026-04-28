#VolatilitySmiles.py
#By Siddhant Dhoot

from EuropeanOption import EuropeanOption
from CallOption import CallOption

import matplotlib.pyplot as plt

if __name__ == "__main__":

    spot = 100.0
    rfr = 0.05
    q = 0.00
    time = 30/252
    strikes = [90,95,100,105,110]
    mkt_prices = [11.39,6.94,3.05,0.71,0.06]

    implied_volatilities=[]

    for i in range(len(strikes)):

        option = CallOption(spot, strikes[i], time, rfr, q, 0.2)
        implied_volatilities.append(option.calculate_implied_vol(mkt_prices[i]))

    print(f"{'Strike Price':<15} {'Market Price':^15} {'Implied Volatility':>15}")
    print("-"*52)

    for i in range(len(strikes)):
        print(f"{strikes[i]:<15.2f} {mkt_prices[i]:^15.2f} {implied_volatilities[i]*100:>15.4f}%")

    plt.plot(strikes,implied_volatilities)
    plt.title("Volatility Curve")
    plt.xlabel("Strike Price")
    plt.ylabel("Implied Volatility")

    plt.show()