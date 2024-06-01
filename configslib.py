# The config of a hand is an array of int containing the number of cards of each suit in the hand.
# The array is sorted in descending order.

from math import comb, factorial as fact

from cst import NB_NUMS, NB_SUITS


def generate_configs(nb_cards=NB_NUMS,
                     nb_suits=NB_SUITS,
                     previous_value=NB_NUMS):
    if nb_cards == 0:
        return [[]]
    next_nb_cards_min = ((nb_cards - 1) // nb_suits) + 1
    next_nb_cards_max = nb_cards
    if next_nb_cards_max > previous_value:
        next_nb_cards_max = previous_value
    res = []
    for i in range(next_nb_cards_min, next_nb_cards_max + 1):
        sub_lists = generate_configs(nb_cards - i, nb_suits - 1, i)
        for sub_list in sub_lists:
            sub_list.insert(0, i)
            res.append(sub_list)
    return res


def nb_color_distributions(config):
    res = fact(NB_SUITS)
    idem_streak = 1
    idx = 0
    while idx < len(config) - 1:
        if config[idx] == config[idx + 1]:
            idem_streak = idem_streak + 1
        else:
            res = res // fact(idem_streak)
            idem_streak = 1
        idx = idx + 1
    res = res // fact(idem_streak) // fact(NB_SUITS - len(config))
    return res


def count(config):
    # Step 1: count the number of ways to match the colors to the config's values.
    res = nb_color_distributions(config)

    # Step 2: multiply by the number of ways to choose the combination of numerals for each color
    for i in config:
        res = res * comb(NB_NUMS, i)
    return res
