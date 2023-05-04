
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
    return 0
def Voltage(x):
    return 0
def ChargeState(x):
    return 0
def Health(x):
    return 0
def Temp(x):
    return 0
def CellVoltage(x):
    return 0
def OCellVoltage(x):
    return 0
def Age(x):
    return 0