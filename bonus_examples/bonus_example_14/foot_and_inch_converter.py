from modules.parsers import parse
from modules.converters import convert

user_input = input("Enter feet and inches: ")
feet, inches = parse(user_input)
meters = convert(feet, inches)

if meters < 1:
    print("Kid is too short.")
else:
    print("Kid can ride the attraction.")
