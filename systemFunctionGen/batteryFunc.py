
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
    return random.randint(0,100)
def Health(x):
    return random.randint(0,100)
def Temp(x):
    return random.randint(0,150)
def CellVoltage(x):
    return random.randint(0,4)
def OCellVoltage(x):
    return random.randint(0,4)
def Age(x):
    return random.randint(0,1000)