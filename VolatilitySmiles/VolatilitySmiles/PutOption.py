
import math
from scipy.stats import norm
from EuropeanOption import EuropeanOption

class PutOption(EuropeanOption):

    def price(self):
        return (self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2())) - (self.S * math.exp(-self.q * self.T) * norm.cdf(-self.d1()))

    def delta(self):

        return (math.exp(-self.q * self.T) * (norm.cdf(self.d1())-1))




