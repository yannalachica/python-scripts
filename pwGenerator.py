import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"
char = letters + numbers + symbols

def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(char)
    return password

length = int(input("Choose length of password:"))
print("Your password is: " + generate_password(length))
