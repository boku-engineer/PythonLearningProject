import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculate score, adjusting aces from 11 to 1 if needed."""
    score = sum(hand)
    # Convert aces from 11 to 1 if busting
    aces = hand.count(11)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def is_blackjack(hand):
    """Check for natural blackjack (21 with 2 cards)."""
    return len(hand) == 2 and calculate_score(hand) == 21

def play_game():
    """The main game loop."""
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Check for natural blackjack
    if is_blackjack(user_cards):
        print("Blackjack! You win!")
        return

    # Player's turn - hit until stand or bust
    while calculate_score(user_cards) < 21:
        choice = input("\nType 'y' to hit, 'n' to stand: ").lower()
        if choice == 'y':
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, score: {calculate_score(user_cards)}")
        else:
            break

    user_score = calculate_score(user_cards)

    # Check if player busted
    if user_score > 21:
        print(f"Your final hand: {user_cards}, score: {user_score}")
        print("Bust! You lose!")
        return

    # Dealer's turn - must hit on 16 or less, stand on 17+
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)
    print(f"\nYour final hand: {user_cards}, score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, score: {computer_score}")

    # Determine winner
    if computer_score > 21:
        print("Computer busts! You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("It's a push (tie)!")
    else:
        print("You lose!")

while True:
    if input("\nDo you want to play a game? [y/n]: ").lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")
        break
