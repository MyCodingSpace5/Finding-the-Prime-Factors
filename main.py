primenumber = input("Enter an prime number")
primenumberproof = lambda a,b: a/b
numberofprimefactors = []
z = 0
i = 1
for i in range(100):
    returnresult = primenumberproof(int(primenumber), i)
    if(returnresult != int):
        break
        print("Not an prime factor")
        print(returnresult)
    else:
        numberofprimefactors.append(returnresult)
        continue
for v in int(primenumber) % 2:
    power = primenumberproof(numberofprimefactors[z], int(numberofprimefactors[z]) % 2)
    if(returnresult != int):
        break
        print("Tried to reduce to the simplest form, failed opreation")
    else:
        print("Operation successful for" + numberofprimefactors[z])
        z+=1

