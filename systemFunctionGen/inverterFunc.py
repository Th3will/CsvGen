def genInverterAry(time):
    inverterAry = []
    for i in range(len(time)):
        inverterAry.append([
            ERPM(i),
            Duty(i),
            VoltIn(i),
            ACCurrent(i),
            DCCurrent(i),
            InvTemp(i),
            MotorTemp(i),
            Faults(i),
            CurrentD(i),
            CurrentQ(i),
            ThrottleIn(i),
            BrakeIn(i),
            D1(i),
            D2(i),
            D3(i),
            D4(i),
            DO1(i),
            DO2(i),
            DO3(i),
            DO4(i),
            DriveEnable(i),
            CapTempLim(i),
            DCCurrentLim(i),
            DriveEnableLim(i),
            IgbtAccelTempLim(i),
            IgbtTempLim(i),
            VoltInLim(i),
            MotorAccelTempLim(i),
            MotorTempLim(i),
            RPMMinLimit(i),
            RPMMaxLimit(i),
            PowerLimit(i),
            Age(i)
        ])
    return inverterAry

    """
    "getERPM",	"getDuty", "getVoltIn",
    "getACCurrent",	"getDCCurrent",	"getInvTemp",
    "getMotorTemp", "getFaults", "getCurrentD",
    "getCurrentQ", "getThrottleIn", "getBrakeIn",	
    "getD1", "getD2", "getD3",
	"getD4", "getDO1",	"getDO2",
    "getDO3", "getDO4",	"getDriveEnable",
    "getCapTempLim", "getDCCurrentLim", "getDriveEnableLim",    
    "getIgbtAccelTempLim",    "getIgbtTempLim", "getVoltInLim",
    "getMotorAccelTempLim", "getMotorTempLim", "getRPMMinLimit",
    "getRPMMaxLimit",	"getPowerLimit",	"getAge"
    """
def ERPM(time):
    return 0
def Duty(time):
    return 0
def VoltIn(time):
    return 0
def ACCurrent(time):
    return 0
def DCCurrent(time):
    return 0
def InvTemp(time):
    return 0
def MotorTemp(time):
    return 0
def Faults(time):
    return 0
def CurrentD(time):
    return 0
def CurrentQ(time):
    return 0
def ThrottleIn(time):
    return 0
def BrakeIn(time):
    return 0
def D1(time):
    return 0
def D2(time):
    return 0
def D3(time):
    return 0
def D4(time):
    return 0
def DO1(time):
    return 0
def DO2(time):
    return 0
def DO3(time):
    return 0
def DO4(time):
    return 0
def DriveEnable(time):
    return 0
def CapTempLim(time):
    return 0
def DCCurrentLim(time):
    return 0
def DriveEnableLim(time):
    return 0
def IgbtAccelTempLim(time):
    return 0
def IgbtTempLim(time):
    return 0
def VoltInLim(time):
    return 0
def MotorAccelTempLim(time):
    return 0
def MotorTempLim(time):
    return 0
def RPMMinLimit(time):
    return 0
def RPMMaxLimit(time):
    return 0
def PowerLimit(time):
    return 0
def Age(time):
    return 0