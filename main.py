import random
import string

words = ("apple", "orange", "banana", "plum", "berry")

# Dictionary of hangman art
hangman_art = {0: ("        ",
                   "        ",
                   "        "),
               1: ("   O    "
                   "   |    "
                   "   |    "),
               2: ("   |    ",
                   "   O    "),
               3: ("   |    ",
                   "   O    ",
                   "   |    "),
               4: ("   |    ",
                   "   O    ",
                   "  /|    "),
               5: ("   |    ",
                   "   O    ",
                   "  /|\\   "),
               6: ("   |    ",
                   "   O    ",
                   "  /|\\   ",
                   "  /      ")}


def display_nam(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        print(hint)

if __name__ == "__main__":
    main()
