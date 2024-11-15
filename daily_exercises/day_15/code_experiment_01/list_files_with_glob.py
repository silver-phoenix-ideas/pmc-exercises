import glob

filepaths = glob.glob("files/*.txt")

for filepath in filepaths:
    print()
    print("Filepath: " + filepath)

    with open(filepath) as file:
        content = file.readlines()

    for line in content:
        print("-", line, end="")

    print()
