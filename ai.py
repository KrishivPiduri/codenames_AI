# guesser.py

from game import Board
import gensim.downloader as api

# Global variable to cache the model
_model = None

def get_model():
    """Load and cache the word vector model"""
    global _model
    if _model is None:
        print("Loading word vectors...")
        _model = api.load('glove-wiki-gigaword-100')
        print("Loaded.")
    return _model


def cosine_similarity(word1, word2):
    model = get_model()
    return model.similarity(word1, word2)


def guess_words(clue, number, board):
    clue = clue.lower()
    unrevealed = [c for c in board.cards if not c.revealed]

    scores = []
    for card in unrevealed:
        try:
            sim = cosine_similarity(clue, card.word.lower())
            scores.append((card.word, sim))
        except KeyError:
            continue  # skip OOV words

    scores.sort(key=lambda x: x[1], reverse=True)
    top_guesses = [word for word, _ in scores[:number]]
    return top_guesses


# ---- Example usage ----

if __name__ == "__main__":
    word_list = [
        'apple', 'moon', 'war', 'code', 'tree', 'bank', 'virus', 'glass',
        'star', 'car', 'cloud', 'train', 'ship', 'map', 'whale', 'paper',
        'space', 'ring', 'crown', 'ghost', 'robot', 'light', 'sound', 'king', 'bomb'
    ]

    board = Board(word_list, starting_team='Red')
    board.display_spymaster_board()
    # Try your own clue and number here:
    clue = input("Enter your clue: ")
    number = int(input("Enter your number: "))

    guesses = guess_words(clue, number, board)
    print(f"Clue: {clue} ({number})")
    print("AI guesses:", guesses)
