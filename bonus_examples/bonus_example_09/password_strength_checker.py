password = input("Enter password: ")

result = {
    "length": len(password) >= 8,
    "digit": any([char.isdigit() for char in password]),
    "uppercase": any([char.isupper() for char in password])
}

print("Strong password." if all(result.values()) else "Weak password.")
