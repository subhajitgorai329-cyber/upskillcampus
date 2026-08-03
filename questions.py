"""
questions.py
------------
This module stores the question bank for the Quiz Game.

Each question is represented as a dictionary with the following keys:
    "question" : str  -> the question text
    "options"  : dict -> mapping of option letters (A, B, C, D) to option text
    "answer"   : str  -> the correct option letter ("A", "B", "C", or "D")

Keeping the questions in a separate module makes the project modular and
allows the question bank to be updated without touching the main game logic.
"""

# List of 10 multiple-choice questions (general knowledge / basic Python mix)
QUESTIONS = [
    {
        "question": "Who is known as the father of computers?",
        "options": {
            "A": "Charles Babbage",
            "B": "Alan Turing",
            "C": "Isaac Newton",
            "D": "Albert Einstein",
        },
        "answer": "A",
    },
    {
        "question": "Which of the following is NOT a programming language?",
        "options": {
            "A": "Python",
            "B": "Java",
            "C": "HTML",
            "D": "C++",
        },
        "answer": "C",
    },
    {
        "question": "What is the file extension used for Python files?",
        "options": {
            "A": ".pyt",
            "B": ".py",
            "C": ".pt",
            "D": ".pyth",
        },
        "answer": "B",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "func",
            "D": "define",
        },
        "answer": "B",
    },
    {
        "question": "What is the capital city of India?",
        "options": {
            "A": "Mumbai",
            "B": "Kolkata",
            "C": "New Delhi",
            "D": "Chennai",
        },
        "answer": "C",
    },
    {
        "question": "Which data type is used to store True/False values in Python?",
        "options": {
            "A": "int",
            "B": "str",
            "C": "bool",
            "D": "float",
        },
        "answer": "C",
    },
    {
        "question": "Which company developed the Python programming language?",
        "options": {
            "A": "Microsoft",
            "B": "Python Software Foundation",
            "C": "Google",
            "D": "Apple",
        },
        "answer": "B",
    },
    {
        "question": "What does CPU stand for?",
        "options": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Utility",
            "D": "Central Processor Utility",
        },
        "answer": "A",
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "<!-- -->",
            "C": "#",
            "D": "**",
        },
        "answer": "C",
    },
    {
        "question": "Which of these is used to store multiple items in a single variable "
        "in Python?",
        "options": {
            "A": "List",
            "B": "Character",
            "C": "Integer",
            "D": "Boolean",
        },
        "answer": "A",
    },
]
