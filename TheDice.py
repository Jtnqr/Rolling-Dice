import random

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

def roll_dice(count):
    dice_total = dice_random = 0
    dice_display = ""
    for i in range(count):
        dice_random = int(random.randint(1,6))
        dice_total += dice_random
        dice_display += "[" + str(dice_random) + "]"

    print("Dice is rolled! " + dice_display)
    print("Total number on Dice is " + str(dice_total) + "\n")

greetings = "Welcome to The Dice Rolling Simulator!"
print(greetings + "\n" + "=" * len(greetings))

dice_count = int(input("How many dice? "))
roll_dice(dice_count)

while True:
    roll_again = input("Roll again?[y/n/c] ").lower()

    if roll_again in yes:
        roll_dice(dice_count)
    elif roll_again in no:
        break
    elif roll_again == 'c':
        dice_count = int(input("How many dice? "))
        roll_dice(dice_count)
    else:
        print("Choices are (y)es/(n)o/(c)hange\n")
