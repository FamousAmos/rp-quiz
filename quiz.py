import random
from string import ascii_lowercase

NUM_QUESTIONS_ON_QUIZ = 5
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm?": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What does dict.get(key) return if the key isn't found in the dictionary?": [
        "None", "key", "True", "False"
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ]
}


def prepare_questions(questions, num_questions):
    num_questions = min(NUM_QUESTIONS_ON_QUIZ, len(QUESTIONS))
    return random.sample(list(QUESTIONS.items()), k=num_questions)


def get_answer(question, options):
    print(f"{question}? ")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, option in labeled_options.items():
        print(f"  {label}) {option}")

    while (answer_label := input("\nChoice? ")) not in labeled_options:
        print(f"Please enter one of {', '.join(labeled_options)}")
    return labeled_options[answer_label]


def ask_question(question, options):
    correct_answer = options[0]
    ordered_options = random.sample(options, k=len(options))

    answer = get_answer(question, ordered_options)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_ON_QUIZ
    )

    num_correct = 0
    for num, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, options)

    print(f"\nYou got {num_correct} correct out of {num} questions")


if __name__ == "__main__":
    run_quiz()
