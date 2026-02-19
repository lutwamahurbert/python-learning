username = "admin"
password = "admin1"
two_FA_auth = "2025"

if username == "admin":
 print("username correct")

 if password == "admin1":
   print("password corect")

  if two_FA_auth == "2025":
   print("two_FA_auth correct")
   print("✔ access granted")

  else:
   print("❎, incorrect 2FA-auth")

 else: 
  print("❎, incorrect password")

else:
 print("incorrect username")
 
