# 🎯 Quiz Game (Python Console Application)

A simple, professional terminal-based **Multiple-Choice Quiz Game** built in
Python, designed as a college / internship submission project. The game
asks the player 10 general-knowledge and basic-programming questions, each
with four options (A, B, C, D), validates all inputs, gives instant
feedback, and finally reports a score, percentage, and PASS/FAIL status.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [How to Play](#-how-to-play)
- [Sample Output](#-sample-output)
- [Project Report](#-project-report)
- [Screenshots](#-screenshots)
- [GitHub Upload Instructions](#-github-upload-instructions)
- [Author](#-author)

---

## ✨ Features

- ✅ Asks for the player's name and shows a personalized welcome message
- ✅ 10 multiple-choice questions, each with 4 options (A/B/C/D)
- ✅ Strict input validation — only A, B, C, or D (case-insensitive) accepted
- ✅ Instant feedback after every question (Correct / Incorrect)
- ✅ Displays the correct answer whenever the player answers incorrectly
- ✅ Automatic score and percentage calculation
- ✅ PASS/FAIL result (pass mark: 50%)
- ✅ "Play again?" option to replay the quiz without restarting the program
- ✅ Clean, modular code using functions (PEP 8 compliant)
- ✅ Uses **only** the Python Standard Library — no installation of extra
  packages required

---

## 📁 Project Structure

```
Quiz_Game/
│
├── quiz_game.py          # Main program - game logic & flow control
├── questions.py          # Question bank (questions, options, answers)
├── README.md             # Project documentation (this file)
├── requirements.txt      # Dependency list (standard library only)
│
├── report/
│   └── Project_Report.docx   # Full internship/college project report
│
├── screenshots/           # Screenshots of the running application
│
└── output_samples/        # Saved sample terminal outputs (.txt)
    ├── sample_output_pass.txt
    └── sample_output_fail.txt
```

---

## 🛠 Requirements

- Python 3.6 or higher
- No external/third-party libraries needed (see `requirements.txt`)

---

## ⚙️ Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/<your-username>/Quiz_Game.git
   cd Quiz_Game
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (none required, listed for completeness):
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

From inside the `Quiz_Game` folder, run:

```bash
python3 quiz_game.py
```

On Windows, you can also use:

```bash
python quiz_game.py
```

---

## 🎮 How to Play

1. Enter your name when prompted.
2. Read each question carefully along with its four options.
3. Type **A**, **B**, **C**, or **D** and press Enter to answer.
4. If you type anything else, the game will ask you to re-enter a valid
   option.
5. After each answer, the game tells you if you were **Correct** or
   **Incorrect** (showing the right answer if you got it wrong).
6. After all 10 questions, your **score**, **percentage**, and
   **PASS/FAIL** status will be displayed.
7. You will then be asked if you want to **play again (Y/N)**.

---

## 🖥 Sample Output

A full sample transcript of a passing and a failing run is available in
the `output_samples/` folder:

- `output_samples/sample_output_pass.txt`
- `output_samples/sample_output_fail.txt`

Example snippet:

```
Q1. Who is known as the father of computers?
   A) Charles Babbage
   B) Alan Turing
   C) Isaac Newton
   D) Albert Einstein
Your answer (A/B/C/D): A
Correct!

...

==================================================
  RESULT FOR RAVI KUMAR
==================================================
  Score      : 10 / 10
  Percentage : 100.0%
  Status     : PASS
==================================================
```

---

## 📄 Project Report

A complete formal project report is provided at
`report/Project_Report.docx`, covering:

Title Page, Certificate, Acknowledgement, Abstract, Introduction,
Objectives, Scope, Technologies Used, System Requirements, Software
Design, Flowchart, Algorithm, Code Explanation, Testing, Sample Outputs,
Advantages, Limitations, Future Scope, Conclusion, and References.

---

## 📸 Screenshots

Please add screenshots of the running program to the `screenshots/`
folder. Suggested screenshots to capture (see report for the full list):

1. Program start / welcome message
2. A question being displayed
3. An invalid input being rejected
4. A "Correct!" response
5. An "Incorrect!" response showing the right answer
6. Final result screen with PASS status
7. Final result screen with FAIL status
8. "Play again?" prompt

---

## 🌐 GitHub Upload Instructions

1. Create a new repository on GitHub named `Quiz_Game` (do **not**
   initialize with a README, since one is already included).
2. On your local machine, navigate to the project folder:
   ```bash
   cd Quiz_Game
   ```
3. Initialize git and make your first commit:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Quiz Game console project"
   ```
4. Link your local repository to GitHub and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/Quiz_Game.git
   git push -u origin main
   ```
5. Refresh your GitHub repository page to confirm all files uploaded
   successfully.

---

## 👤 Author

**Student / Intern Name:** _[Your Name Here]_
**Course / Internship:** Python Programming Internship / College Mini
Project
**Submitted To:** _[Institution / Organization Name]_
**Date:** _[Submission Date]_

---

## 📜 License

This project is created for educational purposes as part of a college /
internship submission. Feel free to use and modify it for learning.
