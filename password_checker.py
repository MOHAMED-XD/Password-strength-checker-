import re

def check_password(password):
    # simple password strength checker
    length_ok = len(password) >= 8
    has_digit = re.search(r"\d", password) is not None
    has_lower = re.search(r"[a-z]", password) is not None
    has_upper = re.search(r"[A-Z]", password) is not None
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_ok, has_digit, has_lower, has_upper, has_symbol])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


if __name__ == "__main__":
    print("Password Strength Checker")
    pwd = input("Enter your password: ")
    print("Your password is:", check_password(pwd))
