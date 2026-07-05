import numpy as np
import math

class LoanPool:

    def __init__(self, initial_balance, wac, wam, cdr, psa_speed):
        self.initial_balance = initial_balance
        self.wac = wac
        self.wam = wam
        self.cdr = cdr
        self.psa_speed = psa_speed

        self.current_balance = initial_balance
        self.historical_scheduled_principal = []
        self.historical_interest = []
        self.historical_prepayments = []
        self.historical_defaults = []
        self.historical_balance = []
        self.historical_balance.append(self.current_balance)
        self.smm_vector = np.empty(360)
        self.mdr_vector = np.empty(360)
        self.rate_vector = np.empty(360)

    def amortize_pool(self):
        for i in range(1,self.wam+1):
            if(i<=30):
                cpr = i*0.002
            if(i>30):
                cpr=0.06
            cpr = cpr * self.psa_speed
            smm = 1 - (math.pow((1-cpr),(1/12)))
            self.smm_vector[i-1] = smm
            mdr = 1 - (math.pow((1-self.cdr),(1/12)))
            self.mdr_vector[i-1] = mdr
            self.rate_vector[i-1] = self.wac/12

        for j in range(self.wam):
            interest = self.current_balance * self.rate_vector[j]
            remaining_term = self.wam - j
            if(remaining_term == 1):
                scheduled_principal = self.current_balance
            else:
                r = self.rate_vector[j]
                n = remaining_term
                payment = self.current_balance * ((r*math.pow((1+r),n))/(math.pow((1+r),n)-1))
                scheduled_principal = payment - interest
            prepayments = (self.current_balance - scheduled_principal) * self.smm_vector[j]
            defaults = (self.current_balance - scheduled_principal - prepayments) * self.mdr_vector[j]

            self.current_balance = self.current_balance-(scheduled_principal+prepayments+defaults)
            self.historical_scheduled_principal.append(max(0,round(scheduled_principal,2)))
            self.historical_interest.append(max(0,round(interest,2)))
            self.historical_prepayments.append(max(0,round(prepayments,2)))
            self.historical_defaults.append(max(0,round(defaults,2)))
            self.historical_balance.append(max(0,round(self.current_balance,2)))

    def get_historical_balance(self):
        return self.historical_balance

    def get_historical_defaults(self):
        return self.historical_defaults

    def get_historical_prepayments(self):
        return self.historical_prepayments

    def get_historical_interest(self):
        return self.historical_interest

    def get_historical_scheduled_principal(self):
        return self.historical_scheduled_principal

    def get_historical_smm(self):
        return self.smm_vector

    def get_historical_mdr(self):
        return self.mdr_vector

    def get_historical_coupon(self):
        return self.rate_vector

    def get_wac(self):
        return self.wac

    def get_wam(self):
        return self.wam

    def get_cdr(self):
        return self.cdr

    def get_psa_speed(self):
        return self.psa_speed


