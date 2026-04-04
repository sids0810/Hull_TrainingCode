#CrossHedger.py
#By Siddhant Dhoot
#A simulator to calculate the optimal number of contracts for the desired hedge

import yfinance as yf
import pandas as pd

def main():
    print("--- Minimum Variance Cross-Hedging Engine ---")
    portfolio_ticker, hedge_ticker, portfolio_value, hedge_futures_price, lot_size, time_frame = inputs()
    
    print("\nFetching historical data and aligning trading days...")
    historical_returns = historical_analysis(portfolio_ticker, hedge_ticker, time_frame)
    
    if historical_returns.empty:
        print("Error: Could not align historical data. Check your tickers.")
        return

    beta, num_hedge = hedge_calculations(historical_returns, lot_size, hedge_futures_price, portfolio_value, hedge_ticker, portfolio_ticker)
    show_results(beta, num_hedge, portfolio_ticker, hedge_ticker)


def inputs():
    portfolio_ticker = input("Enter the ticker of the asset to be hedged (e.g., AAPL, SPY): ").upper()
    hedge_ticker = input("Enter the ticker of the hedge (e.g., ^GSPC, NQ=F): ").upper()
    portfolio_value = float(input("Enter the total dollar value of the asset to be hedged: "))
    hedge_futures_price = float(input("Enter the current price of the futures contract: "))
    lot_size = int(input("Enter the contract lot size multiplier: "))
    time_frame = int(input("Enter the lookback period for the hedge in months: "))
    
    return portfolio_ticker, hedge_ticker, portfolio_value, hedge_futures_price, lot_size, time_frame


def historical_analysis(portfolio_ticker, hedge_ticker, time_frame):
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.DateOffset(months=time_frame)
    print(f"Pulling data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}...")
    data = yf.download([portfolio_ticker, hedge_ticker], start=start_date, end=end_date)['Close']
    data.dropna(inplace=True)
    historical_returns = data.pct_change().dropna()
    
    return historical_returns


def hedge_calculations(historical_returns, lot_size, hedge_futures_price, portfolio_value, hedge_ticker, portfolio_ticker):
    cov_matrix = historical_returns.cov()
    covariance = cov_matrix.loc[portfolio_ticker, hedge_ticker]
    variance_hedge = historical_returns[hedge_ticker].var()
    beta = covariance / variance_hedge
    num_hedge = beta * (portfolio_value / (hedge_futures_price * lot_size))
    
    return beta, num_hedge


def show_results(beta, num_hedge, portfolio_ticker, hedge_ticker):
    print("\n--- Hedging Strategy Output ---")
    print(f"Historical Beta ({portfolio_ticker} relative to {hedge_ticker}): {beta:.4f}")
    print(f"Optimal Contract Calculation: {num_hedge:.2f} contracts")
    action = "Short" if beta > 0 else "Long"
    print(f"Actionable Trade: {action} {round(abs(num_hedge))} contracts of {hedge_ticker}")
    print("-------------------------------")

if __name__ == "__main__":
    main()