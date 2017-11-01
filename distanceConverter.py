print("This program will convert distances to other measurement units.")
print("Distance: Number of distance")
print("Units: Unit of measurement now")
print("Target Units: Units distance will be converted into")
print("Enter Distance(numbers): ")
distance=float(input())
print("Enter Units(mi, km, ft, or m): ")
unit=float(input())
print("enter Target Units(mi, km, ft, or m): ")
target=float(input())
if unit==mi and target==km:
    #answer=Conversion for miles to kilometers
elif unit=mi and target=ft:
    #answer=Conversion for miles to feet
elif unit=mi and target=m:
    #answer=Conversion for miles to meters
elif unit=km and target=mi:
    #answer=Conversion for kilometers to miles
elif unit=km and target=ft:
    #answer=Conversion for kilometers to feet
elif unit=km and target=m:
    #answer=Conversion for kilometers to meters
elif unit=ft and target=mi:
    #answer=Conversion for feet to miles
elif unit=ft and target=km:
    #answer=Conversion for feet to kilometers
elif unit=ft and target=m:
    #answer=Conversion for feet to meters
elif unit=m and target=mi:
    #answer=Conversion for meters to miles
elif unit=m and target=km:
    #answer=Conversion for meters to kilometers
elif unit=m and target=ft:
    #answer=Conversion for meters to feet
else:
    print("Your response is invalid. How dare you. Goodbye.")
    quit()
print("I have finished the math. Your final answer is: ",answer)
