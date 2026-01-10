import random

self = int(input("Rock(1), Paper(2), Scissors(3) ?"))
computer = random.randint(1,3)
computer_gesture = [1,2,3]
computer_pick = int(random.choice(computer_gesture))

if computer_pick == 1:
    print("Computer: Rock")
elif computer_pick == 2:
    print("Computer: Paper")
else:
    print("Computer: Scissors")

announcement = ""

if self == computer_pick:
    announcement = "It's a draw!"
else:
    if (self == 1 and computer_pick == 3) or (self == 2 and computer_pick == 1) or (self == 3 and computer_pick == 2):
        announcement = "You win!"
    else:
        announcement = "You lose!"

print(announcement)