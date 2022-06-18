guesses = 5
correct = False
while guesses != 0 and correct == False:
    guess = input("Guess a number between 1 to 10: ")
    try:
        num = int(guess)
    except:
        print("Not a number!")
        continue

    if num > 10 or num < 1:
        print("Not a number between 1 to 10")
        continue

    for i in range(guesses):
        guesses -= 1
        if num == 9:
            correct = True
            print("Congratulations! you got it!")
            break

        if num <= 10 and num >= 1:
            if guesses != 0:
                print("Incorrect. " + str(guesses) + " guesses left")
                break
            if guesses == 0:
                print("Too bad! You used all your guesses up")
                break
