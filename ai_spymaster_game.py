import random
from game import Board

# same word list
WORDS = [
    'Apple','Ball','Cat','Dog','Eagle','Fish','Ghost','Horse','Igloo','Joker',
    'Kangaroo','Lion','Mountain','Night','Ocean','Pumpkin','Queen','Robot','Sun','Tiger',
    'Umbrella','Violin','Whale','Xylophone','Yacht','Zebra','Anchor','Bridge','Castle','Diamond',
    'Engine','Forest','Garden','Helmet','Island','Jungle','King','Lemon','Mirror','Neptune',
    'Octopus','Pyramid','Quartz','Rainbow','Satellite','Temple','Universe','Volcano','Window','Yogurt'
]

class AIPlayer:
    def __init__(self, team):
        self.team = team

    def give_clue(self, board):
        # pick an unrevealed agent word as clue with number 1
        choices = [c.word for c in board.cards if c.role == self.team and not c.revealed]
        if not choices:
            return None, 0
        return choices[0], 1

def main():
    starting = random.choice(['Red', 'Blue'])
    board = Board(WORDS, starting)
    current = starting
    ai_players = {'Red': AIPlayer('Red'), 'Blue': AIPlayer('Blue')}

    print(f"{starting} team starts and AI spymasters will give clues. You guess cards.")

    while True:
        print("\nCurrent board:")
        board.display_board()()
        # check win
        win = board.check_win()
        if win:
            print(f"Team {win} has won!")
            break
        # AI gives clue
        clue, number = ai_players[current].give_clue(board)
        if not clue:
            print(f"No more clues for {current}.")
            break
        print(f"{current} clue: {clue} {number}")
        guesses = 0
        max_guesses = number + 1
        while guesses < max_guesses:
            guess = input(f"Guess {guesses+1}/{max_guesses} or 'stop': ").strip()
            if guess.lower() == 'stop':
                print("Turn ended by player.")
                break
            try:
                role = board.reveal_card(guess)
            except ValueError:
                print("Invalid guess or already revealed.")
                continue
            print(f"Revealed {guess}: {role}")
            display_board(board)
            if role == 'Assassin':
                print(f"Assassin! {current} loses.")
                return
            if role != current:
                print("Incorrect team, turn ends.")
                break
            guesses += 1
        # switch teams
        current = 'Blue' if current == 'Red' else 'Red'

if __name__ == '__main__':
    main()
