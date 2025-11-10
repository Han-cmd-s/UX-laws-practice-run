# === imports ===
import random

from question_table import questions
# from utils.score_tracker import update_score, display_score



# === core functions ===

# === load_questions() ===
# - load, and shuffle the question list.
def load_questions(shuffle=True):
    question_list = questions.copy()
    if shuffle:
        random.shuffle(question_list)
    return question_list


# === ask_questions() ===
# - display a question, take user input, check answer and return result.
def ask_question(question): 
    print("\n" + question["question"])
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == question['answer'].lower():
        print("Correct!")
        if "explanation" in question:
            print(question['explanation'])
        return True
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")
        if "explanation" in question:
            print(question['explanation'])
        return False


# === run_quiz() ===
# - main quiz loop, run through all questions (and track score)
def run_quiz():
    print("Welcome to the Quiz!")
    score = 0
    question_list = load_questions()

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