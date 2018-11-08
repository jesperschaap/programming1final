import random

def monopolyworp(amnt = 0):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2

    if dice1 == dice2:
        amnt += 1;

        if amnt >= 3:
            print(str(dice1) + " + " + str(dice2) + " = (direct naar de gevangenis)");
            return;
        else:
            print(str(dice1) + " + " + str(dice2) + " = " + str(sum) + " (dubbel)");
            monopolyworp(amnt);

    else:
        print(str(dice1) + " + " + str(dice2) + " = " + str(sum) + " ");

monopolyworp()