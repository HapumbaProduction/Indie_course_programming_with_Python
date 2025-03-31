password = input()

if len(password) < 7:
    print("Short")
else:
    confirm_password = input()
    if password != confirm_password:
        print("Difference")
    else:
        print("OK")
