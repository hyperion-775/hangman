from time import sleep
from words import random_word

hungperson = {
0: """
   ______
   |    |
   O    |
  /|\   |
 _/ \_  |
        |
 """,
 1: """
   ______
   |    |
   O    |
  /|\   |
 _/ \   |
        |
 """,
 2: """
   ______
   |    |
   O    |
  /|\   |
  / \   |
        |
 """,
 3: """
   ______
   |    |
   O    |
  /|\   |
 _/ \_  |
        |
 """,
 4: """
   ______
   |    |
   O    |
  /|\   |
  /     |
        |
 """,
 5: """
   ______
   |    |
   O    |
  /|\   |
        |
        |
 """,
 6: """
   ______
   |    |
   O    |
  /|    |
        |
        |
 """,
 7: """
   ______
   |    |
   O    |
   |    |
        |
        |
 """,
 8: """
   ______
   |    |
   O    |
        |
        |
        |
 """,
 9: """
   ______
   |    |
        |
        |
        |
        |
 """,
 10: """
   O
  /|\ 
 _/ \_
 """
}

#name = input("What's your name? ")

#print("Hello, " + name + "! Time to play hangperson!")

print()

sleep(1)

print("Start guessing...")

sleep(.5)

# word = "secret"
word = random_word(5, 12)

guesses = ""

lives = 9

while lives > 0:
    clue = ""
    print(hungperson[lives])
    # word is "secret"
    for letter in word:
        if letter in guesses:
            clue = clue + letter + " "
        else:
            clue = clue + "_ "

    if "_" not in clue:
        break

    print(clue, guesses)

    guess = input("Your guess? ")

    guess = guess[:1]

    if guess not in guesses:
        if guess not in word:
            lives -= 1

        guesses += guess
    else:
        print("You already guessed " + guess + ", moron.")

if lives == 0:
    print(hungperson[lives])
    print("LOOOOOOOSER!")
else:
    print(hungperson[10])
    print("You won!")
