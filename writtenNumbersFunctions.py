print("Written numbers.")
print("Enter your number between 1 and 99")
user=int(input())

ones = user % 10
tens = user // 10
num2=''
num1=''
if tens<2: #Go to teens/single digits
    if tens<1:
        if ones==0:
            num1='Zero'
        elif ones==1:
            num1='One'
        elif ones==2:
            num1='Two'
        elif ones==3:
            num1='Three'
        elif ones==4:
            num1='Four'
        elif ones==5:
            num1='Five'
        elif ones==6:
            num1='Six'
        elif ones==7:
            num1='Seven'
        elif ones==8:
            num1='Eight'
        elif ones==9:
            num1='Nine'
    else: #Go to teens
        if ones==0:
            num1='Ten'
        elif ones==1:
            num1='Eleven'
        elif ones==2:
            num1='Twelve'
        elif ones==3:
            num1='Thirteen'
        elif ones==4:
            num1='Fourteen'
        elif ones==5:
            num1='Fifteen'
        elif ones==6:
            num1='Sixteen'
        elif ones==7:
            num1='Seventeen'
        elif ones==8:
            num1='Eighteen'
        elif ones==9:
            num1='Nineteen'
elif tens>=2 and tens<=9: #Go to twenties and higher
    if tens==2:
        num2='Twenty'
    elif tens==3:
        num2='Thirty'
    elif tens==4:
        num2='Fourty'
    elif tens==5:
        num2='Fifty'
    elif tens==6:
        num2='Sixty'
    elif tens==7:
        num2='Seventy'
    elif tens==8:
        num2='Eighty'
    elif tens==9:
        num2='Ninety'
    if ones==1:
        print("one")
    elif ones==2:
        print("two")
    elif ones==3:
        num1='three'
    elif ones==4:
        num1='four'
    elif ones==5:
        num1='five'
    elif ones==6:
        num1='six'
    elif ones==7:
        num1='seven'
    elif ones==8:
        num1='eight'
    elif ones==9:
        num1='nine'

else:
    print("\n\nNot a valid number. Goodbye.\n\n")
    quit()


print("\n\nYour number in written form is: ",num2,num1,"\n\n")
