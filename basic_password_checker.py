def check_password_strength(password):
    """
    Basic password strength checker
    Returns: strength level (Weak/Medium/Strong)
    """
    
    # Initialize score
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
        feedback.append("✓ Length is adequate")
    else:
        feedback.append("❌ Password too short (minimum 8 characters)")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("❌ Add numbers")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("❌ Add special characters")
    
    # Determine strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 3:
        strength = "MEDIUM"
    else:
        strength = "STRONG"
    
    return strength, score, feedback


# Test the function
def main():
    print("=== BASIC PASSWORD STRENGTH CHECKER ===\n")
    
    # Test passwords
    test_passwords = [
        "abc",
        "password",
        "Password123",
        "SecureP@ss123",
        "MyStr0ng!Pass"
    ]
    
    for pwd in test_passwords:
        strength, score, feedback = check_password_strength(pwd)
        
        print(f"Password: {pwd}")
        print(f"Strength: {strength} ({score}/5)")
        print("Feedback:")
        for item in feedback:
            print(f"  {item}")
        print()


if __name__ == "__main__":
    main()
