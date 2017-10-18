print("You've been in space for one week now. Everything was running as planned.\n")
print("Suddenly, you hear a loud booming sound from inside the ship... \nthis is where your adventure truly begins")
print("You still have contact to command center, at least for now. \nYou hear a voice through the intercom\n'Hey, uh, there seems to be an unknown problem. Could you remind me which pilot you are? You're not the only ship up there right now so it gets confusing.")
name=str(input())
print("Okay, thank you ",name," now please remind us, \nwhat is the power level of your attack and magic?\nDon't play any tricks on us, we know they have to add up to 100.\n")
print("\nEnter your attack power")
attack=int(input())
magic=100-attack
if magic < 0:
    print("The voice speaks: You have lied... \nThis is why we were suspicious of you and stopped your ship.\nNow,")
    input()
    print("DIIIIIIIIIEEEEEEEE!!!!!")
    print("You are a traitor. Missiles fly toward your ship. \nThe last thing you see is a missile hitting your windshield.")
    print("\nGAME OVER\n\n")
    quit()
else:
    print("Your attack power is ",attack,"Your magic power is ",magic,".")
    #print("...You are in our database.\nWhat are you?")
    #print("I guess my plan failed. I will be arrested as soon as they hear these recordings.\nBut it will be worth it.")
    #print("\n\n\nTodd teleports into your ship. 'I will defeat you for master alien guy.'\n\n")
    #input()
    #yourHealth=1000
    #toddHealth=1000
    #if toddHealth>0 and yourHealth>0:
#        print("Your health: ",yourHealth,"\nTodd's Health: ",toddHealth)
#        print("\n1: Attack\n2: Use Magic")
#        import random
#        print random.random()
#    elif toddHealth<=0:
#        print("Todd is defeated. H*ck Todd.")
#        print("Y O U  W I N !")
#        print("A new voice comes over the intercom: 'Hello ",name" are you alright?!\nThis is the REAL mission command Todd. A fake alien Todd KO'd me and took over.\nI'll reboot your spaceship now.")
#        print("The end.")
#    elif yourHealth<=0:
#        print("You have died.\n\nGAME OVER\n\n")
#        quit()
#    else:
#        print("You defeated Todd as he defeated you. In your dying breath, you saved earth.\n\n\nGAME OVER\n\n\n")
