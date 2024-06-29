def enesimoPrimo(qery,primos):
    cont=1
    nums=[1]
    i=1
    while(cont<qery):
        i+=1
        multiplo=False
        for primo in primos:
            if i%primo==0:
                multiplo=True
                break
            if multiplo==False:
                nums.append(i)
                cont+=1
    return nums[-1]

linea1=input().split(" ")
query=int(linea1[0])
primos=input().split(" ")