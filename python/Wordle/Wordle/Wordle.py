print("==============================================================")
print(" Welcome to Wordle! ")
print("Guess the 5-letter word in 6 tries or less. After each guess, you'll receive feedback:")
print("Feedback: [G] - Correct/Green, [Y] - Present/Yellow, [_] - Absent/Grey\n")
print("==============================================================\n")
secret_word = "Mewge"
max_attempts = 6
for i in range(5):
    secret_char = secret_word[i]

guess = input("Attempt " + str(max_attempts) + " " + " - Enter: ")
