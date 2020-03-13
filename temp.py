'''
# Name:Darrel Reesha Pinto
# Employee ID:142874
# version no:Python 3
'''
# Feature1-Fuel Efficiency
import matplotlib.pyplot as plt
import pandas as pd
import gmplot

DATA = pd.read_csv('City Drive1 (1).csv')
NAN_DATA = DATA[DATA.isna().any(axis=1)]
DATA = DATA.dropna(how='all')
DATA['Trip Distance(km)'] = DATA['Trip Distance(km)'].replace(to_replace="-", value="0")
DATA['Trip average Litres/100 KM(l/100km)'] = \
        DATA['Trip average Litres/100 KM(l/100km)'].replace(to_replace="-", value="0")

#converting column to numberic value
DATA['Speed (OBD)(km/h)'] = pd.to_numeric(DATA['Speed (OBD)(km/h)'])
DATA['Trip Distance(km)'] = pd.to_numeric(DATA['Trip Distance(km)'])
DATA['Trip average Litres/100 KM(l/100km)'] \
        = pd.to_numeric(DATA['Trip average Litres/100 KM(l/100km)'])

SPEED = DATA['Speed (OBD)(km/h)']
DISTANCE = DATA['Trip Distance(km)']
FUEL = DATA['Trip average Litres/100 KM(l/100km)']
EFFICIENT = []
NOT_EFFICIENT = []
THRESHOLD = 9.4 #avg fuel economy of car is 9.4L/100km
for i in range(0, len(FUEL)):
    if FUEL[i] <= THRESHOLD:
        EFFICIENT.append(FUEL[i])
    else:
        NOT_EFFICIENT.append(FUEL[i])

#plot
plt.plot(DISTANCE, FUEL)
plt.axhline(9.4, color='r', linestyle='-')   #fuel economy above 9.4L/100km
plt.title("Fuel ECONOMY(in L/100km)")
plt.xlabel("DISTANCE(km)")
plt.ylabel("AVERAGE LITRES(L/100km)")
plt.show()
# Feature1 ends
# Fleet Owner gets to know the efficiency of the fuel.

# Feature2-Monitoring Engine Coolant Temperature
#Engine analysis Through Coolant Temperature and Trip time

#import osmapi

DF = pd.read_csv("City Drive1 (1).csv")
A = []
B = []
COOLANT_TEMPERATURE = DF["Engine Coolant Temperature(°C)"].replace(to_replace="-", value="0")
ENGINE_LOAD = DF["Engine Load(%)"].replace(to_replace="-", value="0")
TRIP_TIME = DF["Trip Time(Since journey start)(s)"].replace(to_replace="-", value="0")
for i in range(0, len(COOLANT_TEMPERATURE)):
    COOLANT_TEMPERATURE[i] = (float(COOLANT_TEMPERATURE[i])*9/5) +32
    B.append(COOLANT_TEMPERATURE[i])
for i in range(0, len(ENGINE_LOAD)):
    ENGINE_LOAD[i] = (float(ENGINE_LOAD[i]))
for i in range(0, len(TRIP_TIME)):
    TRIP_TIME[i] = (int(TRIP_TIME[i]))
    A.append(TRIP_TIME[i])
ENGINE_LOAD_THRESHOLD = 0.50*max(ENGINE_LOAD)
TRIP_TIME_THRESHOLD = 0.50*max(TRIP_TIME)
SAFESTATE = 0
LOWESTTEMP = 0.0
NORMALTEMP = 190.0 #Reference form internet safe state 190F to 220F
HIGHESTTEMP = 220.0
for i in range(0, len(COOLANT_TEMPERATURE)):
    if COOLANT_TEMPERATURE[i] > NORMALTEMP and COOLANT_TEMPERATURE[i] < HIGHESTTEMP:
        if TRIP_TIME[i] < TRIP_TIME_THRESHOLD:
            if ENGINE_LOAD[i] < ENGINE_LOAD_THRESHOLD:
                SAFESTATE += 1
        elif COOLANT_TEMPERATURE[i] < NORMALTEMP and COOLANT_TEMPERATURE[i] > LOWESTTEMP:
            SAFESTATE += 1
        elif COOLANT_TEMPERATURE[i] > HIGHESTTEMP:
            SAFESTATE -= 1
if SAFESTATE > 400:
    print("Engine is in safe state")
else:
    print("Engine is in danger state")
plt.plot(A, B, "r")
plt.xlabel("Trip Time")
plt.ylabel("Coolant Temperature")
plt.title("Engine Coolant Temperature Management")
plt.show()
# Feature2 ends
# Driver can monitor the engine coolant temperature and tell if engine is safe
# or not

#Feature3-Driver Efficiency
#import numpy as np
#import osmapi

#import os
SPEED_VIOLATION = []
LEVEL = []
GPS_TIME = []
LONGITUDE_DATA = []
LATITUDE_DATA = []
SPEED = []
DF = pd.read_csv("City Drive1 (1).csv")
LONGITUDE = DF[" Longitude"]
LATITUDE = DF[" Latitude"]
LEVEL = DF[" G(z)"]
SPEED = DF["Speed (GPS)(km/h)"]
GPSTIME = DF["GPS Time"]
for i in DF.index:
    if SPEED[i] > 50:
        SPEED_VIOLATION.append([DF[' Latitude'][i], DF[' Longitude'][i]])
        GPS_TIME.append(GPSTIME[i])
        LONGITUDE_DATA.append(LONGITUDE[i])
        LATITUDE_DATA.append(LATITUDE[i])
X = LONGITUDE_DATA
Y = LATITUDE_DATA
plt.scatter(X, Y, label='Speed', color='b')
plt.scatter(X, Y, label='level', color='r')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Speed Violation')
plt.legend()
plt.show()
GMAP1 = gmplot.GoogleMapPlotter(17.46, 78.377, 13)
GMAP1.heatmap(LATITUDE_DATA, LONGITUDE_DATA)
GMAP1.draw("Libraries\Documents\map1.html")
# Feature3 ends
# Fleet owner gets to know if driver is a rash driver or not

# Feature4-Engine Load RPM analysis
DF = pd.read_csv("City Drive1 (1).csv")
ENGINE_LOAD = DF["Engine Load(%)"].replace(to_replace="-", value="0")
ENGINE_RPM = DF["Engine RPM(rpm)"].replace(to_replace="-", value="0")
for i in range(0, len(ENGINE_LOAD)):
    ENGINE_LOAD[i] = float(ENGINE_LOAD[i])
for j in range(0, len(ENGINE_RPM)):
    ENGINE_RPM[j] = float(ENGINE_RPM[j])

MAXINLOAD = 0
for i in range(len(ENGINE_LOAD)):
    if MAXINLOAD < ENGINE_LOAD[i]:
        MAXINLOAD = ENGINE_LOAD[i]
        load_threshold = 0.4 * MAXINLOAD
        MAXINRPM = 0
for j in range(len(ENGINE_RPM)):
    if MAXINRPM < ENGINE_RPM[j]:
        MAXINRPM = ENGINE_RPM[j]
        rpm_threshold = 0.4 * MAXINRPM
        counter_overload = 0
        for i in range(len(ENGINE_RPM)):
            if ENGINE_LOAD[i] > load_threshold and  ENGINE_RPM[i] > rpm_threshold:
                counter_overload = counter_overload + 1
                if counter_overload < 200:
                    print("Load is correct")
                else:
                    print("Overload")
#Feature4 ends
# Driver can check if the vehicle is overloaded or not by the engine rpm and engine load
