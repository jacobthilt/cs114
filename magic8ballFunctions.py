import random
def fortunes(number):
    if number==1:
        return'\nYou will go insane and become a rabid Jake Pauler.\n'
    elif number==2:
        return'\nYou will be awestruck at the end of Undertale 2 when it turns out Ness was Link from Sonic: Odyssey all along.\n'
    elif number==3:
        return'\nYou will become the number one killer of people who believe there are more than 3 Fire Emblem™ games.\nThis is the best fate possible.\n'
    elif number==4:
        return'\nYou will one day legitimately think only people with high intelligence can understand Rick and Morty.\nWhy are you like this?\n'
    elif number==5:
        return'\nYou will buy a virtual reality headset but then game developers \nwill not make games for it and you will be left with a useless gadget.\nRip in pasta.\n'
    elif number==6:
        return'\nYou will drink the water Alex Jones is worried about and reverse your sexuality.\n'
    elif number==7:
        return'\nYou will punch someone for liking Meghan Trainor with no legal repercussions. \nThis is the 2nd best outcome.\n'
    elif number==8:
        return'\nYou will encounter Lady Evil in South Carolina.\n'
    elif number==9:
        return'\nYou will get cancer. Not the disease, I just mean youll buy the Emoji Movie.\n'
def main():
    print("This world is full of possibilities. User, give me your name.\nI shall tell you your fate.")
    name=str(input())
    numberMain=random.randint(1, 9)
    future = fortunes(numberMain)
    print(future)
    print("\nThis is your fate "+name+". Do not try to change it. \nOnly catastrophe will follow.\n")

main()
