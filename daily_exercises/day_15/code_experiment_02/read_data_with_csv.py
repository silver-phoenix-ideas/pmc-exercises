import csv

with open("weather.csv") as file:
    content = list(csv.reader(file))

data = {item[0].lower(): item[1] for item in content[1:]}

user_input = input("Enter city: ").lower()
print("Temperature: " + data[user_input])
