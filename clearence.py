clearence_level = 5

if clearence_level >= 5:
    print("Top secret")
    print("access granted")
elif clearence_level >= 4:
    print("Management")
    print("access granted")
elif clearence_level >= 3:
    print("low mgmt")
    print("access granted")
elif clearence_level >= 2:
    print("usual guys")
    print("access granted")
elif clearence_level >= 1:
    print("visitors")
    print("access granted")
else:
    print("nothing entered")
    print("access denied")