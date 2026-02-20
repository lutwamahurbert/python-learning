import re
from datetime import datetime

def check_password_advanced(password):
    """
    Advanced password strength checker with detailed analysis
    """
    
    score = 0
    max_score = 10
    feedback = []
    warnings = []
    
    # 1. Length check (0-2 points)
    length = len(password)
    if length < 8:
        feedback.append("❌ Length: Too short")
        warnings.append("Password must be at least 8 characters")
    elif length < 12:
        score += 1
        feedback.append("⚠ Length: Acceptable but short")
    elif length < 16:
        score += 2
        feedback.append("✓ Length: Good")
    else:
        score += 2
        feedback.append("✓ Length: Excellent")
    
    # 2. Character variety (0-3 points)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for c in password)
    
    variety_count = sum([has_lower, has_upper, has_digit, has_special])
    
    if variety_count == 4:
        score += 3
        feedback.append("✓ Character variety: Excellent")
    elif variety_count == 3:
        score += 2
        feedback.append("✓ Character variety: Good")
    elif variety_count == 2:
        score += 1
        feedback.append("⚠ Character variety: Fair")
    else:
        feedback.append("❌ Character variety: Poor")
        warnings.append("Use uppercase, lowercase, numbers, and special characters")
    
    # 3. Common patterns check (deduct points)
    common_patterns = [
        (r"(.)\1{2,}", "Repeated characters"),
        (r"(abc|123|xyz)", "Sequential characters"),
        (r"(password|admin|user|login)", "Common words"),
        (r"(qwerty|asdf)", "Keyboard patterns"),
    ]
    
    pattern_found = False
    for pattern, description in common_patterns:
        if re.search(pattern, password.lower()):
            score -= 1
            warnings.append(f"⚠ Avoid {description}")
            pattern_found = True
    
    if not pattern_found:
        score += 1
        feedback.append("✓ No common patterns detected")
    
    # 4. Common passwords check
    common_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "letmein", "trustno1", "dragon", "baseball"
    ]
    
    if password.lower() in common_passwords:
        score = 0  # Instant fail
        warnings.append("🚨 CRITICAL: This is a commonly used password!")
    
    # 5. Complexity bonus
    if length >= 12 and variety_count == 4:
        score += 1
        feedback.append("✓ Complexity bonus earned")
    
    # 6. Entropy calculation (simplified)
    char_set_size = 0
    if has_lower:
        char_set_size += 26
    if has_upper:
        char_set_size += 26
    if has_digit:
        char_set_size += 10
    if has_special:
        char_set_size += 32
    
    # Approximate entropy
    import math
    if char_set_size > 0:
        entropy = length * math.log2(char_set_size)
        feedback.append(f"ℹ Entropy: ~{entropy:.1f} bits")
        
        if entropy >= 60:
            score += 1
            feedback.append("✓ High entropy")
    
    # Ensure score doesn't exceed max
    score = min(score, max_score)
    score = max(score, 0)  # No negative scores
    
    # Determine strength
    if score >= 8:
        strength = "VERY STRONG"
        color = "🟢"
    elif score >= 6:
        strength = "STRONG"
        color = "🟡"
    elif score >= 4:
        strength = "MEDIUM"
        color = "🟠"
    else:
        strength = "WEAK"
        color = "🔴"
    
    return {
        'strength': strength,
        'score': score,
        'max_score': max_score,
        'percentage': (score / max_score) * 100,
        'feedback': feedback,
        'warnings': warnings,
        'color': color
    }


def display_result(password, result):
    """Display password strength analysis"""
    print("=" * 60)
    print(f"PASSWORD ANALYSIS: {result['color']} {result['strength']}")
    print("=" * 60)
    print(f"Password: {'*' * len(password)}")
    print(f"Score: {result['score']}/{result['max_score']} ({result['percentage']:.0f}%)")
    print()
    
    print("FEEDBACK:")
    for item in result['feedback']:
        print(f"  {item}")
    print()
    
    if result['warnings']:
        print("⚠ WARNINGS:")
        for warning in result['warnings']:
            print(f"  {warning}")
        print()
    
    # Recommendations
    if result['score'] < result['max_score']:
        print("💡 RECOMMENDATIONS:")
        if len(password) < 12:
            print("  • Make your password at least 12 characters long")
        if not any(c.isupper() for c in password):
            print("  • Add uppercase letters (A-Z)")
        if not any(c.islower() for c in password):
            print("  • Add lowercase letters (a-z)")
        if not any(c.isdigit() for c in password):
            print("  • Add numbers (0-9)")
        if not any(c in "!@#$%^&*()" for c in password):
            print("  • Add special characters (!@#$%^&*)")
        print()


def main():
    """Main function"""
    print("╔════════════════════════════════════════════════════════╗")
    print("║     ADVANCED PASSWORD STRENGTH CHECKER                ║")
    print("║     For OT/ICS Cybersecurity Learning                 ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    
    # Test passwords
    test_passwords = [
        ("abc123", "Very weak password"),
        ("password", "Common password"),
        ("Password1", "Basic complexity"),
        ("P@ssw0rd123", "Medium strength"),
        ("MySecure!Pass2024", "Strong password"),
        ("Tr0ub4dor&3", "XKCD famous example"),
        ("correct horse battery staple", "Passphrase"),
        ("C0mpl3x!P@ssw0rd#2024", "Very complex"),
    ]
    
    for password, description in test_passwords:
        print(f"\nTesting: {description}")
        result = check_password_advanced(password)
        display_result(password, result)
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
