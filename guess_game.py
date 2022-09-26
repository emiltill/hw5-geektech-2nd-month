import random
from decouple import config


def casino():
    my_money = config("MY_MONEY", cast=int)
    balance = my_money
    while True:
        my_num = input("Choose any number between 1 and 30: ")
        try:
            my_num = int(my_num)
            if my_num not in range(1, 31):
                print("You entered the number which is not suitable!")
                continue
        except ValueError:
            print("Please enter only integers")
            continue

        my_bet = input("Make your bet: ")
        try:
            my_bet = int(my_bet)
            if my_bet > balance:
                print(f'Your bet greater than your available balance: {balance}!')
                continue
        except ValueError:
            print("Please enter only integers")
            continue
        slot = random.randint(1, 31)
        if slot == my_num:
            my_cash = my_bet * 2
            balance += my_cash
        else:
            balance -= my_bet
        play_again = input("Would you like to play again, y/n? ")
        if play_again.lower() == 'n':
            print("Your balance: ", balance)
            break
        elif play_again.lower() == 'y':
            continue


if __name__ == '__main__':
    casino()





