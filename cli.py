import random
from game import Board

WORDS = [
    'Apple','Ball','Cat','Dog','Eagle','Fish','Ghost','Horse','Igloo','Joker',
    'Kangaroo','Lion','Mountain','Night','Ocean','Pumpkin','Queen','Robot','Sun','Tiger',
    'Umbrella','Violin','Whale','Xylophone','Yacht','Zebra','Anchor','Bridge','Castle','Diamond',
    'Engine','Forest','Garden','Helmet','Island','Jungle','King','Lemon','Mirror','Neptune',
    'Octopus','Pyramid','Quartz','Rainbow','Satellite','Temple','Universe','Volcano','Window','Yogurt'
]


def main():
    starting = random.choice(['Red', 'Blue'])
    board = Board(WORDS, starting)
    current = starting
    print(f"{starting} team starts with {'9' if starting == 'Red' else '8'} agents.")

    while True:
        print("\nBoard state:")
        board.display_board()
        display_spymaster_board(board)
        winner = board.check_win()
        if winner:
            print(f"{winner} team has found all their agents and wins!")
            break
        print(f"{current} team's turn.")
        clue_input = input("Spymaster, enter your clue and number (e.g., 'animal 2'): ").split()
        if len(clue_input) < 2 or not clue_input[-1].isdigit():
            print("Invalid clue format, try again.")
            continue
        clue_number = int(clue_input[-1])
        max_guesses = clue_number + 1
        guesses = 0
        while guesses < max_guesses:
            guess = input(f"Guess {guesses + 1}/{max_guesses} (or 'stop'): ").strip()
            if guess.lower() == 'stop':
                break
            try:
                role = board.reveal_card(guess)
            except ValueError as e:
                print(str(e))
                continue
            print(f"Revealed {guess}: {role}")
            if role == 'Assassin':
                print(f"Assassin found! {current} team loses. Game over.")
                return
            if role != current:
                print("Turn ends.")
                break
            guesses += 1
        current = 'Blue' if current == 'Red' else 'Red'

if __name__ == '__main__':
    main()
