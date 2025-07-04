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
