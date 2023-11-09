user = ["ahmad", "doni", "dita", "ardi", "ucup", "usep"]
user_notActive = ["ahmad", "dita", "ardi"]

i = 0
while i < len(user):
    if user[i] in user_notActive:
        print(user[i], "is not active")
    else:
        print(user[i], "is active")
    i += 1
