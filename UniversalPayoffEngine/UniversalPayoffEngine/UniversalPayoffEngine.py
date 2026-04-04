#UniversalPayoffEngine.py
#By Siddhant Dhoot 
#A universal theoretical payoff engine for Options and Forwards

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("--- Universal Derivative Payoff Engine ---")
    choice, position, premium, strike, spot_lower, spot_higher = inputs()
    prices, returns = calculations(choice, position, premium, strike, spot_lower, spot_higher)
    show_payoff(prices, returns, choice, position, strike)

def inputs():
    print("\nSelect the type of derivative:")
    print("1. Call Option")
    print("2. Put Option")
    print("3. Forward Contract")
    
    choice = 0
    while choice not in [1, 2, 3]:
        choice = int(input("Enter your choice (1/2/3): "))
        
    position = input("Enter L for Long and S for Short Position: ").upper()
    premium = float(input("Enter the premium/cost to enter (Use 0 for forwards): "))
    strike = float(input("Enter the strike/delivery price: "))
    spot_lower = float(input("Enter the lowest spot price to model: "))
    spot_higher = float(input("Enter the highest spot price to model: "))
    
    return choice, position, premium, strike, spot_lower, spot_higher

def calculations(choice, position, premium, strike, spot_lower, spot_higher):
    prices = np.linspace(spot_lower, spot_higher, 100)
    returns = np.zeros_like(prices)
    
    mult = 1 if position == "L" else -1

    if choice == 1:   
        returns = np.maximum(prices - strike, 0)
    elif choice == 2: 
        returns = np.maximum(strike - prices, 0)
    elif choice == 3: 
        returns = prices - strike

    net_returns = (returns * mult) - (premium * mult)
    
    return prices, net_returns 

def show_payoff(prices, returns, choice, position, strike):
    names = {1: "Call Option", 2: "Put Option", 3: "Forward Contract"}
    title = f"{position == 'L' and 'Long' or 'Short'} {names[choice]} Payoff (Strike: {strike})"

    print("\n--- Payoff Distribution ---")
    print(f"{'Spot Price':>10} | {'Net PnL':>10}")
    print("-" * 25)
    for p, r in zip(prices[::10], returns[::10]):
        print(f"{p:>10.2f} | {r:>10.2f}")

    plt.figure(figsize=(8, 5))
    plt.plot(prices, returns, color='blue', linewidth=2)
    plt.axhline(0, color='black', linewidth=1, linestyle='--') 
    plt.axvline(strike, color='red', linewidth=1, linestyle=':') 
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Spot Price at Expiration', fontsize=12)
    plt.ylabel('Net Profit / Loss', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.fill_between(prices, returns, 0, where=(returns >= 0), color='green', alpha=0.1)
    plt.fill_between(prices, returns, 0, where=(returns < 0), color='red', alpha=0.1)
    
    print("\nDisplaying Payoff Graph...")
    plt.show()

if __name__ == "__main__":
    main()