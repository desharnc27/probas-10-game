# The goal of this file is to count how many hands are such that you win,
# no matter what's the other players distributions

from math import comb
from cst import NB_NUMS, NB_SUITS, TOTAL_NB_HANDS
from genlib import rational_description as rdesc
import configslib


def nb_of_blind_autowin_hands():
    res = 0
    nb_non_atout_max = NB_NUMS // 2
    for nb_non_atout in range(0, nb_non_atout_max + 1):
        # Number of ways to choose the atout : NB_SUITS

        # number of ways to choose the atout cards that don't need to be maitre since suit will be emptied before
        free_atout_ways = comb(NB_NUMS - nb_non_atout, nb_non_atout)

        # Number of ways to choose the non-atout cards
        non_atout_ways = comb(nb_non_atout + NB_SUITS - 2, nb_non_atout)

        res = res + NB_SUITS * free_atout_ways * non_atout_ways

    # remove duplicates (hands made of two identical streaks were counted twice
    # since both streak could be set as atout)
    if NB_NUMS % 2 == 0:
        res = res - comb(NB_SUITS, 2)
    return res


def nb_of_blind_autowin_hands_if_sansatout_authorized():
    # Count hands containing only maitre cards.
    res = comb(NB_NUMS + NB_SUITS - 1, NB_NUMS)

    # Add hands containting non-maitre cards, but in which these non-maitre cards
    # will surely become maitre once their suit is emptied by force
    nb_non_atout_max = (NB_NUMS - 1) // 2
    for nb_non_atout in range(0, nb_non_atout_max + 1):
        # Number of ways to choose the atout : NB_SUITS

        # Number of ways to choose the atout-cards that don't need to be maitre since suit will be emptied before
        # Note: we removed the one that contains all maitre cards, which is already counted before
        free_atout_ways = comb(NB_NUMS - nb_non_atout, nb_non_atout) - 1

        # Number of ways to choose the non-atout cards
        non_atout_ways = comb(nb_non_atout + NB_SUITS - 2, nb_non_atout)

        res = res + NB_SUITS * free_atout_ways * non_atout_ways
    return res


def verify_calculations():
    nbawh = nb_of_blind_autowin_hands()
    nbawhisa = nb_of_blind_autowin_hands_if_sansatout_authorized()
    diff = 0
    configs = configslib.generate_configs()
    for config in configs:
        if 2 * config[0] >= NB_NUMS:
            continue  # Ignore autowinnable hands with atout
        nb_color_dists = configslib.nb_color_distributions(config)
        diff = diff + nb_color_dists
    if diff + nbawh == nbawhisa:
        print("Calculations for blind-autowin work perfectly")
        return True
    else:
        print("Error: autowin calculations have some incoherence.")
        print("nb_of_blind_autowin_hands(): {0}".format(nbawh))
        print("nb_of_blind_autowin_hands_if_sansatout_authorized(): {0}".format(nbawhisa))
        print("Anticipated difference: {0}".format(nbawhisa - nbawh))
        print("Obtained difference: {0}".format(diff))
        return False


def print_autowin_configs():
    blind_autowin_hands = nb_of_blind_autowin_hands()
    print("blind_autowin_hands: " + rdesc(blind_autowin_hands, TOTAL_NB_HANDS))
    blind_autowin_hands_sansatout = nb_of_blind_autowin_hands_if_sansatout_authorized()
    print("blind_autowin_hands_sansatout: " + rdesc(blind_autowin_hands_sansatout, TOTAL_NB_HANDS))


print_autowin_configs()
verify_calculations()
