# Constants for the project

from math import comb

# Number of colors. It's also the number of players.
NB_SUITS = 4

# Number of cards per color. It's also the number of cards in one player's hand
NB_NUMS = 10

# Number of cards per color. It's also the number of cards in one player's hand
TOTAL_NB_HANDS = comb(NB_NUMS * NB_SUITS, NB_NUMS)
