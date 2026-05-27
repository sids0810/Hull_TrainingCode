#Mortgage_Amortizer.py
#By Siddhant Dhoot

if __name__ == "__main__":

    principal = 500000
    interest_rate = 0.06
    term = 360 
    cpr = 0.1

    interest_rate = interest_rate / 12

    pmt = principal * ((interest_rate*((1+interest_rate)**term))/((1+interest_rate)**term - 1))

    print(f"Monthly Payment: {pmt:.2f}")

    smm = 1 - ((1 - cpr)**(1/12))

    interest_paid = interest_rate * principal

    required_paydown = pmt - interest_paid

    voluntary_prepayment = principal * smm

    print(f"Interest Paid: {interest_paid:.2f}")

    print(f"Required Principal Paydown: {required_paydown:.2f}")

    print(f"Voluntary Principal Prepaid: {voluntary_prepayment:.2f}")