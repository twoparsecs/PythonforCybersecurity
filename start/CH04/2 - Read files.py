# Write a script that reads "hackme.txt"
# Print "Here is someone to hack - information"
# Then print the various information found in the file.
# Explicitly code the closing of the hackme.txt file
# Created by Justin Gardner on 7/8/2024

hack = open("hackme.txt", "r")

info = hack.read()
print("Here is someone to hack: ")
print(info)

hack.close()