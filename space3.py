import random


input("\nA Todd dummy appears! Press enter to start.\n")

def action(magic, attack, decision):
    if decision=='m':
        #while magic>0 and decision=='m':
        randomNumber=random.randint(1, 25)
        print("You use ",randomNumber,"magic points on yourself.")
        magic= magic-randomNumber
        if magic<=0:
            magic=0
        print("\nAttack: ",attack,"\nMagic: ",magic,"\n")
    elif decision=='a':
        #while attack>0 and decision=='a':
        randomNumber=random.randint(1, 25)
        print("You attack the dummy.")
        attack=attack-randomNumber
        print("You lose",randomNumber,"attack points.")
        if attack<=0:
            attack=0
        print("\nAttack: ",attack,"\nMagic: ",magic,"\n")
    else:
        print("\nThat choice is invalid. \nAttack: 0\nMagic:0\n\nYou have died.")
        quit()

def main():
    magic=50
    attack=50
    while magic>0 or attack>0:
        choice=str(input("Enter 'm' to use magic or 'a' to attack: "))
        action(magic, attack, choice)

    print("You have completely run out of magic AND attack. Ya dork.")

main()
