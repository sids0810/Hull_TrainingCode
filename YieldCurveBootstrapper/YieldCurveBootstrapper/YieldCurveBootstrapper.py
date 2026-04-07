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
        zero_rate = -((math.log(price/100))/maturity)
        return zero_rate

    if(maturity>0.5):
        coupon = 100*(coupon_rate/2)
        pv_coupons = 0
        time=0.5
        while time<maturity:
            discount_rate = yield_curve[time]
            pv_coupons += coupon*(math.exp(-discount_rate*time))
            time+=0.5
        zero_rate = -math.log((price-pv_coupons)/(100+coupon))/maturity
        return zero_rate
                    

if __name__ == "__main__":
    print("---Yield Curve Bootstrapper---")
    coupon_bonds = [(0.25,0,97.50),(0.5,0,94.90),(1,0.08,96),(1.5,0.12,101.60),(2,0.15,102.40)]

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