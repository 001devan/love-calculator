#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator")

in_letters=int(input("How many letters would you like in your password: \n"))
in_symbols=int(input(f"How many symbols would you like: \n"))
in_numbers=int(input(f"How many numbers would you like: \n"))

password_list=[]
for p in range(0,in_letters):
  password_list+=random.choice(letters)
for p in range(0,in_symbols):
  password_list+=random.choice(symbols)
for p in range(0,in_numbers):
  password_list+=random.choice(numbers)

random.shuffle(password_list)
password=''
for n in password_list:
  password+=n

print(f"Your password is {password}")
