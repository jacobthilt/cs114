print("Please enter the amount of change you would like to dispense in cents")
user=int(input())
dollars=user//100
user=user-dollars*100
quarters=user//25
user=user-quarters*25
dimes=user//10
user=user-dimes*10
nickels=user//5
user=user-nickels*5
pennies=user-0
print("Dollars: ", dollars)
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)
