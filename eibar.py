import csv


def eibar():
    
    a = 1
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
            fnames = ['id', 'day', 'time', 'location', 'opponent', 'result']

            f = 1
            while f == 1:
                i = int(input("Write the match id: "))
                w = input("Write the match day (dd.mm.yyyy): ")
                t = input("Write the match time (00:00): ")

                c = 1
                while c == 1:
                    p = str(input("Write where the match was played (Enter C or F): "))
                    if p == 'C' or p == 'F':
                        c = 0
                    else:
                        print("You have to enter C or F")
                        c = 1

                o = str(input("Write the opponent: "))
                r = input("Write the match result (0:0): ")

                dict = {'id': i, 'day': w, 'time': t, 'location': p, 'opponent': o, 'result': r}

                with open('eibar.csv', 'a+') as csv_file: #block to append into a csv file
                    dict_object = csv.DictWriter(csv_file, fieldnames=fnames)

                    dict_object.writerow(dict)

                b = 1
                while b == 1:
                    a = input("Do you want to enter another match? (y/n): ")

                    if a == 'n':
                        f = 0
                        a = 1
                        b = 0

                    elif a == 'y':
                        f = 1
                        b = 0

                    else:
                        print("You have to enter 'y' or 'n'")
                        b = 1

        elif option == "2":
            with open('eibar.csv', "r") as csv_file: #block to read a csv file
                reader = csv.reader(csv_file)

                for item in reader:
                    print(item)

        elif option == "3":
            print("Goodbye")
            a = a - 1

        else:
            print("Invalid option. Please enter a number between 1 and 3.")
