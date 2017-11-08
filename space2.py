import random
magic=50
attack=50
i=5

input("\nA Todd dummy appears! Press enter to start.\n")
choice=str(input("Enter 'm' to use magic or 'a' to attack: "))
while magic>0 or attack>0:
    if choice=='m':
        while magic>0 and choice=='m':
            randomNumber=random.randint(1, 25)
            print("You use ",randomNumber,"magic points on yourself.")
            magic= magic-randomNumber
            if magic<=0:
                magic=0
            print("\nAttack: ",attack,"\nMagic: ",magic)
            choice=str(input("Enter 'm' to use magic or 'a' to attack: "))
            print("\n")
    elif choice=='a':
        for i in range(5):
            randomNumber=random.randint(1, 25)
            print("You attack the dummy.")
            attack=attack-randomNumber
            print("You lose",randomNumber,"attack points.")
            if attack<=0:
                attack=0
            print("\nAttack: ",attack,"\nMagic: ",magic)
            i=i-1
            choice=str(input("Enter 'm' to use magic or 'a' to attack: "))
            print("\n")
    else:
        print("That choice is invalid. \nAttack: 0\nMagic:0\n\nYou have died: ")
        quit()


print("You have completely run out of magic AND attack. Ya dork.")
