import numpy as np
import csv

filename = input("filename: ")
f = open(filename, "x")
wr = csv.writer(f)
#time is 0.1 seconds, gonna be from time 0-5s

invLabels = [
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
]
batLabels = [
    "getCurrent",	"getVoltage",	"getChargeState",	
    "getHealth",	"getTemp",	"getCellVoltage",
    "getOCellVoltage",	"getAge",
]
imdLabels = [
    "getIsolation",	"getIsolationStates",	"getHardware_Error",
	"getTouch_energy_fault",	"getHigh_Uncertainty",	"getExc_off",
    "getHigh_Battery_Voltage",	"getLow_Battery_Voltage",	"getAge"
]
charLabels = [
    "getVoltage",	"getCurrent",	"getStatus",
    "getAge"
    ]
sensLabels = [
    "getLatitude"	,"getLatitudeHP",	"getLongitude",
    "getLongitudeHP" ,"getGPSPrecision", "getLinAccelX",
    "getLinAccelY"	,"getLinAccelZ",	"getAbsOrenX",
    "getAbsOrenY"	,"getAbsOrenZ",	"getAngVeloX",
    "getAngVeloY"	,"getAngVeloZ",	"getFRtemp1",
    "getFRtemp2"	,"getFRtravel",	"getFRspeed",
    "getFRpsi"	,"getFLtemp1",	"getFLtemp2",
    "getFLtravel"	,"getFLspeed",	"getFLpsi",
    "getRRtemp1"	,"getRRtemp2",	"getRRtravel",
    "getRRspeed"	,"getRRpsi",	"getRLtemp1",
    "getRLtemp2"	,"getRLtravel",	"getRLspeed",
    "getRLpsi"	,"getAge"
]
pedLabels = [
    "getAPPS1",	"getAPPS2",	"getBrakeLimit",
    "getBrakePressure1",	"getBrakePressure2",	"getAge"
]
timeRange = input("what is the desired time range?")
time = np.arange(0,int(timeRange),0.1)
formattedArr = [[]]
typeGen = input("what do you want to generate? Options are: \n all, inv, bat, imd, char, sens, ped \n") 

wr.writerows(formattedArr)