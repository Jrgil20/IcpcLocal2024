import math

rawInputLineOne = input()
radiuses = rawInputLineOne.split(" ")

throws = int(input())
throwsCoordinates = []

for i in range(throws):
    throwCoordInput = input()
    throwCoord = throwCoordInput.split(" ")
    throwsCoordinates.append({
        "x": throwCoord[0],
        "y": throwCoord[1]
    })

points = 0

w = int(radiuses[0])
b = int(radiuses[1])
d = int(radiuses[2])
s = int(radiuses[3])
wedgesStep = 360.0/float(radiuses[0])

for i in range(throws):
    xSqr = pow(float(throwsCoordinates[i]["x"]), 2)
    ySqr = pow(float(throwsCoordinates[i]["y"]), 2)
    radioThrow = math.sqrt(xSqr + ySqr)
    if(radioThrow != 0.0):
        angleThrow = math.degrees(math.acos(float(throwsCoordinates[i]["x"])/radioThrow))
    if(float(throwsCoordinates[i]["y"]) < 0):
        angleThrow = 360 - angleThrow
    
    if((xSqr + ySqr) < b**2):
        points = points + 50
    else:
        for j in range(w):
            recorrido = wedgesStep*(j+1)
            if((xSqr + ySqr) < s**2):
                intervaloAnterior = 0
                if(recorrido != 0):
                    intervaloAnterior = recorrido-wedgesStep
                if((angleThrow < recorrido) and (angleThrow > intervaloAnterior)):
                    reward = j+1
                    if(((xSqr + ySqr) > b**2) and ((xSqr + ySqr) < d**2)):
                        reward = reward*2
                    points = points + reward

print(points)