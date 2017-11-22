import random
input("\nPress enter to encounter an enemy.\n")
def villain():
    enemyNumber = random.randint(0,3)
    enemy = ["Someone who believes in more than 3 Fire Emblem™ games","Ness from Undertale 2","A h*ck","A writer for The Emoji Movie"]

    print(enemy[enemyNumber], "appears!\n")

villain()
