
import random
def genBattAry(time):
    battAry = []
    for i in range(len(time)):
        battAry.append([
            Current(i),
            Voltage(i),
            ChargeState(i),
            Health(i),
            Temp(i),
            CellVoltage(i),
            OCellVoltage(i),
            Age(i)
        ])
    return battAry
        
    """
    function gens for all of these
    "getCurrent",	"getVoltage",	"getChargeState",	
    "getHealth",	"getTemp",	"getCellVoltage",
    "getOCellVoltage",	"getAge",
    """
def Current(x):
    return random.randint(-200,200)
def Voltage(x):
    return random.randint(300,600)
def ChargeState(x):
    return 100
    #return random.randint(0,100)
def Health(x):
    return 100
    #return random.randint(0,100)
def Temp(x):
    if (x < 5):
        return random.randint(20,40)
    else:
        return 70
def CellVoltage(x):
    return 4
    #return random.randint(0,4)
def OCellVoltage(x):
    return 4
    #return random.randint(0,4)
def Age(x):
    if x == 0:
        return 2000
    return 10
    #return random.randint(0,1000)