
import math
from scipy.stats import norm

class EuropeanOption():

    def __init__(self, S, K, T, r, q, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.q = q
        self.sigma = sigma

    def d1(self):
        return (math.log(self.S/self.K) + (self.r - self.q + (self.sigma**2)/2) * self.T) / (self.sigma * math.sqrt(self.T))

    def d2(self):
        return self.d1() - (self.sigma*math.sqrt(self.T))

    def gamma(self):
        n_prime_d1 = norm.pdf(self.d1())
        return ((n_prime_d1*math.exp(-self.q * self.T))/(self.S*self.sigma*math.sqrt(self.T)))

    def vega(self):
        n_prime_d1 = norm.pdf(self.d1())
        return (n_prime_d1 * self.S * math.exp(-self.q * self.T) * math.sqrt(self.T))






