import csv

a = 1
m = 1
while a == 1:
    print("===================================")
    print("SDEIBAR MENU")
    print("===================================")
    print("1. Append new SD Eibar statistics")
    print("2. Read the SD Eibar statistics")
    print("3. Exit the menu")
    print("===================================")

    option = input("Enter your option (1-3): ")

    if option == "1":
        f = open("eibar.csv", "a+")  # a append, r read, write

        a = 1
        while a == 1:
            d = input("Write the match day (dd/mm/yyyy): ")
            t = input("Write the match time (00:00): ")
            p = input("Write where the match was played (Enter H or O): ")
            o = input("Write the opponent: ")
            r = input("Write the match result (0-0): ")


            s2 = input("Do you want to enter another match? (y/n): ")
            if s2 == "y":
                a = 1
                m = 0
            elif s2 == "n":
                a = 0
                m = 0
            else:
                print("You have to enter y or n.")
                m = 1
        f.close()
        a = 1

    elif option == "2":
        f = open("eibar.csv", "r")
        a = 1
        while a != 0:
            reader = csv.DictReader(f)
            for row in reader:
                print(row['Id'], row['Day'])
        a = 1

    elif option == "3":
        print("Goodbye")
        a = a - 1

    else:
        print("Invalid option. Please enter a number between 1 and 3.")