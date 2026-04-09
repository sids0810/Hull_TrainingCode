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

def get_fixed_rate(yield_curve: dict) -> float:
    maturities = list(yield_curve.keys())
    pv_sum = 0.00

    last_maturity = maturities[-1]
    last_rate = yield_curve[last_maturity]
    final_discount_factor = math.exp(-last_rate * last_maturity)

    for i in range(len(maturities)):
        current_time = maturities[i]
        rate = yield_curve[current_time]

        if i == 0:
            delta_t = current_time
        else:
            delta_t = current_time - maturities[i-1]

        discount_factor = math.exp(-rate * current_time)
        pv_sum += discount_factor * delta_t

    fair_fixed_rate = (1 - final_discount_factor) / pv_sum

    spread = 0.0003
    quote_rate = fair_fixed_rate - spread

    return quote_rate



if __name__ == "__main__":

    yield_curve = {0.5: 0.050848, 1.0: 0.048380, 1.5: 0.046890, 2.0: 0.045388}
    notional = 100000000
    fixed_rate = get_fixed_rate(yield_curve)

    swap_value = calculate_swap_value(yield_curve, notional, fixed_rate)

    print(f"Fixed Rate: {fixed_rate*100:,.4f}%")
    print(f"Swap Value: ${swap_value:,.4f}")
