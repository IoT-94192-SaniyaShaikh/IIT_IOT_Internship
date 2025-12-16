# Write a lambda functions to convert kilometers to meters, meters to centimeters, centimeters to
# millimeters, feets to inches, and inches to centimeter. Write a function distance_converter() that takes a
# distance, conversion type as a string (e.g. km to m, m to cm, etc.) and a conversion function as
# argument. This function does the converion using given function and print the result. Input a distance
# from user and print all conversions

km_to_m=lambda n:n*1000
m_to_cm=lambda n:n*100
cm_to_mm=lambda n:n*1000
feet_to_inches=lambda n:n*12
inches_to_cm=lambda n:n*2.54

def distance_convertor(distance,conversion_type,func):
    result=func(distance)
    print(f"{conversion_type}:{result}")

distance=int(input("enter distnace:"))
distance_convertor(distance,"km to m:",km_to_m)
distance_convertor(distance,"m to cm:",m_to_cm)
distance_convertor(distance,"cm to mm:",cm_to_mm)
distance_convertor(distance,"inches to cm",inches_to_cm)
distance_convertor(distance,"feet to inches",feet_to_inches)