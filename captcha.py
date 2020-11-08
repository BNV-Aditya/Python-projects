import random
charz = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
triez = 1
charzno = 10
while triez < 10:
    count = 1
    cap = random.choice(charz)
    while count < charzno:
        cap = cap + random.choice(charz)
        count = count + 1
    print(cap)
    capinput = input("type the captcha to prove that ur not a bot:")
    if cap == capinput:
        print(" access allowed ")
        triez = 10
    else:
        print("try again")
        charzno = charzno + 10
        triez = triez + 1
if triez < 10:
    print("ur a bot")  