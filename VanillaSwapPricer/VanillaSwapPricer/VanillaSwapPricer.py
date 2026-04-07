#VanillaSwapPricer.py
#By Siddhant Dhoot
#Calculates the value of a fixed-for-floating vanilla swap

import math

def calculate_swap_value(yield_curve: dict, notional: float, fixed_rate: float) -> float:

    maturities = list(yield_curve.keys())
    zero_rates = list(yield_curve.values())
    pv_swap_payments = 0
    for i in range(len(maturities)):

        if(i==0):
            implied_forward_rate = zero_rates[i]
            fixed_payment = notional * fixed_rate * maturities[i]
            floating_payment = notional * (math.exp(implied_forward_rate*maturities[i])-1)
        else:
            implied_forward_rate = ((zero_rates[i]*maturities[i])-(zero_rates[i-1]*maturities[i-1]))/(maturities[i]-maturities[i-1])
            fixed_payment = notional * fixed_rate * (maturities[i]-maturities[i-1])
            floating_payment = notional * (math.exp(implied_forward_rate*(maturities[i]-maturities[i-1]))-1)
        net_swap_payment = floating_payment - fixed_payment
        pv_swap_payments += net_swap_payment * math.exp(-zero_rates[i]*maturities[i])
    return pv_swap_payments

if __name__ == "__main__":

    yield_curve = {0.5: 0.10469, 1.0: 0.12038, 1.5: 0.10475, 2.0: 0.13402}
    notional = 10000000
    fixed_rate = 0.115

    swap_value = calculate_swap_value(yield_curve, notional, fixed_rate)

    print(f"Swap Value: ${swap_value:,.4f}")
