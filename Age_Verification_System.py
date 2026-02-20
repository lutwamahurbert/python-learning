age = int(input("Enter your age: "))

if age < 13:
    print("❌ Access Denied")
    print("Users under 13 cannot access this content (COPPA compliance)")
elif age < 18:
    print("⚠ Parental Consent Required")
    print("Users 13-17 need parental permission")
    consent = input("Do you have parental consent? (yes/no): ")
    if consent.lower() == "yes":
        print("✓ Access Granted with parental consent")
    else:
        print("❌ Access Denied - Parental consent required")
else:
    print("✓ Full Access Granted")
    print("Welcome!")
