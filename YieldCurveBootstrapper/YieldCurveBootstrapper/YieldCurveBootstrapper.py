#YieldCurveBootstrapper.py
#By Siddhant Dhoot
#This program bootstraps a yield curve using coupon bearing bonds

import math
import matplotlib.pyplot as plt

def curve_bootstrapper(coupon_bonds: tuple, yield_curve: dict) -> float:

    """
    Calculates the zero rates using the appropriate discount rates

    Args: 
    coupon_bonds (tuple): A single coupon from the input list containing maturity, coupon rate in decimal, and price
    yield_curve (dictionary): A dictionary matching zero rates to their appropriate maturities

    Output:
    zero_rate (float): The calculated zero rate from the given bond for the specified maturity
    """

    maturity, coupon_rate, price = coupon_bonds

    if(maturity<=0.5):
        coupon = 100 * (coupon_rate / 2)
        zero_rate = -math.log(price / (100 + coupon)) / maturity
        return zero_rate

    if(maturity>0.5):
        coupon = 100*(coupon_rate/2)
        pv_coupons = 0
        time=0.5
        while time<maturity:
            discount_rate = get_rate(time, yield_curve)
            pv_coupons += coupon*(math.exp(-discount_rate*time))
            time+=0.5
        zero_rate = -math.log((price-pv_coupons)/(100+coupon))/maturity
        return zero_rate

def get_rate(target_time, yield_curve):
    if target_time in yield_curve:
        return yield_curve[target_time]
    known_times = list(yield_curve.keys())
    smaller_times = [t for t in known_times if t < target_time]
    if not smaller_times:
        raise ValueError(f"Cannot interpolate: Target time {target_time} is lower than our shortest bond.")
    time_1 = max(smaller_times)
    rate_1 = yield_curve[time_1]
    larger_times = [t for t in known_times if t > target_time]
    if not larger_times:
        raise ValueError(f"Cannot interpolate: Target time {target_time} is beyond our longest bond.")
    time_2 = min(larger_times)
    rate_2 = yield_curve[time_2]
    slope = (rate_2 - rate_1) / (time_2 - time_1)
    interpolated_rate = rate_1 + (target_time - time_1) * slope
    return interpolated_rate

def build_complete_par_curve(sparse_par_rates):
    max_maturity = max(sparse_par_rates.keys())
    complete_curve = {} 
    current_time = 0.5
    while current_time <= max_maturity:
        current_time = round(current_time, 1) 
        if current_time in sparse_par_rates:
            complete_curve[current_time] = sparse_par_rates[current_time]
        else:
            complete_curve[current_time] = get_rate(current_time, sparse_par_rates)
        current_time += 0.5
    return complete_curve
                    

if __name__ == "__main__":
    print("---Yield Curve Bootstrapper---")
    raw_par_rates = {
        0.5: 0.0515, 
        1.0: 0.0490, 
        2.0: 0.0460, 
        5.0: 0.0425
    }

    complete_par_rates = build_complete_par_curve(raw_par_rates)

    coupon_bonds = []
    for maturity in sorted(complete_par_rates.keys()):
        coupon_bonds.append((maturity, complete_par_rates[maturity], 100))

    yield_curve = {}
    
    for bond in coupon_bonds:
        maturity = bond[0]
        yield_curve[maturity] = curve_bootstrapper(bond, yield_curve)

    for maturity, rate in yield_curve.items():
        print(f"Maturity {maturity} Yrs : {rate * 100:.4f}%")

    maturities = list(yield_curve.keys())
    curve_pct = [rate * 100 for rate in yield_curve.values()]

    plt.figure(figsize=(9, 6))

    plt.plot(maturities, curve_pct, marker='o', linestyle='-', color='blue')

    plt.title('Bootstrapped Continuous Zero Curve', fontweight='bold')
    plt.xlabel('Maturity (Years)')
    plt.ylabel('Zero Rate (%)')
    plt.grid(True, alpha=0.3)

    for i, j in zip(maturities, curve_pct):
        plt.text(i, j + 0.2, f'{j:.2f}%', ha='center', va='bottom')

    plt.ylim(min(curve_pct) - 0.5, max(curve_pct) + 0.75)

    plt.show()