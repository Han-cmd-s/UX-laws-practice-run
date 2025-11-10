import random
import sys
import re

from graphics import HANGMAN_UI
from language import DICTIONARY

# Colors for terminal
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# Ask language
language = input(f"{DICTIONARY['en']['msgLanguageChoice']}\n\n{DICTIONARY['no']['msgLanguageChoice']}\n> ").strip().lower()
if language not in DICTIONARY:  # Default to English
    language = "en"

# Read word list
list_of_words = DICTIONARY[language]['wordList']
with open(list_of_words, 'r', encoding='utf-8') as f:
    all_words = [w.strip() for w in f.read().splitlines() if w.strip()]

# Pick a random word
word = random.choice(all_words).lower()
letters_in_word = list(word)

# Helpers
def pull_randomly_from_list(list):
    return random.choice(list)

# Make visual
def make_visual_from_word(word):
    return ["_"] * len(word)


# Reset game
mistake = []  # List of wrong guesses
correct = []  # List of correct guesses
stat_trackers = []  # Track number of guesses per round
rounds_played = 0
total_guesses = 0