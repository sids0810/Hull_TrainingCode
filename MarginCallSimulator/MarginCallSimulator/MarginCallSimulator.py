#MarginCallSimulator.py
#By Siddhant Dhoot
#This simulator looks into Mark-to-Market and Margin Account mechanics

import pandas as pd

def main():
    print("--- Futures Margin Call Simulator ---")
    num_contracts, lot_size, initial_margin, maintenance_margin, entry_price, position = inputs()
    
    total_initial = num_contracts * initial_margin
    total_maint = num_contracts * maintenance_margin
    
    daily_variation_calculator(total_initial, total_maint, lot_size, entry_price, position, num_contracts)

def inputs():
    num_contracts = int(input("Number of contracts: "))
    lot_size = int(input("Lot size (e.g., 100 for Gold): "))
    initial_margin = float(input("Initial margin per contract: "))
    maintenance_margin = float(input("Maintenance margin per contract: "))
    entry_price = float(input("Entry price: "))
    pos_input = input("Position (L/S): ").upper()
    return num_contracts, lot_size, initial_margin, maintenance_margin, entry_price, pos_input

def daily_variation_calculator(total_init, total_maint, lot_size, entry_price, position, num_contracts):
    num_days = int(input("Enter the number of days to be simulated: "))
    mult = 1 if position == "L" else -1
    
    balance = total_init
    prev_price = entry_price
    cumulative_pnl = 0 
    history = []

    for i in range(num_days):
        day_price = float(input(f"Day {i+1} Price: "))
        
        daily_pnl = (day_price - prev_price) * lot_size * num_contracts * mult
        cumulative_pnl += daily_pnl 
        balance += daily_pnl
        margin_call = 0
        if balance < total_maint:
            margin_call = total_init - balance
            balance += margin_call 
        
        history.append({
            "Day": i + 1,
            "Price": day_price,
            "Daily PnL": daily_pnl,
            "Cum. PnL": cumulative_pnl,  
            "Account Balance": balance,
            "Margin Call": margin_call
        })
        
        prev_price = day_price

    df = pd.DataFrame(history)
    print("\n--- Futures Settlement & Margin Report ---")
    print(df.to_string(index=False, formatters={
        'Price': '{:,.2f}'.format,
        'Daily PnL': '{:,.2f}'.format,
        'Cum. PnL': '{:,.2f}'.format,
        'Account Balance': '{:,.2f}'.format,
        'Margin Call': '{:,.2f}'.format
    }))

if __name__ == "__main__":
    main()