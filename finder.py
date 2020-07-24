print("Auto X Find | Choose from the menu")
print(" ")
print("1. multiply")
print("2. addition")
print("3. subtraction")
print("4. division")
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
    print("Operation: ",x,"-",user_number,"=",score)
    print("x =",x)
if choose == 4:
    print("Okay, type your first number")
    user_number = input()
    user_number = int(user_number)
    print("Okay, type result")
    score = input()
    score = int(score)

    x = score*user_number
    print("Operation: ",x,"/",user_number,"=",score)
    print("x =",x)