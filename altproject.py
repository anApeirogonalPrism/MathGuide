import math
from math import gcd
import tkinter as tk
from fractions import Fraction
import time


user_database = [
    'Torrez'
]
password_database = [
    '20111128'
]
email_database = [
    'tsoicheukkit@skhsjps.edu.hk'
]

i = 1
bus_text = 'Booting up system.'

def boot_system():
    global i, bus_text
    while i == 1:
        print(bus_text)
        time.sleep(1)
        i += 1
        while i == 2:
            bus_text = bus_text + '.'
            print(bus_text)
            time.sleep(1)
            i += 1
            try:
                while i == 3:
                    bus_text = bus_text + '.'
                    print(bus_text)
                    time.sleep(1)
                    i += 1
                    if i == 4:
                        pass
            except:
                pass

def acc_gen():
    j = 0
    while j == 0:
        new_username = input("Enter original username:")
        if user_database.count(new_username) >= 1:
            print("This username is taken")
        else:
            new_password = input("Enter strong password:")
            user_database.append(new_username)
            password_database.append(new_password)
            print("New account registered into system. You can now login.")
            j = 1
    return

def logged_in(username):
    print("Congrats, you logged in as " + username + '!')
    time.sleep(4.43)
    choice = input("Do you want to CREATE new account, LOG in with different account or EXIT?   ")
    return choice

secret_db = (122.284754 * 4316 / 7649)
secret_db = round(secret_db, None)
boot_system()
print('Welcome to Torrez\'s Maths Guide For Beginners!!')
time.sleep(4.20)
print('Please login to your account.')
time.sleep(2.51) #I use my phone's stopwatch to record how long it take for at least an average person to read
need_new_acc = input("Torrez's user storage database is not updatable, so do you want to create new acc? Yes/No   ")
need_new_acc.lower()
i = 0
while i == 0:
    if need_new_acc.lower() == "yes":
        need_new_acc = "no"
        acc_gen()
    elif need_new_acc.lower() == "no":
        username = input("Username:")
        if user_database.count(username) == 0:
            print("I can't find the account.")
        else:
            password = input("Password:")
            email = input('Email: ')
            if password == password_database[user_database.index(username)] and email == email_database[user_database.index(username)] and password_database[email_database.index(email)] and email_database[password_database.index(password)]:
                print("Logged in successfully")
                select = logged_in(username)
                if select.lower() == "create":
                    need_new_acc = "yes"
                elif select.lower() == "log":
                    need_new_acc = "no"
                elif select.lower() == "exit":
                    i = 1
            else:
                print("Sorry, password or email incorrect. Restart to try again.")