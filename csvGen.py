import numpy as np
import csv
from systemFunctionGen import *

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

def aryStringConv(ary):
    temp = "{ \n"
    for i in range(len(ary)-1):
        temp += "{"
        for j in range (len(ary[0])-1):
            temp += str(ary[i][j])
            temp += ", "
        temp += str(ary[i][len(ary[0])-1])
        temp += "}, \n"
    temp += "}"
    return temp


#timeRange = input("what is the desired time range?")
time = np.arange(0,int(10),1)
formattedArr = []
typeGen = input("what do you want to generate? Options are: \n all, inv, bat, imd, char, sens, ped \n")
testPed = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
if(typeGen == "all"):
    f.open("all.txt", "w", newline = '')
    allTemp = ""
    
    allTemp += "Inverter Data: \n"
    npInv = np.array(inverterFunc.genInverterAry(time))
    allTemp+= aryStringConv(list(np.transpose(npInv)))
    
    allTemp += "Battery Data: \n"
    npBat = np.array(batteryFunc.genBattAry(time))
    allTemp+= aryStringConv(list(np.transpose(npBat)))
    
    allTemp += "IMD Data: \n"
    npImd = np.array(imdFunc.genImdAry(time))
    allTemp+= aryStringConv(list(np.transpose(npImd)))
    
    allTemp += "Charger Data: \n"
    npChar = np.array(charFunc.genCharAry(time))
    allTemp+= aryStringConv(list(np.transpose(npChar)))
    
    allTemp += "Sensor Data: \n"
    npSens = np.array(sensFunc.genSensAry(time))
    allTemp+= aryStringConv(list(np.transpose(npSens)))
    
    allTemp += "Pedal Data: \n"
    npPed = np.array(pedFunc.genPedAry(time))
    allTemp+= aryStringConv(list(np.transpose(npPed)))
    
    f.write(allTemp)
elif (typeGen == "inv"):
    f = open("INV.CTT", "w", newline = '')
    #formattedArr.append(invLabels)
    npInv = np.array(inverterFunc.genInverterAry(time))
    f.write(aryStringConv(list(np.transpose(npInv))))

    
elif (typeGen ==  "bat"):
    f = open("BATT.txt", "w",newline = '')
    #formattedArr.append(batLabels)
    npBat = np.array(batteryFunc.genBattAry(time))
    f.write(aryStringConv(list(np.transpose(npBat))))

    
elif (typeGen == "imd"):
    f = open("IMD.txt", "w", newline = '')
    npImd = np.array(imdFunc.genImdAry(time))
    f.write(aryStringConv(list(np.transpose(npImd))))

    
elif (typeGen == "char"):
    f = open("CHAR.txt", "w", newline = '')
    npChar = np.array(charFunc.genCharAry(time))
    f.write(aryStringConv(list(np.transpose(npChar))))

    
elif (typeGen == "sens"):
    f = open("SENS.txt", "w", newline = '')
    npSens = np.array(sensFunc.genSensAry(time))
    f.write(aryStringConv(list(np.transpose(npSens))))

    
elif (typeGen == "ped"):
    f = open("PEDALS.txt", "w", newline = '')
    npPed = np.array(inverterFunc.genInverterAry(time))
    f.write(aryStringConv(list(np.transpose(npInv))))

    
else:
    print("invalid input")
    exit()
#print(formattedArr)