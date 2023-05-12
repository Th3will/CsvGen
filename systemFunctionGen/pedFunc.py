def genPedAry(time):
    pedAry = []
    for i in range(len(time)):
        pedAry.append([
            APPS1(i),
            APPS2(i),
            BrakeLimit(i),
            BrakePressure1(i),
            BrakePressure2(i),
            Age(i)
        ])
    return pedAry

    """
    "getAPPS1",	"getAPPS2",	"getBrakeLimit",
    "getBrakePressure1",	"getBrakePressure2",	"getAge"
    """
    
def APPS1(x):
    return 40
def APPS2(x):
    return 40
def BrakeLimit(x):
    return 0
def BrakePressure1(x):
    if x < 5:
        return 0
    return 10
def BrakePressure2(x):
    if x < 5:
        return 0
    return 10
def Age(x):
    if x == 4:
        return 2000
    return 0