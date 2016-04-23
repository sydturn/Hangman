from __future__ import print_function
import random

word_list = []
file = open('word_list.txt', 'r')

for line in file:
    line = line.rstrip()
    word_list.append(line)


while True:
    guesses_left = 6
    play_again = ""
    correct_guessed = []
    wrong_guessed = []
    word = random.choice(word_list)

    print ("There are", len(word), "letters in the word.")
    print (word)
    while guesses_left > 0 and len(correct_guessed) != len(word):
        for letter in word:
            if letter in correct_guessed:
                print (letter, end=" ")
            else:
                print ("_", end=" ")
        print ()

        guess_letter = str(raw_input("Guess a letter: "))
        if len(guess_letter) != 1:
            print ("Invalid input, please try again.")
        elif guess_letter in correct_guessed or guess_letter in wrong_guessed:
            print ("You already guessed that, try again.")
        elif guess_letter in word:
            occurance = word.count(guess_letter)
            correct_guessed += occurance * [guess_letter]
            left_over = len(word) - len(correct_guessed)
            print ("There are", occurance, "'" + guess_letter + "'(s). There are", left_over, "letters left in the word.")

        else:
            guesses_left -= 1
            wrong_guessed.append(guess_letter)
            print ("There are no", "'" + guess_letter + "'s. You have", guesses_left, "more guesses.")
            print (wrong_guessed)

    if len(word) == len(correct_guessed):
        print ("Congratulations! You win!")
    else:
        print ("You lose. The word was:", word)

    play_again = str(raw_input("Play again? Y or N").lower())
    if play_again != "y":
        print ("End Game")
        break