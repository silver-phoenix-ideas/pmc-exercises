def parse(user_input):
    data = user_input.split(" ")
    feet = float(data[0])
    inches = float(data[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


user_input = input("Enter feet and inches: ")
feet, inches = parse(user_input)
meters = convert(feet, inches)

if meters < 1:
    print("Kid is too short.")
else:
    print("Kid can ride the attraction.")
