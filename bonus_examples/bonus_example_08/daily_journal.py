date = input("Enter today's date: ")
mood = input("How do you rate your mood on a scale from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    file.write(f"Date: {date}\n")
    file.write(f"Mood: {mood}\n")
    file.write(f"\n{thoughts}\n")
