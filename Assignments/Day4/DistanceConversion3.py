# Create a list of lambda functions that converts from tonns to kilograms, kilograms to grams, grams to
# milligrams, and milligrams to pounds. Input a weight from user in tonns and print it in remaining all
# units. E.g. if user inputs 0.002 tonns, then output should be 2 kg, 2000gm, 2000000 mg, and
# 4.409245244 lbs.

# def tons_to_kg(n):
#     return n*1000

# def kg_to_gm(n):
#     return n*1000

# def gm_to_mg(n):
#     return n*1000

# def mg_to_pound(n):
#     return n*0.00000220462

# tons=float(input("enter value in tones"))
# kg=tons_to_kg(tons)
# gm=kg_to_gm(kg)
# mg=gm_to_mg(gm)
# pound=mg_to_pound(mg)

# print("KG:",kg)
# print("GM:",gm)
# print("MG:",mg)
# print("pound:",pound)

#with lambda function

l1=[
    lambda tones:tones*1000,
    lambda kg:kg*1000,
    lambda gm:gm*1000,
    lambda pounds:pounds*0.00000220462
        ]


tons = float(input("Enter weight in tons: "))

# Apply conversions step by step
value = tons
for i in range(len(l1)):
    value = l1[i](value)
    print(f"{i}={value} ")



