def  maxValue(strNum):
    resStrNum =""
    while(len(resStrNum) < len(strNum)):
        biggestDigit=0
        for n in strNum:
            if int(n)>biggestDigit and resStrNum.count(n)<strNum.count(n):
                biggestDigit=int(n)
        resStrNum+=str(biggestDigit)
    return resStrNum


num = input()
print(maxValue(num))
