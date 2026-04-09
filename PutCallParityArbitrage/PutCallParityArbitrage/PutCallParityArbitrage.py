#PutCallParityArbitrage.py
#A calculator to check if the market is pricing options 
#By Siddhant Dhoot

import math

def arbitrage_scanner(spot_price: float, strike_price: float, continuous_yield: float, risk_free_rate: float, time_to_expiry: float, call_price: float, put_price: float):

    fiduciary_call = call_price+ (strike_price * math.exp(-risk_free_rate*time_to_expiry))

    protective_put = put_price + (spot_price * math.exp(-continuous_yield*time_to_expiry))

    tolerance = 0.001

    if abs(fiduciary_call - protective_put) > tolerance:
        if(fiduciary_call>protective_put):
            print("Fiduciary Call Overpriced")
            print("Sell Call Option, Borrow Present Value of Strike at Risk Free Rate")
            print("Buy Put Option, Buy Present Value of Stock")
            profit = fiduciary_call - protective_put
            print(f"Arbitrage Profit = ${profit:.4f}")
        else:
            print("Protective Put Overpriced")
            print("Buy Call Option, Invest Present Value of Strike at Risk Free Rate")
            print("Sell Put Option, Sell Present Value of Stock")
            profit = protective_put - fiduciary_call
            print(f"Arbitrage Profit = ${profit:.4f}")
    else:
        print("No Arbitrage Opportunity Found!")

if __name__ == "__main__":

    print("---Continuous Yield Arbitrage Scanner---")

    spot_price = 1.25
    strike_price = 1.25
    continuous_yield = 0.04
    risk_free_rate = 0.05
    time_to_expiry = 0.5
    call_price = 0.0450
    put_price = 0.0348

    arbitrage_scanner(spot_price, strike_price, continuous_yield, risk_free_rate, time_to_expiry, call_price, put_price)

    
