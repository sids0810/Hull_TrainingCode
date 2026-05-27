#Duration_Convexity_Approximator.py
#By Siddhant Dhoot

def present_value(face_value, coupon_rate, ytm, time_to_maturity):
    sum_pvcf = 0
    coupon = (coupon_rate/2)*face_value 
    for i in range(1, (time_to_maturity*2)+1):
        if(i == time_to_maturity*2):
            cash_flow = face_value + coupon 
        else:
            cash_flow = coupon 
        sum_pvcf += cash_flow / ((1+(ytm/2))**i)
    return sum_pvcf

if __name__ == "__main__":
    face_value = 100
    coupon_rate = 0.05
    ytm = 0.05
    time_to_maturity = 10

    price = present_value(face_value, coupon_rate, ytm, time_to_maturity)

    price_down = present_value(face_value, coupon_rate, ytm+0.0001, time_to_maturity)

    price_up = present_value(face_value, coupon_rate, ytm-0.0001, time_to_maturity)

    duration = (price_up - price_down) / (2*0.0001*price)
    
    convexity = (price_up + price_down - (2*price)) / (price * (0.0001**2))
 
    print(f"Approx Duration: {duration:.4f}")
    print(f"Approx Convexity: {convexity:.4f}")

