
import math
from scipy.stats import norm
from EuropeanOption import EuropeanOption

class PutOption(EuropeanOption):

    def theoretical_price(self):
        return (self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2())) - (self.S * math.exp(-self.q * self.T) * norm.cdf(-self.d1()))

    def delta(self):

        return (math.exp(-self.q * self.T) * (norm.cdf(self.d1())-1))

    def theta(self):
        return (-(((self.S*math.exp(-self.q * self.T))*self.sigma*norm.pdf(self.d1()))/(2*math.sqrt(self.T))) - (self.q*(self.S*math.exp(-self.q * self.T))*norm.cdf(-self.d1())) + (self.r * (self.K * math.exp(-self.r * self.T))*norm.cdf(-self.d2())))/365





