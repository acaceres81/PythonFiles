import random
import time

def hangmanGame(name):
    # The start:
    print("\nHello. This is the hangman game")
    print("\nHello " + name + "! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")
    time.sleep(3)


    # A loop to re-execute the game when the game ends:

    def play_loop():
        play_game = input("Do You want to play again? y = yes, n = no \n")
        while play_game not in ["y", "n","Y","N"]:
            play_game = input("Do You want to play again? y = yes, n = no \n")
        if play_game == "y":
            hangman()
        elif play_game == "n":
            print("Bye!")
            exit()


    # Initializing all the conditions required for the game:
    def hangman():
        words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                       ,"plants"]
        word = random.choice(words_to_guess)
        length = len(word)
        count = 0
        display = '_' * length
        already_guessed = []
        limit = 5

        while count != limit or word == '_' * length:

            guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
            guess = guess.strip()
            if len(guess) == 0 or len(guess) >= 2 or guess <= "9":
                print("Invalid Input, Try a letter\n")

            elif guess in word:
                already_guessed.extend([guess])
                index = word.find(guess)
                word = word[:index] + "_" + word[index + 1:]
                display = display[:index] + guess + display[index + 1:]
                print(display + "\n")

            elif guess in already_guessed:
                print("Try another letter\n")

            else:
                count += 1

                if count == 1:
                    time.sleep(1)
                    print("   _____ \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

                elif count == 2:
                    time.sleep(1)
                    print("   _____ \n"
                        "  |     | \n"
                        "  |     |\n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

                elif count == 3:
                    time.sleep(1)
                    print("   _____ \n"
                            "  |     | \n"
                            "  |     |\n"
                            "  |     | \n"
                            "  |      \n"
                            "  |      \n"
                            "  |      \n"
                            "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

                elif count == 4:
                    time.sleep(1)
                    print("   _____ \n"
                        "  |     | \n"
                        "  |     |\n"
                        "  |     | \n"
                        "  |     O \n"
                        "  |      \n"
                        "  |      \n"
                        "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

                elif count == 5:
                    time.sleep(1)
                    print("   _____ \n"
                        "  |     | \n"
                        "  |     |\n"
                        "  |     | \n"
                        "  |     O \n"
                        "  |    /|\ \n"
                        "  |    / \ \n"
                        "__|__\n")
                    print("Wrong guess. You are hanged!!!\n")
                    print("The word was:",already_guessed,word)
                    print("")


            if word == '_' * length:
                print("Congrats! You have guessed the word correctly!")

    #Execute hangman function
    hangman()