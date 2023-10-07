# The goal of this file is to count, for every config, how many hands it has

from cst import NB_NUMS, NB_SUITS, TOTAL_NB_HANDS
from math import comb
from genlib import rational_description as rdesc
import configslib


def print_configs_with_probs():
    configs = configslib.generate_configs()
    total_count = comb(NB_NUMS * NB_SUITS, NB_NUMS)
    total_count_debug = 0

    for config in configs:
        amount = configslib.count(config)
        print("{0}: {1}".format(config, rdesc(amount, TOTAL_NB_HANDS)))
        total_count_debug = total_count_debug + amount

    if total_count_debug == total_count:
        print("Count of all configs successfully calculated.")
    else:
        print("Warning: total count does not match.")


print_configs_with_probs()
