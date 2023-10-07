from math import factorial as fact, comb

# Number of colors. It's also the number of players.
NB_SUITS = 4

# Number of cards per color. It's also the number of cards in one player's hand
NB_NUMS = 10


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


def count(config):
    # Step 1: count the number of ways to match the colors to the config's values.
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

    # Step 2: multiply by the number of ways to choose the combination of numerals for each color
    for i in config:
        res = res * comb(NB_NUMS, i)
    return res


def print_configs_with_probs():
    configs = generate_configs()
    total_count = comb(NB_NUMS * NB_SUITS, NB_NUMS)
    total_count_debug = 0

    for config in configs:
        amount = count(config)
        print("{0}: {1}/{2} = {3}".format(config, amount, total_count, amount / total_count))
        total_count_debug = total_count_debug + amount

    if total_count_debug == total_count:
        print("Count of all configs successfully calculated.")
    else:
        print("Warning: total count does not match.")


print_configs_with_probs()
