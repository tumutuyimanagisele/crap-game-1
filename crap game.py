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

    print(f" how much would you like to  bet  from your  ${bank} this round?")
    bet= int(input())

    while bet <= 0:
        print("too low! try again.")
        bet = int(input())


    while bank > 0 and bet > 0:
        roll= random.randint(2,12)

        print(f" you have rolled a {roll}")

        if roll==7 or roll==11:
            print(" you won!")
            bank= bank+ bet
            print(f"your current amount is ${bank}")
            pre_game()


        elif roll==2 or roll==3 or roll==12:
            print("you lost!")

            bank= bank-bet
            print(f" your current amount is ${bank}")
            pre_game()

        else:
            new_roll = random.randint(2,12)
            while roll != new_roll and new_roll != 7:
                print(f"You have rolled a {new_roll}, we'll keep going.")
                new_roll = random.randint(2,12)
            if new_roll == roll:
                print(f"You got {new_roll}!")
                print("you won!")
                pre_game()

            elif new_roll == 7:
                print("You lost !")
                pre_game()


play_game()
