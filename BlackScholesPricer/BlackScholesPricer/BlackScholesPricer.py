#BlackScholesPricer.py
#By Siddhant Dhoot
#A theoretical pricer for options using the Black Scholes Model

import scipy.stats as sci
import math

def calculate_prices(spot, strike, rfr, div, time, vol):

    d1 = (math.log(spot/strike) + (rfr - div + (vol**2)/2) * time) / (vol * math.sqrt(time))

    d2 = d1 - (vol*math.sqrt(time))

    call_price = ((spot*math.exp(-div*time))*sci.norm.cdf(d1)) - ((strike*(math.exp(-rfr*time)))*sci.norm.cdf(d2))

    put_price = ((strike*(math.exp(-rfr*time)))*sci.norm.cdf(-d2)) - ((spot*math.exp(-div*time))*sci.norm.cdf(-d1))

    return call_price, put_price

if __name__ == "__main__":

    spot_price = 32
    strike_price = 35
    risk_free_rate = 0.03
    continuous_yield = 0.0
    time_to_maturity = 1/12
    volatility = 0.4

    call, put = calculate_prices(spot_price, strike_price, risk_free_rate, continuous_yield, time_to_maturity, volatility)

    print("---Black-Scholes-Merton Options Pricer for European Options---")

    print(f"Call Price: {call:,.4f}")

    print(f"Put Price: {put:,.4f}")

