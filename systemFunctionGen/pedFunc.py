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
    return 0
def APPS2(x):
    return 0
def BrakeLimit(x):
    return 0
def BrakePressure1(x):
    return 0
def BrakePressure2(x):
    return 0
def Age(x):
    return 0