import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(user_deck):
    """Appends a random card to the user_deck."""
    if len(user_deck) < 3:
        user_deck.append(random.choice(cards))
    return user_deck

def calculate_cards(user_deck):
    """Sum the scores of all cards in the user_deck."""
    total = 0
    if len(user_deck) > 0:
        total = sum(user_deck)
    return total

def play_game():
    """The main game loop."""
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards = deal_card(user_cards)
        computer_cards = deal_card(computer_cards)

    user_score = calculate_cards(user_cards)
    computer_score = calculate_cards(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    if input("\nType \'y\' to get another card, and \'n\' to pass [y/n]").lower() == "y":
        deal_again = True
        user_cards = deal_card(user_cards)

    if computer_score < 20:
        computer_cards = deal_card(computer_cards)

    user_score = calculate_cards(user_cards)
    computer_score = calculate_cards(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 0 and user_score <= 21:
        if user_score > computer_score:
            print("You win!")
        elif user_score == computer_score:
            print("Computer wins!")
        else:
            print("You lose!")
    else:
        print("You lose!")


playing = True
while playing:
    if input("Do you want to play a game? [y/n]").lower() == "y":
        playing = True
        play_game()
    else:
        playing = False
