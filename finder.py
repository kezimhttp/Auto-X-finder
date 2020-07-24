print("Auto X Find | Choose from the menu")
print("1. multiply")
print("2. addition")
print("3. subtraction")
choose = input()
choose = int(choose)

if choose == 1:
    print("Okay, type your first number")
    user_number = input()
    user_number = int(user_number)
    print("Okay, type result")
    score = input()
    score = int(score)

    x = score/user_number
    print("Operation: ",user_number,"*",x,"=",score)
    print("x =",x)
if choose == 2:
    print("Okay, type your first number")
    user_number = input()
    user_number = int(user_number)
    print("Okay, type result")
    score = input()
    score = int(score)

    x = score-user_number
    print("Operation: ",user_number,"+",x,"=",score)
    print("x =",x)
if choose == 3:
    print("Okay, type your first number")
    user_number = input()
    user_number = int(user_number)
    print("Okay, type result")
    score = input()
    score = int(score)

    x = score+user_number
    print("Operation: ",user_number,"-",x,"=",score)
    print("x =",x)