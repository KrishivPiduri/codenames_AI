import pytest
import random
from game import Board, Card

# Use a fixed set of words for deterministic tests
TEST_WORDS = [f"w{i}" for i in range(30)]

@pytest.fixture(autouse=True)
def fixed_seed():
    random.seed(42)

@pytest.mark.parametrize('starting_team, red_count, blue_count', [
    ('Red', 9, 8),
    ('Blue', 8, 9),
])
def test_board_distribution(starting_team, red_count, blue_count):
    board = Board(TEST_WORDS, starting_team)
    roles = [card.role for card in board.cards]
    assert len(board.cards) == 25
    assert roles.count('Red') == red_count
    assert roles.count('Blue') == blue_count
    assert roles.count('Assassin') == 1
    assert roles.count('Neutral') == 25 - red_count - blue_count - 1

def test_reveal_and_double_reveal():
    board = Board(TEST_WORDS, 'Red')
    card = board.cards[0]
    role = board.reveal_card(card.word)
    assert role == card.role
    assert card.revealed
    # revealing again should raise
    with pytest.raises(ValueError):
        board.reveal_card(card.word)

def test_invalid_reveal():
    board = Board(TEST_WORDS, 'Red')
    with pytest.raises(ValueError):
        board.reveal_card('not_on_board')

def test_check_win_red():
    board = Board(TEST_WORDS, 'Red')
    # Reveal all red cards
    for card in list(board.cards):
        if card.role == 'Red':
            board.reveal_card(card.word)
    assert board.check_win() == 'Red'

def test_check_win_blue():
    board = Board(TEST_WORDS, 'Blue')
    # Reveal all blue cards
    for card in list(board.cards):
        if card.role == 'Blue':
            board.reveal_card(card.word)
    assert board.check_win() == 'Blue'

def test_no_win_initially():
    board = Board(TEST_WORDS, 'Red')
    assert board.check_win() is None

