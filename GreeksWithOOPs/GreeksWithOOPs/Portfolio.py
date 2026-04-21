
import math
import EuropeanOption
import CallOption
import PutOption

class Portfolio():

    def __init__(self):
        self.positions = []

    def add_position(self, option, qty):
        new_position = (option,qty)
        self.positions.append(new_position)

    def net_delta(self):
        net_delta = 0
        for opt, qty in self.positions:
            net_delta += opt.delta() * qty * 100
        return net_delta

    def net_gamma(self):
        net_gamma = 0
        for opt, qty in self.positions:
            net_gamma += opt.gamma() * qty * 100
        return net_gamma