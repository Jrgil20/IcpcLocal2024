import math

entrada = input().split(" ")
base = []

for i in range(int(entrada[0])):
    base.append("A")
for i in range(int(entrada[1])):
    base.append("B")
for i in range(int(entrada[2])):
    base.append("C")

combinaciones = []
comb = []

print(math.comb(base, combinaciones))