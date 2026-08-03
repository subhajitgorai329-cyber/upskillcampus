"""
quiz_game.py
------------
A terminal-based Multiple Choice Quiz Game.

Features:
    1. Asks the user for their name and displays a welcome message.
    2. Presents 10 multiple-choice questions (A, B, C, D options).
    3. Validates user input so only A, B, C, or D is accepted.
    4. Tells the user immediately whether each answer is correct.
    5. Shows the correct answer whenever the user answers incorrectly.
    6. Calculates the final score and percentage.
    7. Displays PASS/FAIL based on a 50% cut-off.
    8. Lets the user choose to play again.

Author : Student / Intern
Course : Python Programming Internship / College Project
"""

from questions import QUESTIONS

# Constant representing the passing percentage threshold
PASS_PERCENTAGE = 50

# The only valid option letters a user is allowed to type
VALID_OPTIONS = ("A", "B", "C", "D")


def display_welcome_message(name):
    """
    Display a friendly welcome banner using the player's name.

    Parameters
    ----------
    name : str
        The name entered by the player.
    """
    print("\n" + "=" * 50)
    print(f"  Welcome, {name}! Let's test your knowledge.")
    print("  You will be asked 10 multiple-choice questions.")
    print("  Answer each question by typing A, B, C, or D.")
    print("=" * 50 + "\n")


def get_player_name():
    """
    Prompt the user for their name and return a cleaned (stripped) version.
    Keeps asking until a non-empty name is provided.

    Returns
    -------
    str
        The validated player name.
    """
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def display_question(question_number, question_data):
    """
    Print a single question along with its four options.

    Parameters
    ----------
    question_number : int
        The 1-based index of the question (for display purposes).
    question_data : dict
        Dictionary containing "question" and "options" keys.
    """
    print(f"Q{question_number}. {question_data['question']}")
    for option_letter in VALID_OPTIONS:
        print(f"   {option_letter}) {question_data['options'][option_letter]}")


def get_validated_answer():
    """
    Repeatedly prompt the user until a valid option (A/B/C/D) is entered.
    Input is case-insensitive (e.g., "a" is accepted as "A").

    Returns
    -------
    str
        A validated, uppercase option letter.
    """
    while True:
        user_input = input("Your answer (A/B/C/D): ").strip().upper()
        if user_input in VALID_OPTIONS:
            return user_input
        print("Invalid input! Please enter only A, B, C, or D.\n")


def evaluate_answer(user_answer, question_data):
    """
    Compare the user's answer with the correct answer and print feedback.

    Parameters
    ----------
    user_answer : str
        The option letter chosen by the user.
    question_data : dict
        Dictionary containing the "answer" key with the correct option letter.

    Returns
    -------
    bool
        True if the answer was correct, False otherwise.
    """
    correct_answer = question_data["answer"]
    if user_answer == correct_answer:
        print("Correct!\n")
        return True

    correct_text = question_data["options"][correct_answer]
    print(f"Incorrect! The correct answer was {correct_answer}) {correct_text}\n")
    return False


def run_quiz():
    """
    Run through the full list of questions, collecting and evaluating
    the user's answers.

    Returns
    -------
    int
        The total number of questions answered correctly.
    """
    score = 0
    total_questions = len(QUESTIONS)

    for index, question_data in enumerate(QUESTIONS, start=1):
        display_question(index, question_data)
        user_answer = get_validated_answer()
        if evaluate_answer(user_answer, question_data):
            score += 1

    return score, total_questions


def calculate_percentage(score, total_questions):
    """
    Calculate the percentage of correctly answered questions.

    Parameters
    ----------
    score : int
        Number of correct answers.
    total_questions : int
        Total number of questions asked.

    Returns
    -------
    float
        Percentage score rounded to 2 decimal places.
    """
    return round((score / total_questions) * 100, 2)


def display_result(name, score, total_questions, percentage):
    """
    Display the final score, percentage, and PASS/FAIL status.

    Parameters
    ----------
    name : str
        The player's name.
    score : int
        Number of correct answers.
    total_questions : int
        Total number of questions.
    percentage : float
        Calculated percentage score.
    """
    print("=" * 50)
    print(f"  RESULT FOR {name.upper()}")
    print("=" * 50)
    print(f"  Score      : {score} / {total_questions}")
    print(f"  Percentage : {percentage}%")

    if percentage >= PASS_PERCENTAGE:
        print("  Status     : PASS")
    else:
        print("  Status     : FAIL")
    print("=" * 50 + "\n")


def ask_play_again():
    """
    Ask the user whether they want to play another round.
    Only accepts 'Y' or 'N' (case-insensitive).

    Returns
    -------
    bool
        True if the user wants to play again, False otherwise.
    """
    while True:
        choice = input("Do you want to play again? (Y/N): ").strip().upper()
        if choice in ("Y", "N"):
            return choice == "Y"
        print("Invalid input! Please enter Y or N.")


def main():
    """
    The main driver function that ties the whole game together.
    Supports replaying the quiz until the user chooses to stop.
    """
    print("#" * 50)
    print("#            PYTHON QUIZ GAME PROJECT           #")
    print("#" * 50)

    name = get_player_name()

    play_again = True
    while play_again:
        display_welcome_message(name)
        score, total_questions = run_quiz()
        percentage = calculate_percentage(score, total_questions)
        display_result(name, score, total_questions, percentage)
        play_again = ask_play_again()

    print(f"\nThank you for playing, {name}! Goodbye.")


# Standard Python entry-point guard so the game only runs when this file
# is executed directly (not when imported as a module).
if __name__ == "__main__":
    main()
