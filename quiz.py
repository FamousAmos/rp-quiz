import random
from string import ascii_lowercase
import pathlib

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_ON_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"


def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions), k=num_questions)


def get_answer(question, options):
    print(f"{question}? ")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, option in labeled_options.items():
        print(f"  {label}) {option}")

    while (answer_label := input("\nChoice? ")) not in labeled_options:
        print(f"Please enter one of {', '.join(labeled_options)}")
    return labeled_options[answer_label]


def ask_question(question):
    correct_answer = question["answer"]
    options = [question["answer"]] + question["options"]
    ordered_options = random.sample(options, k=len(options))

    answer = get_answer(question["question"], ordered_options)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_ON_QUIZ
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")


if __name__ == "__main__":
    run_quiz()
