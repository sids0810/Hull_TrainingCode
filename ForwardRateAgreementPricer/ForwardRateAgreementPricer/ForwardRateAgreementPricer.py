#ForwardRateAgreementPricer.py
#By Siddhant Dhoot 
#A theoretical FRA pricer based on continous zero rates

import math

def forward_rate_calculator(first_zero_rate: float,second_zero_rate: float ,fra_start: float, fra_end: float) -> float:
    """
    Calculates the implied forward rate 

    Args:
    first_zero_rate (float): the zero rate for time until the start of the FRA
    second_zero_rate (float): the zero rate for time until the end of the FRA
    fra_start (float): the time between now and that start of the FRA
    fra_end (float): the time between now and the end of the FRA

    Output:
    implied_forward_rate (float): the implied forward rate for the actual duration of the FRA 
    """
    implied_forward_rate = ((second_zero_rate*fra_end)-(first_zero_rate*fra_start))/(fra_end-fra_start)
    return implied_forward_rate

def calculate_fra_value(notional: float, fixed_rate: float, implied_forward_rate: float, fra_start: float, fra_end: float, second_zero_rate: float) -> float:
    """
    Calculates the value of the FRA from the perspective of receiving the fixed rate and paying the floating rate

    Args:
    notional (float): notional amount for the FRA
    implied_forward_rate (float): the implied forward rate for the actual duration of the FRA
    fra_start (float): the time between now and that start of the FRA
    fra_end (float): the time between now and the end of the FRA
    second_zero_rate (float): the zero rate for time until the end of the FRA

    Output:
    fra_value (float): the present value of the FRA
    """
    fra_value = notional * (fixed_rate-implied_forward_rate) * (fra_end-fra_start) * (math.exp(-second_zero_rate*fra_end))
    return fra_value

if __name__=="__main__":
    notional = 10000000
    fixed_rate = 0.04
    fra_start = 1
    fra_end = 1.5
    first_zero_rate = 0.03
    second_zero_rate = 0.035

    print("--- Forward Rate Agreement Pricer ---")
    implied_forward_rate = forward_rate_calculator(first_zero_rate,second_zero_rate,fra_start, fra_end)
    fra_value = calculate_fra_value(notional, fixed_rate, implied_forward_rate, fra_start, fra_end, second_zero_rate)

    print(f"Implied Forward Rate: {implied_forward_rate*100:,.4f}%")
    print(f"Present Value of Forward Rate Agreement: ${fra_value:,.4f}")