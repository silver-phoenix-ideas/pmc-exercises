def get_average():
    with open("files/data.txt") as file:
        data = file.readlines()

    values = data[1:]
    values = [float(value) for value in values]
    average = sum(values) / len(values)

    return average


print(get_average())
