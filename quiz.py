

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
}

for question, options in QUESTIONS.items():
    correct_answer = options[0]
    sorted_options = sorted(options)
    for label, option in enumerate(sorted_options):
        print(f"  {label}) {option}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_options[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
