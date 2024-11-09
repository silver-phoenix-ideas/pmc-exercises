filenames = ["doc.txt", "report.txt", "presentation.txt"]
contents = [
    "All carrots are to be sliced longitudinally.",
    "The carrots were reportedly sliced.",
    "The slicing process was well presented."
]

for filename, content in zip(filenames, contents):
    file = open(f"files/{filename}", "w")
    file.write(content)
    file.close()
