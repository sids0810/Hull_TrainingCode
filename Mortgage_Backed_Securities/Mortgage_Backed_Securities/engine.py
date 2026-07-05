import numpy as np
import math
from assets import LoanPool
from liabilities import Tranche

class CapitalStructureGenerator:

    def __init__(self, pool_balance, base_expected_loss):
        self.pool_balance = pool_balance
        self.base_expected_loss = base_expected_loss
        self.tranche_multiples = {'AAA': 5, 'AA': 4, 'A': 3, 'BBB': 2, 'Equity': 0}
        self.tranche_coupon = {'AAA': 0.05, 'AA': 0.06, 'A': 0.07, 'BBB': 0.09, 'Equity': 0.15}
        self.tranche_list = []

    def generate_tranches(self):
        current_top_pct = 1.0
        for key,val in self.tranche_multiples.items():
            required_ce = min(1.0, self.base_expected_loss * val)
            tranche_pct = max(0.0, current_top_pct - required_ce)
            tranche_balance = self.pool_balance*tranche_pct
            if(tranche_balance>0):
                self.tranche_list.append(Tranche(key,tranche_balance,self.tranche_coupon[key]))
            current_top_pct = required_ce
        return self.tranche_list

class WaterfallEngine:

    def __init__(self, tranches):
        self.tranches = tranches

    def run_single_month(self, period_cash, period_loss):
        for tranche in self.tranches:
            period_cash = tranche.pay_interest(period_cash)
        for tranche in self.tranches:
            period_cash = tranche.pay_principal(period_cash)
        for tranche in reversed(self.tranches):
            period_loss = tranche.absorb_losses(period_loss)
        for tranche in self.tranches:
            tranche.record_balance()

    def run_waterfall(self, loan_pool):

        for i in range(loan_pool.get_wam()):
            cash = loan_pool.historical_interest[i] + loan_pool.historical_scheduled_principal[i] + loan_pool.historical_prepayments[i]
            losses = loan_pool.historical_defaults[i]
            self.run_single_month(cash, losses)
