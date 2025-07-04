import random

class Card:
    def __init__(self, word, role):
        self.word = word
        self.role = role
        self.revealed = False

class Board:
    def __init__(self, words, starting_team):
        selected = random.sample(words, 25)
        if starting_team == 'Red':
            roles = ['Red'] * 9 + ['Blue'] * 8
        else:
            roles = ['Blue'] * 9 + ['Red'] * 8
        roles += ['Assassin'] + ['Neutral'] * (25 - len(roles) - 1)
        random.shuffle(roles)
        self.cards = [Card(w, r) for w, r in zip(selected, roles)]

    def display_board(self):
        for i, card in enumerate(self.cards):
            if card.revealed:
                r = card.role[0]
                print(f"[{r}:{card.word:^10}]", end=' ')
            else:
                print(f"[ {card.word:^10} ]", end=' ')
            if (i + 1) % 5 == 0:
                print()

    def display_spymaster_board(self):
        print("\nSpymaster view (roles revealed):")
        for i, card in enumerate(self.cards):
            symbol = card.role[0]
            print(f"[{symbol}:{card.word:^10}]", end=' ')
            if (i + 1) % 5 == 0:
                print()
        print()

    def reveal_card(self, guess_word):
        for card in self.cards:
            if card.word.lower() == guess_word.lower():
                if card.revealed:
                    raise ValueError('Card already revealed')
                card.revealed = True
                return card.role
        raise ValueError('Invalid guess')

    def check_win(self):
        red_left = sum(1 for c in self.cards if c.role == 'Red' and not c.revealed)
        blue_left = sum(1 for c in self.cards if c.role == 'Blue' and not c.revealed)
        if red_left == 0:
            return 'Red'
        if blue_left == 0:
            return 'Blue'
        return None
