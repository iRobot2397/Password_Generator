import random
import string
print("Welcome to the Random Password Generator!!")
number = int(input("How many letters would you like?: "))
def password(number):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(number))
    print("You can do:", result_str)
print("Here are some suggestions:")
password(number)
password(number)
password(number)
password(number)
def if_or_else():
  happy = input("Are you satisfied with your choices?(yes/no): ".lower())
  if happy == "yes":
    print("Thank you! I hope that you will use the Random Password Generator again!")
  elif happy == "Yes":
     print("Thank you! I hope that you will use the Random Password Generator again!")

  
  else:
    print("Here are some more suggestions:")
    password(number)
    password(number)
    password(number)
    password(number)
    if_or_else()
if_or_else()

