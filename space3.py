import random
magic=50
attack=50

input("\nA Todd dummy appears! Press enter to start.\n")

def action(Fmagic, Fattack, decision):
    if decision=='m':
        #while Fmagic>0 and decision=='m':
        randomNumber=random.randint(1, 25)
        print("You use ",randomNumber,"Fmagic points on yourself.")
        Fmagic= Fmagic-randomNumber
        if Fmagic<=0:
            Fmagic=0
        print("\nAttack: ",Fattack,"\nMagic: ",Fmagic,"\n")
    elif decision=='a':
        #while Fattack>0 and decision=='a':
        randomNumber=random.randint(1, 25)
        print("You attack the dummy.")
        Fattack=Fattack-randomNumber
        print("You lose",randomNumber,"attack points.")
        if Fattack<=0:
            Fattack=0
        print("\nAttack: ",Fattack,"\nMagic: ",Fmagic,"\n")
    else:
        print("\nThat choice is invalid. \nAttack: 0\nMagic:0\n\nYou have died.")
        quit()

def main():
    while magic>0 or attack>0:
        choice=str(input("Enter 'm' to use magic or 'a' to attack: "))
        action(magic, attack, choice)

    print("You have completely run out of magic AND attack. Ya dork.")

main()
