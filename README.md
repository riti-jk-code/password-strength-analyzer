# 🔐 Password Strength Analyzer

A Python-based password analysis tool that evaluates password strength using **Regular Expressions (Regex)** and rule-based checks. It identifies common password patterns and provides suggestions to help users create stronger passwords.

## ✨ Features

- **Length Validation** — Checks whether the password meets the minimum length requirement.
- **Character Validation** — Detects uppercase letters, lowercase letters, digits, and special characters.
- **Common Password Detection** — Identifies passwords that appear in a predefined list of commonly used passwords.
- **Repeated Character Detection** — Flags predictable patterns such as `aaaa` or `1111`.
- **Sequential Pattern Detection** — Detects selected sequences such as `abcd` and `1234`.
- **Strength Classification** — Classifies passwords as Weak, Moderate, or Strong based on predefined rules.
- **Improvement Suggestions** — Provides feedback based on the checks that fail.

## 🛠️ Tech Stack

- **Language:** Python
- **Core Concept:** Regular Expressions (`re` module)
- **Other Concepts:** Functions, Conditional Statements, String Handling

## ⚙️ How It Works

1. The user enters a sample password.
2. The program checks its length and character composition.
3. Regex-based checks identify selected repeated and sequential patterns.
4. The program checks whether the password matches a predefined common-password list.
5. A score, strength classification, warnings, and suggestions are displayed.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed
- A terminal or code editor such as Visual Studio Code

### Installation

Clone the repository:

```bash
git clone https://github.com/riti-jk-code/password-strength-analyzer.git
```

Navigate to the project directory:

```bash
cd password-strength-analyzer
```

Run the analyzer:

```bash
python regex.py
```

## 💻 Example

```text
Enter your password: abcd1234

Score: 3 /5
Strength: Weak
Warning: Sequential pattern detected!

Suggestions:
- Add an uppercase letter.
- Add a special character.
- Avoid predictable sequences like abcd or 1234.
```

## 📚 What I Learned

Through this project, I practiced:

- Writing reusable Python functions
- Using Regex with Python's `re` module
- Applying conditional logic to analyze input
- Detecting common and predictable password patterns
- Generating user-friendly feedback
- Using Git and GitHub for version control and project documentation

## 🔮 Future Improvements

- Expand the common-password database
- Detect more sequential patterns
- Improve password-strength estimation
- Add automated unit tests
- Develop a simple graphical user interface

## ⚠️ Disclaimer

This project is intended for educational purposes. Its strength classification is based on a limited set of rules and does not guarantee real-world password security. Avoid entering real or sensitive passwords into this tool.

## 👩‍💻 Author

**Ritika Mondal**

GitHub: [riti-jk-code](https://github.com/riti-jk-code)

---

*Built as a hands-on project to practice Python, Regex, and basic security concepts.*
