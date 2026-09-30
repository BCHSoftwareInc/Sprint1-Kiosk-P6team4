secret = 64
guess = int(input("Guess the secret number: "))
while guess != secret:
    if guess > secret:
        print("You're too high!")
    else:
        print("You're too low!")
    guess = int(input("Guess the secret number: "))
