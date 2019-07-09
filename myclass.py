# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:53:21 2019

@author: paprasad
"""

class CreditCard:
    """A custumer Credit Card"""
    def __init__(self,customer,bank,acnt,limit):
        """create credit card instance"""
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        """return the customer name """
        return self._customer
    
    def get_bank(self):
        """return the customer's bank name"""
        return self._bank
    
    def get_acnt(self):
        """return the customer account name"""
        return self._acnt
    
    def get_limit(self):
        """get customer's limit"""
        return self._limit
    def get_balance(self):
        """return the current balance of customer"""
        return self._balance
    
    def charge(self,price):
        """this method implement charge, if the charge amount is within the limits then 
        the method will return true else it will return false"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        """Process the customer payment, subtract the payment made from balance amount"""
        self._balance -=amount




if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman' , 'California Savings' ,'5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard('John Bowman' , 'California federal' ,'5391 0375 0959 5309' , 3500) )
    wallet.append(CreditCard('John Bowman' , 'California Finance' ,'5309 5391 0375 0959' , 500) )
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        
    for c in range(3):
        print('\n\n-----------------------------')
        print('Custromer = ',wallet[c].get_customer())
        print('bank = ',wallet[c].get_bank())
        print('Account = ',wallet[c].get_acnt())
        print('Limit = ',wallet[c].get_limit())
        print('Balance = ',wallet[c].get_balance())
        
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('*******making payment of 100********')
            print('New Balance = ',wallet[c].get_balance() )
            print("\n")
            
            