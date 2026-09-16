#!/usr/bin/env python3

import random
import string

# set pw length
password_length = 20

# set pw requirements
num_caps    = 2
num_dig     = 2
num_special = 2
num_lower   = password_length - num_caps - num_dig - num_special

# get the required characters
digits  = random.choices(string.digits, k=num_dig)
caps    = random.choices(string.ascii_uppercase, k=num_caps)
special = random.choices(string.punctuation, k=num_special)

password = digits + caps + special

# print(len(password))

# finish the password, adding one character at a time
for i in range(password_length - len(password)):
    password.append(random.choice(string.ascii_lowercase))

# randomize our password (shuffle randomizes a list in place)
random.shuffle(password)

# join the list into a string and print the final password
print(''.join(password))

