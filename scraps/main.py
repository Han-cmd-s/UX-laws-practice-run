# === imports ===
import random
import os
import glob
import importlib.util
import sys

# from utils.score_tracker import update_score, display_score



# === core functions ===

# === load_questions() ===
# - load, and shuffle the question list.
def find_banks():
    """Discover available question bank files in the scraps folder.

    Returns a dict mapping bank id (str) -> absolute file path.
    """
    folder = os.path.dirname(__file__)
    pattern = os.path.join(folder, "question_tabel-*.py")
    banks = {}
    for path in glob.glob(pattern):
        name = os.path.basename(path)
        # expect files like question_tabel-104.py
        if name.startswith("question_tabel-") and name.endswith('.py'):
            bank_id = name.replace('question_tabel-', '')[:-3]
            banks[bank_id] = path
    return banks


def load_bank(bank_id):
    """Dynamically import a question bank by its id (string).

    Returns the module object or raises FileNotFoundError/ImportError.
    """
    banks = find_banks()
    if bank_id not in banks:
        raise FileNotFoundError(f"Question bank {bank_id} not found")
    path = banks[bank_id]
    mod_name = f"question_tabel_{bank_id}"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_questions(shuffle=True, bank_id='104'):
    """Load questions from the selected bank (default 104).
    """
    try:
        bank = load_bank(str(bank_id))
        question_list = list(getattr(bank, 'questions', []))
    except Exception as e:
        print(f"Warning: failed to load bank {bank_id}: {e}. Falling back to empty list.")
        question_list = []

    if shuffle:
        random.shuffle(question_list)
    return question_list


# === ask_questions() ===
# - display a question, take user input, check answer and return result.
def ask_question(question):
    print("\n" + question["question"])

    # Print multiple-choice options if present (support both 'Options' and 'options')
    opts = None
    if "options" in question:
        opts = question["options"]
    elif "Options" in question:
        opts = question["Options"]

    if opts:
        # Enumerate as A, B, C ...
        for idx, opt in enumerate(opts):
            label = chr(ord('A') + idx)
            print(f"  {label}. {opt}")

    user_answer = input("Your answer: ").strip()

    # Allow answers as full text or as a letter/number corresponding to the option
    selected = user_answer
    if opts and len(user_answer) == 1 and user_answer.isalpha():
        idx = ord(user_answer.upper()) - ord('A')
        if 0 <= idx < len(opts):
            selected = opts[idx]
    elif opts and user_answer.isdigit():
        idx = int(user_answer) - 1
        if 0 <= idx < len(opts):
            selected = opts[idx]

    # Compare normalized answers
    try:
        correct = question['answer']
    except KeyError:
        correct = question.get('Answer') if 'Answer' in question else ''

    if selected.strip().lower() == str(correct).strip().lower():
        print("Correct!")
        # Support both 'explanation' and 'Explanation' keys
        if "explanation" in question:
            print(question['explanation'])
        elif "Explanation" in question:
            print(question['Explanation'])
        return True
    else:
        print(f"Incorrect. The correct answer is: {correct}")
        if "explanation" in question:
            print(question['explanation'])
        elif "Explanation" in question:
            print(question['Explanation'])
        return False


# === run_quiz() ===
# - main quiz loop, run through all questions (and track score)
def run_quiz():
    print("Welcome to the Quiz!")
    score = 0
    # let the user pick a question bank
    banks = find_banks()
    if not banks:
        print("No question banks found. Exiting.")
        return

    print("Available banks:")
    for b in sorted(banks.keys()):
        default_tag = ' (default)' if b == '104' else ''
        print(f"  {b}{default_tag}")

    choice = input("Choose a bank id (press Enter for default 104): ").strip()
    if not choice:
        choice = '104'

    question_list = load_questions(shuffle=True, bank_id=choice)

    for i, question in enumerate(question_list, 1):
        print(f"\nQuestion {i} of {len(question_list)}:")
        if ask_question(question):
            score += 1

        print("\n Quiz Complete!")
        print(f"Your final score is: {score} out of {len(question_list)}")

# === main execution ===
# - entry point of the script.
def main():
    run_quiz()


# === Run Script ===
if __name__ == "__main__":
    main()