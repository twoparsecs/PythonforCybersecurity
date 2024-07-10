# Create a script that asks the user:
# What is your name?
# What is your favorite color?
# What was your first pet's name?
# What is your mother's maiden name?
# What elementary school did you attend?
# Output the collected information to "hackme.txt"
# Created by Justin Gardner on 7/8/2024

name = input("What is your name? ")
fav_color = input("What is your favorite color? ")
first_pet = input("What was your first pet's name? ")
mother_maiden = input("What is your mother's maiden name? ")
elementary_school = input("What elementary school did you attend? ")

with open('hackme.txt', 'w') as file:
    file.write(name + '\n' + fav_color + '\n' + first_pet + '\n' + mother_maiden + '\n' + elementary_school + '\n')

print(f"User input has been written to 'hackme.txt'.")