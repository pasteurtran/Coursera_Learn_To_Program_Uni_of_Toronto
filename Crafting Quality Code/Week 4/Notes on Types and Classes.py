#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:03:07 2017

@author: PasteurTran
"""

class CashRegister(object):
    
    def __init__(self, ones, twos, fives, tens, twenties):
        self.ones = ones
        self.twos = twos
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        
    def __str__(self):
        #return ("Cash Register: " + str(self.ones) + " ones," + str(self.twos) + " twos," + str(self.fives) + " fives,"
        #      + str(self.tens) + " tens," + str(self.twenties) + " twenties.") 
        return ("Cash Register: " +\
                "{0} ones, {1}, twos, {2} fives, {3} tens, {4} twenties".format(
                        self.ones, self.twos, self.fives, self.tens, self.twenties)
                )
        

if __name__ == '__main__':
    """
    Here we initiazlise the module. 
    The print is pulling __str__
    
    """
    cr1 = CashRegister(1,1,1,1,1)
    cr2 = CashRegister(1,2,2,1,0)
    print(cr1)
    print(cr2)
    
    
class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
        """ (Contact, str, str, str) -> NoneType

       Initialize this Contact with first name first_name, last name
       last_name, and email address email_address.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
       
    def add_phone_number(self, telephone_num):
        """ (Contact, str) -> NoneType
    
        Add phone number telephone_num for this contact.
        """
        self.phone_number = telephone_num