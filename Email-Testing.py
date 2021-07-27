email = input("please enter email")
valid = False
for i in range(0, len(email)+1):
    email_check = list(email)
    if "@" in email_check:
        valid = True
        i += 1
    else:
        i += 1
