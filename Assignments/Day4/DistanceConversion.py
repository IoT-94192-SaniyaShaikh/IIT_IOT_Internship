# 1. Write functions to convert kilometers to meters, meters to centimeters, centimeters to millimeters, feets
# to inches, and inches to centimeter. Write a function distance_converter() that takes a distance,
# conversion type as a string (e.g. km to m, m to cm, etc.) and a conversion function as argument. This
# function does the converion using given function and print the result. Input a distance from user and
# print all conversions

def kmToM(n):
    return n*1000

def MeterToCm(n):
    return n*100

def cm_to_mm(n):
    return n*1000

def feet_to_inches(n):
    return n*12

def inches_to_cm(n):
    return n*2.54

def distance_conversion(Distance,conversion_type,func):
    result=func(Distance)
    print(f"{conversion_type}:{result}")


distance=int(input("Enter distance:"))
distance_conversion(distance,"KmToMeter",kmToM)
distance_conversion(distance,"Meter to cm",MeterToCm)
distance_conversion(distance,"cm to mm:",cm_to_mm)
distance_conversion(distance,"inches to cm",inches_to_cm)
distance_conversion(distance,"feet to inches",feet_to_inches)