import random


def ask_for_bet():
    count = 0
    while True:
        try:
            message = "Place your bet for the next round: " if not count else "The bet has to be an integer number. Please try again: "
            bet = int(input(message))
            break
        except ValueError:
            count += 1
            continue
    return bet


def deal_cards():
    """
    :return
    User's card, Computer's card
    """
    valid_cards = range(1, 13)
    return random.choice(valid_cards), random.choice(valid_cards)


def ask_for_next_step():
    options = """
        1. Play another round
        2. Leave with my money :-)
    """
    next_step = input(f'What would you like to do?{options}\n')
    while not next_step.isdigit():
        next_step = input(f'Please enter a valid option: {options}')
    return next_step


def main():
    slashes = ("/" * 8)
    backslashes = ("\\" * 8)
    deal_cards
    dashes = ('-' * 11)
    print(f"{slashes}{dashes} Welcome to WAR {dashes}{backslashes}")
    name = input("Please enter your name: ")
    money = 50
    print(f"Hello {name}! You currently have {money} ILS")

    while True:
        bet = ask_for_bet()
        if bet > money or bet < 1:
            print(f"I said between 1 and {money} but you typed {bet}")
            print(f"I don't play with liars!!! Bye {name}, see you never.")
            break

        user_card, computer_card = deal_cards()
        print(f"Your card is {user_card} and mine is {computer_card}")
        if user_card > computer_card:
            money += bet
            print(f"You won {bet} and now you have {money}")
        else:
            money -= bet
            print(f"You lost {bet} and now you have {max(money, 0)}")

        if money < 1:
            print("You're broke... Nice to meet you, bye bye")
            break

        next_step = ask_for_next_step()
        if int(next_step) == 2:
            print(f"Good choice... You left with {money}")
            break


main()
