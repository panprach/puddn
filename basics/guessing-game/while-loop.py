guesses = 5
while guesses != 0:
    guess = input("Guess a number between 1 to 10: ")
    try:
        num = int(guess)
    except:
        print("Not a number!")
        continue

    if num > 10 or num < 1:
        print("Not a number between 1 to 10")
        continue

    elif num == 9:
        print("Congratulations! you got it!")
        break

    elif num <= 10 and num >= 1:
        guesses -= 1
        if guesses != 0:
            print("Incorrect. " + str(guesses) + " guesses left")
            continue
        else:
            print("Too bad! You used all your guesses up")
