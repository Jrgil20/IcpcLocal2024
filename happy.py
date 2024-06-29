length = int(input())
costumers = []

for i in range(length):
    rawInput = input()
    inputSplitted = rawInput.split(" ")
    
    costumers.append({
        "position": int(inputSplitted[0]),
        "arrivalTime": int(inputSplitted[1]),
        "serviceTime": int(inputSplitted[2]),
        "patienceTime": int(inputSplitted[3]),
    })

prevCostumerFinishTime = costumers[0]["arrivalTime"]
for i in range(length):
    costumerWillWaitUntil = costumers[i]["arrivalTime"] + costumers[i]["patienceTime"]
    if(prevCostumerFinishTime <= costumerWillWaitUntil):
        print(i+1)
        if(costumers[i]["arrivalTime"] + costumers[i]["serviceTime"] > prevCostumerFinishTime +  + costumers[i]["serviceTime"]):
            prevCostumerFinishTime = costumers[i]["arrivalTime"] + costumers[i]["serviceTime"]
        else:
            prevCostumerFinishTime = prevCostumerFinishTime + costumers[i]["serviceTime"]
    