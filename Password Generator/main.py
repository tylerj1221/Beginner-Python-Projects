import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
passwordLen = nr_letters + nr_symbols + nr_numbers
randNum = random.randint(0,2)

while passwordLen != 0:
    if  randNum == 0 and nr_letters != 0:
        password += letters[random.randint(0, len(letters) - 1)]
        nr_letters -= 1
        passwordLen -= 1
        randNum = random.randint(0, 2)
    elif randNum == 1 and nr_symbols != 0:
        password += symbols[random.randint(0, len(symbols) - 1)]
        nr_letters -= 1
        passwordLen -= 1
        randNum = random.randint(0, 2)
    else:
        password += numbers[random.randint(0, len(numbers)-1)]
        nr_numbers -= 1
        passwordLen -= 1
        randNum = random.randint(0, 2)

print(password)