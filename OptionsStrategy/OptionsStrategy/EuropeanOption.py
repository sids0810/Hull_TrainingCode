
import math
from scipy.stats import norm

class EuropeanOption():

    def __init__(self, S, K, T, r, q, sigma, mkt_price):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.q = q
        self.sigma = sigma
        self.mkt_price = mkt_price
        self.sigma = self.calculate_implied_vol()


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

    def calculate_implied_vol(self):
        tolerance = 1e-5
        option_price = self.theoretical_price()
        step=0
        while(abs(self.mkt_price-option_price) > tolerance):
            vega = self.vega()
            diff = option_price - self.mkt_price
            if(vega<1e-8):
                vega = 1e-8
            adj = diff/vega
            if(adj>0.5):
                adj = 0.5
            if(adj<-0.5):
                adj = -0.5
            self.sigma = self.sigma - adj
            if(self.sigma<=0):
                self.sigma = 0.0001
            option_price = self.theoretical_price()
            step+=1
            if(step==100):
                return "Error: 100 iterations with no result"
        return self.sigma

    def set_spot(self, spot):
        self.S = spot

    def get_spot(self):
        return self.S

    def set_strike(self, strike):
        self.K = strike

    def get_strike(self):
        return self.K

    def set_expiry(self, expiry):
        self.T = expiry

    def get_expiry(self):
        return self.T

    def set_rfr(self, rfr):
        self.r = rfr

    def get_rfr(self):
        return self.r

    def set_div_yield(self, div_yield):
        self.q = div_yield

    def get_div_yield(self):
        return self.q

    def set_sigma(self, vol):
        self.sigma = vol

    def get_sigma(self):
        return self.sigma

    def set_mkt_price(self, market_price):
        self.mkt_price = market_price

    def get_mkt_price(self):
        return self.mkt_price








