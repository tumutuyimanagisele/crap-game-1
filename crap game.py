 # Gisele Tumutuyimana
 # 10/23/2019
 # Crap game
import random
# this is the game of crap the player will bet the amount they want

print("Hey there !what is your name ?")
name = (input())



def pre_game():
    print(" would you like to play?")
    print(" choose 0 if want to play or 1 if want to quit ")
    play = int(input())

    if play==0:
        print("Cool! LET's go!")

    elif play==1:
        print("okay! have a good one!")
        exit()

pre_game()
# im going to ask the player their bankroll amount and how much they would like to bet and fromthat they will roll the dice

def play_game():

    print(" what is your bankroll AMOUNT?")
    bank = int(input())
    while bank <= 0:
        print(" you cant play with that amount ,try again ")
        bank=input()
        pre_game()

    print(f" how much would you like to  bet  from your  ${bank} this round?")
    bet= int(input())

    while bet <= 0:
        print("too low! try again.")
        bet = int(input())
        pre_game()

    while bet > bank:
        print("you bet too high than your bank roll, try again! ")
        pre_game()



    while bank > 0 and bet > 0:
        roll=random.randint(1,6)
        roll2=random.randint(1,6)
        roll_total=roll+roll2

        print(f" you have rolled a {roll}")
        print(f" you have rolled a {roll2}")
        print(f" you have rolled a {roll_total}")



        if roll_total==7 or roll_total==11:
            print(" you won!")
            bank= bank + bet
            print(f"your current amount is ${bank}")
            exit()


        elif roll_total==2 or roll_total==3 or roll_total==12:
            print("you lost!")

            bank= bank-bet
            print(f" your current amount is ${bank}")
            pre_game()

        else:
            new_roll = random.randint(1,6)
            new_roll2 = random.randint(1,6)
            new_roll_total = new_roll +  new_roll2

            while roll != new_roll_total and new_roll_total != 7:
                print(f"You have rolled a {new_roll}, we'll keep going.")
                bank = bank - bet
                print(f"your current amount is {bank}")



            if new_roll_total == roll:
                print(f"You got {new_roll_total}!")
                print("you won!")
                pre_game()

            elif new_roll_total == 7:
                print("You lost !")
                pre_game()

play_game()
