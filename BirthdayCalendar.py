import calendar
import datetime
import csv
try:
    f = open('birthdays.csv', 'r')
except:
    f = open('birthdays.csv', 'w')
    with f:
        fnames = ['First name', 'Surname', 'Year', 'Month', 'Day']
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        a = "yes"
        while a == "yes":
            fn = input("Enter your friend's name: ")
            sn = input("Enter your friend's surname: ")
            
            a = input("Do you want to add another friend?")
else:
    f = open('birthdays.csv', 'a')
