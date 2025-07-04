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
    return [{'word': w, 'role': r, 'revealed': False} for w, r in zip(selected, roles)]

def check_win(board):
    red_left = sum(1 for c in board if c['role'] == 'Red' and not c['revealed'])
    blue_left = sum(1 for c in board if c['role'] == 'Blue' and not c['revealed'])
    if red_left == 0:
        return 'Red'
    if blue_left == 0:
        return 'Blue'
    return None

def reveal_card(board, guess_word):
    for card in board:
        if card['word'].lower() == guess_word.lower():
            if card['revealed']:
                raise ValueError('Card already revealed')
            card['revealed'] = True
            return card['role']
    raise ValueError('Invalid guess')
