from BirthdayCalendar import birthday
from eibarStatistics import eibar

aukera = 1
while aukera != 4:
    print("GAMES")
    print("---------------------------------")
    print("1.- Manage my birthday agenda")
    print("2.- See the Statistics for SD Eibar")
    print("3.- Hangman")
    print("4.- exit.")
    print()
    aukera = int(input("What do you want to do today? "))
    match aukera:
        case 1:
            birthday()
        case 2:
            eibar()
        case 3:

        case other:
            print("that option does not exist.")