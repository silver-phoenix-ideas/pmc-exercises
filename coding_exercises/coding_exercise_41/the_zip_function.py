countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for filename, country in zip(filenames, countries):
    file = open(filename, "w")
    file.write(country)
    file.close()
