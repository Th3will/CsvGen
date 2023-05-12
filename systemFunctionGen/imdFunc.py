def genImdAry(time):
    imdAry = []
    for i in range(len(time)):
        imdAry.append([
            Isolation(i),
            IsolationStates(i),
            Hardware_Error(i),
            Touch_energy_fault(i),
            High_Uncertainty(i),
            Exc_off(i),
            High_Battery_Voltage(i),
            Low_Battery_Voltage(i),
            Age(i)
        ])
    return imdAry

"""
"getIsolation",	"getIsolationStates",	"getHardware_Error",
	"getTouch_energy_fault",	"getHigh_Uncertainty",	"getExc_off",
    "getHigh_Battery_Voltage",	"getLow_Battery_Voltage",	"getAge"
    """
def Isolation(x):
    return 0
def IsolationStates(x):
    return 0
def Hardware_Error(x):
    return 0
def Touch_energy_fault(x):
    return 0
def High_Uncertainty(x):
    return 0
def Exc_off(x):
    return 0
def High_Battery_Voltage(x):
    return 0
def Low_Battery_Voltage(x):
    return 0
def Age(x):
    if x == 2:
        return 2000
    return 0