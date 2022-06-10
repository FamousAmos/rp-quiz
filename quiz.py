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


def get_answers(question, options, num_choices=1, hint=None):
    print(f"{question}? ")
    labeled_options = dict(zip(ascii_lowercase, options))
    if hint:
        labeled_options["?"] = "Hint"

    for label, option in labeled_options.items():
        print(f"  {label}) {option}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by a comma"
            print(f"Please answer {num_choices} option{plural_s}")
            continue

        if any(
            (invalid := answer) not in labeled_options
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_options)}"
            )
            continue

        return [labeled_options[answer] for answer in answers]


def ask_question(question):
    correct_answers = question["answers"]
    options = question["answers"] + question["options"]
    ordered_options = random.sample(options, k=len(options))

    answers = get_answers(
        question=question["question"],
        options=ordered_options,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        is_or_are = "is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))

    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    return 1 if correct else 0


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
