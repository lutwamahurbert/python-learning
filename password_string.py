password = "admin123"

for char in password:
 if char.isdigit():
  print(f"Found digit :{char}")
 elif char.isupper:
  print(f"Found uppercase : {char}")
 elif char in "!@#$%^&*":
  print(f"Found special character : {char}")
 else:
  print("found nothing")
