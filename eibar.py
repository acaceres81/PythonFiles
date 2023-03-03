import csv

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

            while m == 1:
                i = input("Write the match id: ")
                d = input("Write the match day (dd.mm.yyyy): ")
                t = input("Write the match time (00:00): ")
                p = input("Write where the match was played (Enter C or F): ")
                o = input("Write the opponent: ")
                r = input("Write the match result (0:0): ")

                dict = {'id': i, 'day': d, 'time': t, 'location': p, 'opponent': o, 'result': r}

                with open('eibar.csv', 'a+') as csv_file:
                    dict_object = csv.DictWriter(csv_file, fieldnames=fnames)

                    dict_object.writerow(dict)

                a = input("Do you want to enter another match? (y/n): ")

                if a == 'n':
                    a = 0

                elif a == 'y':
                    a = 1

                else:
                    print("You have to enter 'y' or 'n'")
                    a = 1
            f.close()

    elif option == "2":
        with open('eibar.csv', "r") as csv_file:
            reader = csv.reader(csv_file)

            for item in reader:
                print(item)

    elif option == "3":
        print("Goodbye")
        a = a - 1

    else:
        print("Invalid option. Please enter a number between 1 and 3.")
