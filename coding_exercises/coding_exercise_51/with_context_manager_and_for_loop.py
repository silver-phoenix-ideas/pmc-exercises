languages = ['English', 'German', 'Spanish']

for language in languages:
    with open(language + ".txt", "w") as file:
        file.write(language)
