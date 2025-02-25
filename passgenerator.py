import random
import string


def pass_generator(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,./<>?"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

print(pass_generator(12))



