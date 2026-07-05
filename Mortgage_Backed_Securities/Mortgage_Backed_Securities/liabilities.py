import numpy as np
import math

class Tranche:

    def __init__(self, name, initial_balance, rate):
        self.name = name
        self.initial_balance = initial_balance 
        self.rate = rate 
        self.current_balance = initial_balance

        self.historical_interest_paid = []
        self.historical_principal_paid = []
        self.historical_balance = []
        self.historical_losses_absorbed = []

    def pay_interest(self, cash_available):
        interest_owed = self.current_balance * (self.rate/12)
        interest_paid = min(interest_owed, cash_available)
        self.historical_interest_paid.append(interest_paid)
        return cash_available-interest_paid

    def pay_principal(self, cash_available):
        principal_paid = min(self.current_balance, cash_available)
        self.historical_principal_paid.append(principal_paid)
        self.current_balance = self.current_balance - principal_paid
        return cash_available-principal_paid

    def absorb_losses(self, loss_amount):
        loss_taken = min(self.current_balance, loss_amount)
        self.current_balance = self.current_balance - loss_taken
        self.historical_losses_absorbed.append(loss_taken)
        return loss_amount-loss_taken

    def record_balance(self):
        self.historical_balance.append(self.current_balance)

    def get_name(self):
        return self.name

    def get_initial_balance(self):
        return self.initial_balance

    def get_rate(self):
        return self.rate

    def get_historical_interest_paid(self):
        return self.historical_interest_paid

    def get_historical_principal_paid(self):
        return self.get_historical_principal_paid

    def get_historical_balance(self):
        return self.historical_balance

    def get_historical_losses_absorbed(self):
        return self.get_historical_losses_absorbed



