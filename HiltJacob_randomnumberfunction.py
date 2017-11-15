import random #Imports random library
def randomWord(word): #Creates function
    print("Henlo user. Plz enter yuor random word.") #Asks user for input
    word= input() #Gets user input
    num2=len(word) #Creates variable 'num2' and sets it equal to length of user input
    result=random.randint(0, num2) #Creates variable 'result' and sets it equal to a random number, the maximum possible being num2
    print('%s' '%s' '%s' % ("Teh lenght oof yor txt iz: ",num2,".\n")) #Prints total length of user input
    return result #Returns 'result' as function value

resultFinal = randomWord('python') #Creates variable 'resultFinal' and sets it equal to function value
print('%s' '%s' '%s' %("Yur rando numb equelz: ",resultFinal,".")) #Outputs final result
