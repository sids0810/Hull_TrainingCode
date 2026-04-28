
import math
from scipy.stats import norm
from EuropeanOption import EuropeanOption

class CallOption(EuropeanOption):

    def price(self):

        return (self.S * math.exp(-self.q * self.T) * norm.cdf(self.d1())) - (self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2()))

    def delta(self):

        return (math.exp(-self.q * self.T) * norm.cdf(self.d1()))



