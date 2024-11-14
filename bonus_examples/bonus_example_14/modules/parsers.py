def parse(user_input):
    data = user_input.split(" ")
    feet = float(data[0])
    inches = float(data[1])
    return feet, inches
