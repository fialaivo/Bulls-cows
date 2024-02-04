import time
import random
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ivo Fiala
email: fiala.ivo@spszr.cz
discord:  ivofiala
"""

def duration (start_time, stop_time):
    return round((stop_time-start_time),1)

def create_random_number():
  random_number = ""
  digits = [str(i) for i in range(1, 10)]
  for cycle_number in range(1,5):
    random_digit = random.choice(digits)
    random_number += random_digit
    digits.remove(random_digit)
  if cycle_number == 1:
    digits.append("0")
  return(random_number)

def check_duplication(user_number):
  duplication = False
  for cycle_number in range(0,3):
    if user_number[cycle_number] in user_number[cycle_number+1]:
      duplication = True
      break
  return duplication

def chcek_user_number(user_number):
  error=""
  if not user_number.isdigit():
    error="Your input insn't number, please inser number again"
  if len(user_number) < 4:
    error="Your number is too short, plese insert number again:"
  if len(user_number) > 4:
    error="Your number is too long, plese insert number again:"
  if user_number[0] == "0":
    error="The number must not start with zero, plese insert number again:"
  return error

def check_bulls_cows(user_number, random_number):
  bulls = 0
  cows = 0
  for cycle_number in range(0,4):
    if user_number[cycle_number] == random_number[cycle_number]:
      bulls += 1
      continue
    if user_number[cycle_number] in random_number:
      cows +=1  
  print(f"{bulls} bulls, {cows} cows")

start_time = time.time()
line = "-" * 40
user_number = 0
random_number = create_random_number()
print(random_number)
print("Hi there!")
print(line)
print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
print(line)
print("Enter a number:")
print(line)
while (user_number:= input(">>>")) != random_number:
  error_string = chcek_user_number(user_number)
  if (error_string != ""):
    print(error_string)
    print(line)
    continue
  duplication = check_duplication(user_number)
  if duplication == True:
    print("The number contains duplication, plese insert number again:")
    continue
  check_bulls_cows(user_number, random_number)
  print(line)
print("Correct, you've guessed the right number")
stop_time = time.time()
print(f"You guessed the secret number in {duration(start_time, stop_time)} seconds.")
