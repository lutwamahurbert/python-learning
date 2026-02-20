def get_password_input():
    """Get password from user securely"""
    import getpass
    
    print("\n" + "=" * 60)
    print("INTERACTIVE PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    print("\nEnter your password to check its strength.")
    print("(Your password will be hidden as you type)")
    print()
    
    password = getpass.getpass("Password: ")
    return password


def check_strength_interactive(password):
    """Check password strength with interactive feedback"""
    
    print("\n🔍 Analyzing your password...\n")
    
    checks = {
        'Length (≥12 chars)': len(password) >= 12,
        'Uppercase letters': any(c.isupper() for c in password),
        'Lowercase letters': any(c.islower() for c in password),
        'Numbers': any(c.isdigit() for c in password),
        'Special characters': any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
        'No common patterns': not any(p in password.lower() for p in ['123', 'abc', 'qwerty', 'password']),
    }
    
    passed = 0
    for check, result in checks.items():
        status = "✓" if result else "❌"
        print(f"{status} {check}")
        if result:
            passed += 1
    
    print()
    print(f"Checks passed: {passed}/{len(checks)}")
    
    # Calculate percentage
    percentage = (passed / len(checks)) * 100
    
    # Progress bar
    bar_length = 40
    filled = int(bar_length * passed / len(checks))
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n[{bar}] {percentage:.0f}%")
    
    # Recommendation
    if percentage >= 80:
        print("\n🟢 EXCELLENT! Your password is strong.")
    elif percentage >= 60:
        print("\n🟡 GOOD! Your password is fairly strong.")
        print("💡 Consider adding more variety for better security.")
    else:
        print("\n🔴 WEAK! Your password needs improvement.")
        print("💡 Follow the suggestions above to strengthen it.")


def main():
    """Main interactive function"""
    while True:
        password = get_password_input()
        
        if not password:
            print("\n❌ Password cannot be empty!")
            continue
        
        check_strength_interactive(password)
        
        print("\n" + "=" * 60)
        again = input("\nCheck another password? (y/n): ").lower()
        if again != 'y':
            print("\nThank you for using the Password Strength Checker!")
            break


if __name__ == "__main__":
    main()
