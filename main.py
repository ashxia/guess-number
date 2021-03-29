#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from logo import logo
import random
print(logo)
#create a function to generate a secret number between 1 ans 100

def secret_number():
  number = random.randint(1, 100)
  return number

def compare(hidden_number, number_of_lives):
  
  while number_of_lives >0:
    guess = int(input("please guess a number between 1 and 100"))
    if guess > hidden_number:
      number_of_lives -=1
      print(f"Too high\n You have {number_of_lives} atemtps remaining to guess please try again")
    elif guess < hidden_number:
      number_of_lives -=1
      print(f"Too low\n you have {number_of_lives} atemtps remaining to guess please try again")
    elif guess == hidden_number:
      return ("you win")
      
  return "you lost!!"


def game():
  print("welcome to the number guessing game")
  print("im thinking of a number between 1 and 100")


  number_of_lives = 0
  EASY = 10
  HARD = 5
  while number_of_lives ==0:
    difficulty = input("choose a difficulty type, 'easy' or 'hard'")
    if difficulty == "easy":
      number_of_lives = EASY
    elif difficulty == "hard":
      number_of_lives = HARD
    else:
      print("wrong entry please try again")

  hidden_number = secret_number()

  print(hidden_number)
  print(compare(hidden_number, number_of_lives))

game()
