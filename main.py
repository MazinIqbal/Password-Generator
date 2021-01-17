## Simple Password Generator by Mazin Iqbal.
import random

## These are the various characters that will be used to generate a password.
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "`~!@#$%^&*()[]-_+=/\\<>?:;'.,"

## Choose to allow only certain characters to be used to generate a password. True = Yes, False = No.
upper, lower, number, symbol = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if number:
    all += digits
if symbol:
    all += symbols

## Ask user to input number of characters and number of passwords they would like generated.
while 1:
    password_length = int(input("How many characters should be in your password? "))
    password_count = int(input("How many passwords would you like to generate? "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_length):
            password_gen = random.choice(all)
            password = password + password_gen
        print("Password created: ", password)