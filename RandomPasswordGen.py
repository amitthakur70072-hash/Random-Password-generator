import random
import string

def password_generator(length):
    character=string.ascii_letters+string.digits
    password=""

    for i in range(length):
        password+=random.choice(character)
    return password
print(password_generator(8))