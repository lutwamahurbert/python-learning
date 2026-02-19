#!/usr/bin/env python3

print("=" * 50)
print("PASSWORD STRENGTH CHECKER")
print("=" * 50)
print()

password = input("Enter password to check: ")

score = 0

if len(password) >= 8:
    score += 1
    print("✓ Length OK")

if any(c.isupper() for c in password):
    score += 1
    print("✓ Has uppercase")

if any(c.islower() for c in password):
    score += 1
    print("✓ Has lowercase")

if any(c.isdigit() for c in password):
    score += 1
    print("✓ Has numbers")

if any(c in "!@#$%^&*()" for c in password):
    score += 1
    print("✓ Has special chars")

print()
print(f"Score: {score}/5")

if score >= 4:
    print("🟢 STRONG")
elif score >= 2:
    print("🟡 MEDIUM")
else:
    print("🔴 WEAK")
print("bye")
