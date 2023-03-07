import calendar
import datetime
import csv


try:
    f = open('birthdays.csv', 'r')
    fnames = ['First name', 'Surname', 'Year', 'Month', 'Day']
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
            year = input("Enter the year your friend was born: ")
            correct = "no"
            while correct == "no":
                month = int(input("What month was he/she born? (01 to 12) "))
                if 0 < month < 13:
                    correct = "yes"
                else:
                    print("The month has to be between 1 and 12")
            correctDay = "no"
            while correctDay == "no":
                day = int(input("What day was he/she born? "))
                if month == 4 or month == 6 or month == 9 or month == 11:
                    if day > 30:
                        print("Incorrect value. This month has 30 days. ")
                        correctDay = "no"
                    else:
                        correctDay = "yes"
                if month == 2:
                    if day > 29:
                        print("Incorrect value. This month has 28 days (29 on a leap year). ")
                        correctDay = "no"
                    if day == 29:
                        answer = input("Was he born in a leap year? ")
                        if answer == "yes":
                            correctDay = "yes"
                        else:
                            print("Enter a correct day")
                            correctDay = "no"
                    if day < 29:
                        correctDay = "yes"
                else:
                    if day > 31:
                        print("Incorrect value. This month has 31 days.")
                        correctDay = "no"
                    else:
                        correctDay = "yes"
            writer.writerow({'First name': fn, 'Surname': sn, 'Year': year, 'Month': month, 'Day': day})
            a = input("Do you want to add another friend?(yes/no) ")

else:
    f = open('birthdays.csv', 'a')
    writer = csv.DictWriter(f, fieldnames=fnames)
    a = "yes"
    while a == "yes":
        fn = input("Enter your friend's name: ")
        sn = input("Enter your friend's surname: ")
        year = input("Enter the year your friend was born: ")
        correct = "no"
        while correct == "no":
            month = int(input("What month was he/she born? (01 to 12) "))
            if 0 < month < 13:
                correct = "yes"
            else:
                print("The month has to be between 1 and 12")
        correctDay = "no"
        while correctDay == "no":
            day = int(input("What day was he/she born? "))
            if month == 4 or month == 6 or month == 9 or month == 11:
                if day > 30:
                    print("Incorrect value. This month has 30 days. ")
                    correctDay = "no"
                else:
                    correctDay = "yes"
            if month == 2:
                if day > 29:
                    print("Incorrect value. This month has 28 days (29 on a leap year). ")
                    correctDay = "no"
                if day == 29:
                    answer = input("Was he born in a leap year? ")
                    if answer == "yes":
                        correctDay = "yes"
                    else:
                        print("Enter a correct day")
                        correctDay = "no"
                if day < 29:
                    correctDay = "yes"
            else:
                if day > 31:
                    print("Incorrect value. This month has 31 days.")
                    correctDay = "no"
                else:
                    correctDay = "yes"
        writer.writerow({'First name': fn, 'Surname': sn, 'Year': year, 'Month': month, 'Day': day})
        a = input("Do you want to add another friend?(yes/no) ")
