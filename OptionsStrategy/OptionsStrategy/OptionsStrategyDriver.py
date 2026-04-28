#OptionsStrategyDriver.py
#By Siddhant Dhoot

from OptionsStrategy import OptionsStrategy
from EuropeanOption import EuropeanOption
from CallOption import CallOption
from PutOption import PutOption

if __name__ == "__main__":

    strat = OptionsStrategy("Test1")

    option1 = CallOption(100,100,30/365,0.05,0.03,0.2,10)
    option2 = PutOption(100,100,30/365,0.05,0.03,0.2,10)

    strat.add_leg(option1, 2)

    strat.add_leg(option2, -1)

    print(strat.net_premium())

