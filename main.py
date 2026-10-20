import re
def check_common_password(password):
    common_passwords = [
        "password",
        "password123",
        "12345678",
        "qwerty123",
        "admin123",
    ]

    return password.lower() in common_passwords
def check_repeated_chars(password):
    return re.search(r"(.)\1{3,}", password) is not None            # (.) — jekono ekta character match kore. \1 — oi eki character abar match kore. {3} — aro ontoto 3 bar repeat hote hobe.
def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return re.search(r"[A-Z]", password) is not None

def check_lowercase(password):
    return re.search(r"[a-z]", password) is not None

def check_digit(password):
    return re.search(r"[0-9]", password) is not None

def check_special(password):
    return re.search(r"[^A-Za-z0-9]", password) is not None

def check_sequential(password):
    return re.search(r"abcd|bcde|cdef|defg|efgh|fghi|ghij|1234|2345|3456|4567|5678|6789|7890", password.lower()) is not None

password = input("Enter your password: ")
has_length = check_length(password)
has_upper = check_uppercase(password)
has_lower = check_lowercase(password)
has_digit = check_digit(password)
has_special = check_special(password)
has_repeated = check_repeated_chars(password)
has_sequential = check_sequential(password)
score = 0

if has_length:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("Score:", score, "/5")
is_common = check_common_password(password)

if is_common or has_repeated or has_sequential:
    print("Strength: Weak")

    if is_common:
        print("Warning: This is a common password!")

    if has_repeated:
        print("Warning: Repeated characters detected!")

    if has_sequential:
        print("Warning: Sequential pattern detected!")
elif score <= 2:
    print("Weak password")
   
elif score <= 4:
    print("Moderate password")
    
else:
    print("Strong password")

print("\nSuggestions:")

if not has_length:
    print("- Use at least 8 characters.")

if not has_upper:
    print("- Add an uppercase letter.")

if not has_lower:
    print("- Add a lowercase letter.")

if not has_digit:
    print("- Add a digit.")

if not has_special:
    print("- Add a special character.")

if has_length and has_upper and has_lower and has_digit and has_special:
    print("- All basic checks passed!")
if has_sequential:
    print("- Avoid predictable sequences like abcd or 1234.")
