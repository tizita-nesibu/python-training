import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Method 1: Easy Version:
easy_password = ""
#print("Your password is: ", end="")
for letter in range(0, nr_letters):
    easy_password += random.choice(letters)
    #print(random.choice(letters), end="")
for symbol in range(0, nr_symbols):
    easy_password += random.choice(symbols)
    #print(random.choice(symbols), end="")
for number in range(0, nr_numbers):
    easy_password += random.choice(numbers)
    #print(random.choice(numbers), end="")
print(f"Option 1: Your Easy Version password is:\n {easy_password}")

#Method 2: Easy Version and Hard Version:
password_lst = []
for letter in range(0, nr_letters):
    password_lst.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    password_lst.append(random.choice(symbols))
for symbol in range(0, nr_numbers):
    password_lst.append(random.choice(numbers))

print("Option 2: Your Easy and Hard Version (shuffled) password is:")
print(password_lst) #Easy Version
random.shuffle(password_lst) #Hard Version
print(password_lst)

#To print the password without brackets and commas
password = ""
for char in password_lst:
    password += char
print(f"Your password is: {password}")
