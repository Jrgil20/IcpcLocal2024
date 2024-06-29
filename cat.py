edadGatuna = input()
Datos = edadGatuna.split(" ")

anosGatunos= int(Datos[0])
mesesGatunos= int(Datos[1])

Anos = 0
Meses = 0

if( (anosGatunos >= 0 and anosGatunos<=20) or (mesesGatunos >= 0 and mesesGatunos<=11)):
    if (anosGatunos == 0):
        Meses =mesesGatunos*15
    elif (anosGatunos == 1):
        Anos = 15
        if (mesesGatunos != 0):
            Meses = mesesGatunos*9
    elif (anosGatunos == 2):
        Anos = 15+9
        if (mesesGatunos != 0):
            Meses = mesesGatunos*4
    else:
        Anos = 15+9+(anosGatunos-2)*4
        Meses = mesesGatunos*4

    while( Meses >11):
        Anos = Anos+1
        Meses = Meses-12

print(Anos,Meses)