import json

with open("questions.json") as file:
    data = json.load(file)

print("\n" + "Trivia Quiz" + "\n")

for question in data:
    print(question["text"])

    for index, choice in enumerate(question["choices"], start=1):
        print(f"{index}) {choice}")

    print()
    user_answer = input("Enter answer: ")
    question["user_answer"] = int(user_answer)
    print()

print("Results" + "\n")

score = 0

for index, question in enumerate(data, start=1):
    print(
        f"Question {index}: "
        f"Your answer - {question['user_answer']}, "
        f"Correct answer - {question['correct_answer']}"
    )

    if question["user_answer"] == question["correct_answer"]:
        score += 1

print("\n" + f"You got {score} out of {len(data)} correct.")
