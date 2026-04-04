#ArbitrageCalculator.py
#By Siddhant Dhoot 
#A theoretical Arbitrage Opportunity Finder for Spot vs Futures Prices

import math

def main():
    print("--- Spot-Futures Arbitrage Engine ---")
    spot_price, futures_price, risk_free_rate, dividend_yield, time, trans_cost = inputs()
    
    theoretical_price, diff = theoretical_pricer(spot_price, futures_price, risk_free_rate, dividend_yield, time)
    results(theoretical_price, futures_price, diff, trans_cost)

def inputs():
    spot_price = float(input("Enter the spot price (S0): "))
    futures_price = float(input("Enter the market futures price (F0): "))
    risk_free_rate = float(input("Enter the risk-free rate (r) in decimals (e.g., 0.05): "))
    dividend_yield = float(input("Enter the continuous dividend yield (q) in decimals (e.g., 0.02): "))
    time = float(input("Enter the time to expiry (T) in years: "))
    trans_cost = float(input("Enter total transaction costs (friction) per unit: "))
    return spot_price, futures_price, risk_free_rate, dividend_yield, time, trans_cost

def theoretical_pricer(spot_price, futures_price, risk_free_rate, dividend_yield, time):

    theoretical_price = spot_price * math.exp((risk_free_rate - dividend_yield) * time)
    
    diff = futures_price - theoretical_price
    return theoretical_price, diff

def results(theoretical_price, futures_price, diff, trans_cost):
    print("\n--- Arbitrage Analysis ---")
    print(f"Theoretical Futures Price: {theoretical_price:.4f}")
    print(f"Market Futures Price:      {futures_price:.4f}")
    print(f"Gross Pricing Discrepancy: {diff:.4f}")
    
    if abs(diff) <= trans_cost:
        print(f"\nResult: NO TRADE. The discrepancy ({abs(diff):.4f}) does not exceed transaction costs ({trans_cost:.4f}).")
        return

    if diff > 0:
        net_profit = diff - trans_cost
        print("\nAction: CASH AND CARRY ARBITRAGE")
        print("1. Borrow cash at the risk-free rate.")
        print("2. Buy the physical Spot asset.")
        print("3. Sell (Short) the overpriced Futures contract.")
        print(f"Net Arbitrage Profit per unit: {net_profit:.4f}")
        
    elif diff < 0:
        net_profit = abs(diff) - trans_cost
        print("\nAction: REVERSE CASH AND CARRY ARBITRAGE")
        print("1. Short the physical Spot asset.")
        print("2. Invest the cash proceeds at the risk-free rate.")
        print("3. Buy (Long) the underpriced Futures contract.")
        print(f"Net Arbitrage Profit per unit: {net_profit:.4f}")

if __name__ == "__main__":
    main()