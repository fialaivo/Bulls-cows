import time
import random
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ivo Fiala
email: fiala.ivo@spszr.cz
discord:  ivofiala
"""
start_time = time.time()
line = "-" * 40
user_number = 0
random_number = ""
digits = ["1","2","3","4","5","6","7","8","9"]
for cycle_number in range(1,5):
  random_digit = random.choice(digits)
  random_number += random_digit
  digits.remove(random_digit)
  if cycle_number == 1:
    digits.append("0")
"""print(random_number)"""
print("Hi there!")
print(line)
print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
print(line)
print("Enter a number:")
print(line)
while (user_number:= input(">>>")) != random_number:
  if not user_number.isdigit():
    print("Your input insn't number, please inser number again")
    print(line)
    continue
  if len(user_number) < 4:
    print("Your number is too short, plese insert number again:")
    print(line)
    continue
  if len(user_number) > 4:
    print("Your number is too long, plese insert number again:")
    print(line)
    continue
  if user_number[0] == "0":
    print("The number must not start with zero, plese insert number again:")
    print(line)
    continue
  digits = ["1","2","3","4","5","6","7","8","9"]
  duplication = False
  for cycle_number in range(0,3):
    if user_number[cycle_number] in user_number[cycle_number+1]:
      duplication = True
      break
  if duplication == True:
    print("The number contains duplication, plese insert number again:")
    continue
  bulls = 0
  cows = 0
  for cycle_number in range(0,4):
    if user_number[cycle_number] == random_number[cycle_number]:
      bulls += 1
      continue
    if user_number[cycle_number] in random_number:
      cows +=1  
  print(f"{bulls} bulls, {cows} cows")
  print(line)
print("Correct, you've guessed the right number")
end_time = time.time()
duration = end_time - start_time

print(f"You guessed the secret number in {round(duration,1)} seconds.")
