user_input = input("Enter a new member: ")

file = open("members.txt", "a")
file.write(user_input + "\n")
file.close()
