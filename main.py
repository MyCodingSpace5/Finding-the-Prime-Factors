primenumber = input("Enter an prime number")
primenumberproof = lambda a,b: a/b
i = 1
for i in range(100):
    returnresult = primenumberproof(int(primenumber), i)
    if(returnresult != int):
        print("Factor" + "" + i + "Cannot be evenly divided into an prime number")
        continue
    else:
        print("This number is not an prime number as it has mutiple factors that arent 1")
        break
        
