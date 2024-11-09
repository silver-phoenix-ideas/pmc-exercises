waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, name in enumerate(waiting_list, start=1):
    print(f"{index}.{name.capitalize()}")
