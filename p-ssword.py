import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Strong"
    
    if len(password) >= 12 and re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Unbreakable"
    
    return "Very Weak"

user_password = input("Enter your password: ")

strength_result = check_password_strength(user_password)
print(f"The strength of your password is: {strength_result}")
