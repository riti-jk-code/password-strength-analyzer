import re
password = input("Enter your password:")
score = 0
def check_digit(password):
    return re.search(r"[0-9]", password) is not None
if check_digit(password):
    score += 1
    print(score)