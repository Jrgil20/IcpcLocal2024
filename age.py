def determinePositiveInteger(o,a,k):
    for n1 in range(1,o+1):        
        for n2 in range(1,a+1):
            if n1*a+n2*k==o:
                return 1
    return 0

ages=input().split(" ")
o=int(ages[0])
a=int(ages[1])
k=int(ages[2])
print(determinePositiveInteger(o,a,k))