
import math
from scipy.stats import norm
from EuropeanOption import EuropeanOption

class CallOption(EuropeanOption):

    def theoretical_price(self):

        return (self.S * math.exp(-self.q * self.T) * norm.cdf(self.d1())) - (self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2()))

    def delta(self):

        return (math.exp(-self.q * self.T) * norm.cdf(self.d1()))

    def theta(self):
        return (-(((self.S*math.exp(-self.q * self.T))*self.sigma*norm.pdf(self.d1()))/(2*math.sqrt(self.T))) + (self.q*(self.S*math.exp(-self.q * self.T))*norm.cdf(self.d1())) - (self.r * (self.K * math.exp(-self.r * self.T))*norm.cdf(self.d2())))/365


