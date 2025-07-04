import random

def generate_board(words, starting_team):
    selected = random.sample(words, 25)
    roles = []
    if starting_team == 'Red':
        roles = ['Red'] * 9 + ['Blue'] * 8
    else:
        roles = ['Blue'] * 9 + ['Red'] * 8
    roles += ['Assassin'] + ['Neutral'] * (25 - len(roles) - 1)
    random.shuffle(roles)
    board = [{'word': w, 'role': r, 'revealed': False} for w, r in zip(selected, roles)]
    return board

def display_board(board):
    for i, card in enumerate(board):
        if card['revealed']:
            r = card['role'][0]
            print(f"[{r}:{card['word']:^10}]", end=' ')
        else:
            print(f"[ {card['word']:^10} ]", end=' ')
        if (i + 1) % 5 == 0:
            print()

def display_spymaster_board(board):
    print("\nSpymaster view (roles revealed):")
    for i, card in enumerate(board):
        symbol = card['role'][0]
        print(f"[{symbol}:{card['word']:^10}]", end=' ')
        if (i + 1) % 5 == 0:
            print()
    print()

def check_win(board):
    red_left = sum(1 for c in board if c['role'] == 'Red' and not c['revealed'])
    blue_left = sum(1 for c in board if c['role'] == 'Blue' and not c['revealed'])
    if red_left == 0:
        return 'Red'
    if blue_left == 0:
        return 'Blue'
    return None

def main():
    WORDS = [
        'Apple','Ball','Cat','Dog','Eagle','Fish','Ghost','Horse','Igloo','Joker',
        'Kangaroo','Lion','Mountain','Night','Ocean','Pumpkin','Queen','Robot','Sun','Tiger',
        'Umbrella','Violin','Whale','Xylophone','Yacht','Zebra','Anchor','Bridge','Castle','Diamond',
        'Engine','Forest','Garden','Helmet','Island','Jungle','King','Lemon','Mirror','Neptune',
        'Octopus','Pyramid','Quartz','Rainbow','Satellite','Temple','Universe','Volcano','Window','Yogurt'
    ]
    starting = random.choice(['Red', 'Blue'])
    board = generate_board(WORDS, starting)
    current = starting
    print(f"{starting} team starts with {'9' if starting == 'Red' else '8'} agents.")

    while True:
        print("\nBoard state:")
        display_board(board)
        display_spymaster_board(board)
        winner = check_win(board)
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
            match = next((c for c in board if c['word'].lower() == guess.lower() and not c['revealed']), None)
            if not match:
                print("Invalid guess or already revealed, try again.")
                continue
            match['revealed'] = True
            print(f"Revealed {match.get('word')}: {match.get('role')}")
            if match.get('role') == 'Assassin':
                print(f"Assassin found! {current} team loses. Game over.")
                return
            if match.get('role') != current:
                print("Turn ends.")
                break
            guesses += 1
        current = 'Blue' if current == 'Red' else 'Red'

if __name__ == '__main__':
    main()
