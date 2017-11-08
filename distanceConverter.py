#Introduces program, explains rules
print("This program will convert distances to other measurement units.")
print("Distance: Number of distance")
print("Units: Unit of measurement that will be converted")
print("Target Units: Unit of measurment that distance will be converted into")

distance = float(input("Enter Distance (numbers): "))#Gets distance from user
unit = str(input("Enter Units(mi, km, ft, or m): "))#Gets units to be converted
target = str(input("Enter Target Units(mi, km, ft, or m): "))#Gets units to be converted into

#mi to target conversions
if unit=='mi' and target=='km':
    answer=distance*1.60934
elif unit=='mi' and target=='ft':
    answer=distance*5280
elif unit=='mi' and target=='m':
    answer=distance*1609.34
elif unit=='mi' and target=='in'
    answer=distance*63360
elif unit=='mi' and target=='cm'
    answer=distance*160934
#km to target conversions
elif unit=='km' and target=='mi':
    answer=distance*0.621371
elif unit=='km' and target=='ft':
    answer=distance*3280.84
elif unit=='km' and target=='m':
    answer=distance*1000
elif unit=='km' and target=='in'
    answer=distance*39370.1
elif unit=='km' and target=='cm'
    answer=distance*100000
#ft to target conversions
elif unit=='ft' and target=='mi':
    answer=distance*0.000189394
elif unit=='ft' and target=='km':
    answer=distance*0.0003048
elif unit=='ft' and target=='m':
    answer=distance*0.3048
elif unit=='ft' and target=='in'
    answer=distance*12
elif unit=='ft' and target=='cm'
    answer=distance*30.48
#m to target conversions
elif unit=='m' and target=='mi':
    answer=distance*0.000621371
elif unit=='m' and target=='km':
    answer=distance*0.001
elif unit=='m' and target=='ft':
    answer=distance*3.28084
elif unit=='m' and target=='in'
    answer=distance*39.3701
elif unit=='m' and target=='cm'
    answer=distance*100
#in to target to target to target conversions
elif unit=='in' and target=='mi'
    answer=distance*((1.5783**10)-5)
elif unit=='in' and target=='km'
    answer=distance*((2.54**10)-5)
elif unit=='in' and target=='ft'
    answer=distance*0.0833333
elif unit=='in' and target=='m'
    answer=distance*0.0254
elif unit=='in' and target=='cm'
    answer=distance*2.54
#cm to target to target conversions
elif unit=='cm' and target=='mi'
    answer=distance*((6.2137**10)-5)
elif unit=='cm' and target=='km'
    answer=distance*((1**10)-5)
elif unit=='cm' and target=='ft'
    answer=distance*0.0328084
elif unit=='cm' and target=='m'
    answer=distance*0.01
elif unit=='cm' and target=='in'
    answer=distance*0.393701
#Displays to target results
else:
    print("Your response is invalid. How dare you. Goodbye.")
    quit()
print("I have finished the math. Your final answer is: ",answer)
