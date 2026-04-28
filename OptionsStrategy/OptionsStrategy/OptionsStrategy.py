#OptionsStrategy.py
#By Siddhant Dhoot

from EuropeanOption import EuropeanOption
from CallOption import CallOption
from PutOption import PutOption

class OptionsStrategy():
    
    def __init__(self, strat_name):
        self.strat_name = strat_name
        self.legs = []

    def add_leg(self, option, qty):
        self.legs.append((option, qty))

    def net_premium(self):
        self.total_premium = 0
        for i in range(len(self.legs)):
            leg_price = self.legs[i][0].get_mkt_price()
            self.total_premium += (leg_price*self.legs[i][1])
        return self.total_premium



