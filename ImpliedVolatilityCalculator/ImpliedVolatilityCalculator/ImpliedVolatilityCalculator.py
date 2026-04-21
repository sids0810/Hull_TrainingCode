#ImpliedVolatilityCalculator.py
#By Siddhant Dhoot
#Finds the volatility that the market is pricing in for a stock

import math
import scipy.stats as sci

def calculate_call_price(spot, strike, rfr, div, time, vol):

    d1 = (math.log(spot/strike) + (rfr - div + (vol**2)/2) * time) / (vol * math.sqrt(time))

    d2 = d1 - (vol*math.sqrt(time))

    call_price = ((spot*math.exp(-div*time))*sci.norm.cdf(d1)) - ((strike*(math.exp(-rfr*time)))*sci.norm.cdf(d2))

    return call_price

def calculate_put_price(spot, strike, rfr, div, time, vol):

    d1 = ((math.log(spot/strike))+(rfr - div + ((vol**2/2))*time))/(vol*math.sqrt(time))

    d2 = d1 - (vol*math.sqrt(time))

    put_price = ((strike*(math.exp(-rfr*time)))*sci.norm.cdf(-d2)) - ((spot*math.exp(-div*time))*sci.norm.cdf(-d1))

    return put_price

def implied_vol_calc(spot, strike, rfr, div, time, option_type, market_price, vol_guess):

    tolerance = 1e-5

    if(option_type==1):
        step = 0
        call_price = calculate_call_price(spot, strike, rfr, div, time, vol_guess)
        while(abs(market_price-call_price) > tolerance):
            d1 = ((math.log(spot/strike))+(rfr - div + ((vol_guess**2/2)*time)))/(vol_guess*math.sqrt(time))
            n_prime_d1 = math.exp(-0.5 * d1**2) / math.sqrt(2.0 * math.pi)
            vega = spot * math.exp(-div * time) * math.sqrt(time) * n_prime_d1
            vol_guess = vol_guess - ((call_price-market_price)/vega)
            call_price = calculate_call_price(spot, strike, rfr, div, time, vol_guess)
            step+=1
            if(step==100):
                return "Error: 100 iterations with no result"
    elif(option_type==2):
        step = 0
        put_price = calculate_put_price(spot, strike, rfr, div, time, vol_guess)
        while(abs(market_price-put_price) > tolerance):
            d1 = ((math.log(spot/strike))+(rfr - div + ((vol_guess**2/2)*time)))/(vol_guess*math.sqrt(time))
            n_prime_d1 = math.exp(-0.5 * d1**2) / math.sqrt(2.0 * math.pi)
            vega = spot * math.exp(-div * time) * math.sqrt(time) * n_prime_d1
            diff = put_price - market_price
            if(vega<1e-8):
                vega = 1e-8
            step = diff/vega
            if(step>0.5):
                step = 0.5
            if(step<-0.5):
                step = -0.5
            vol_guess = vol_guess - step
            if(vol_guess<=0):
                vol_guess = 0.0001
            put_price = calculate_put_price(spot, strike, rfr, div, time, vol_guess)
            step+=1
            if(step==100):
                return "Error: 100 iterations with no result"
    return vol_guess

if __name__ == "__main__":

    spot_price = 100
    strike_price = 80
    risk_free_rate = 0.05
    continuous_yield = 0.02
    time_to_maturity = 0.5
    call_or_put = 2
    market_option_price = 0.35
    initial_volatility_guess = 0.1

    implied_vol = implied_vol_calc(spot_price, strike_price, risk_free_rate, continuous_yield, time_to_maturity, call_or_put, market_option_price, initial_volatility_guess)

    print("--Black Scholes Merton Reverse Implied Vol Calculator--")

    print(f"Implied Vol: {implied_vol*100:,.4f}%")



