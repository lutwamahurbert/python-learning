permissions = {
 "lutwama" : "admin",
 "hubert" : "user",
 "charles" : "other"
}

for username in permissions:
 print(f"User : {username}")
 
#for role in permissions.values():
# print(f"Role : {role}")

for username, in  permissions.items(): 
 print(f"{username} has {role} role")
