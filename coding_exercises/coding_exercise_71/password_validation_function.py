def strength(password):
    result = {
        "length": len(password) > 7,
        "uppercase": any([char.isupper() for char in password]),
        "digit": any([char.isdigit() for char in password])
    }

    return "Strong Password" if all(result.values()) else "Weak Password"
