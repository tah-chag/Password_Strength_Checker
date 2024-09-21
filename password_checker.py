import re

def assess_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess strength
    strength_score = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])
    
    # Feedback on strength
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = {
        "Strength": strength,
        "Length Criteria": length_criteria,
        "Uppercase Letters": upper_criteria,
        "Lowercase Letters": lower_criteria,
        "Numbers": number_criteria,
        "Special Characters": special_criteria
    }

    return feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    feedback = assess_password_strength(password)
    
    print("\nPassword Assessment:")
    for key, value in feedback.items():
        print(f"{key}: {'Yes' if value else 'No'}")