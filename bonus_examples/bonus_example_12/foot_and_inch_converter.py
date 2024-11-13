def convert(feet_inches):
    numbers = feet_inches.split(" ")
    feet = float(numbers[0])
    inches = float(numbers[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")
meters = convert(feet_inches)

if meters < 1:
    print("Kid is too short.")
else:
    print("Kid can ride the attraction.")
