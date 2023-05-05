import random
def genCharAry(time):
    charAry = []
    for i in range(len(time)):
        charAry.append([
            Voltage(i),
            Current(i),
            Status(i),
            Age(i)
        ])
    return charAry

    """
    "getVoltage",	"getCurrent",	"getStatus",
    "getAge"
    """
def Voltage(x):
    return 0
def Current(x):
    return 0
def Status(x):
    return 0
def Age(x):
    return 0