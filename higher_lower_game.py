import random
from game_data import data


def get_random_entry(exclude=None):
    """Get a random entry from data, optionally excluding one."""
    available = [entry for entry in data if entry != exclude]
    return random.choice(available)


def format_entry(label, entry):
    """Format an entry for display."""
    return f"Compare {label}: {entry['name']}, a {entry['description']}, from {entry['country']}"


def play_game():
    """Main game loop."""
    score = 0
    compare_a = get_random_entry()

    while True:
        compare_b = get_random_entry(exclude=compare_a)

        print(format_entry("A", compare_a))
        print(format_entry("B", compare_b))

        guess = input("\nIs Compare B's follower count higher or lower than Compare A? (h/l): ").lower()

        while guess not in ['h', 'l']:
            guess = input("Please enter 'h' for higher or 'l' for lower: ").lower()

        b_is_higher = compare_b['follower_count'] > compare_a['follower_count']

        if (guess == 'h' and b_is_higher) or (guess == 'l' and not b_is_higher):
            score += 1
            print(f"\nCorrect! Your score is {score}\n")
            compare_a = compare_b
        else:
            print(f"\nWrong! {compare_b['name']} has {compare_b['follower_count']}M followers.")
            print(f"{compare_a['name']} has {compare_a['follower_count']}M followers.")
            print(f"\nGame Over! Your final score is {score}")
            break


if __name__ == "__main__":
    print("Welcome to the Higher Lower Game!\n")
    play_game()
