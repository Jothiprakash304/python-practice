import os
import datetime
from datetime import date
import re

def add_validation(card_number,expiry,cv,amount,m_number):
    validation=add_logic(card_number,expiry,cv,amount,m_number)
    return True




def add_logic(card_number,expiry,cv,amount,m_number):

    if not validate_number(card_number):
        return "enter the valid card number"
    if not validate_expiry(expiry):
        return "your card is expired"
    if not validate_cv(cv):
        return "please check the CV number"
    if not validate_amount(amount):
        return "enter the amount"
    if not validate_number(m_number):
        return "please enter the proper mobile number"
    




def validate_number(first):
    if (len(first)>=16):
        return True
def validate_expiry(expiry):
    today=date.today()
    if today.year<=expiry.year:
        return True
def validate_cv(cv):
    if len(cv)==3:
        return True
def validate_amount(amount):
    if amount!=0:
        return True
def validate_number(number):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return re.fullmatch(Pattern,number)

card=validate_number(12345677)
expiry=validate_expiry(1999,2,2)
cv=validate_cv(123)
amount=validate_amount(2000)
number=validate_number(918903878266)
print(card)








