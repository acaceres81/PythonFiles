import calendar
import datetime
import csv

def birthday():

    option="0"
    while option !="3":
        print("What would you like to do? ")
        print("1. add birthdays to my agenda.")
        print("2. See my birthdays' agenda.")
        print("3. exit")
        option = input("enter your choice (1, 2 or 3): ")
        match option:
            case "1":
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
            case "2":
                try:
                    f = open('birthdays.csv', 'r')
                    fnames = ['First name', 'Surname', 'Year', 'Month', 'Day']
                except:
                    print("You need to create the agenda before you can read it.")
                else:
                    f = open('birthdays.csv', 'a')
                    f = open('birthdays.csv', 'r')
                    with f:
                        reader = csv.DictReader(f)
                        writer = csv.DictWriter(f, fieldnames=fnames)
                        headers = reader.fieldnames
                        print(headers)
                        for row in reader:
                            print(row['First name'], row['Surname'], row['Year'], row['Month'], row['Day'])
            case "3":
                print("Thanks for using our programme")
            case other:
                print("That option does not exist.")