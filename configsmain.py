# The goal of this file is to count, for every config, how many hands it has

import os
from math import comb

import configslib
import genlib
from cst import NB_NUMS, NB_SUITS, TOTAL_NB_HANDS
from genlib import rational_description as rdesc


def generate_wiki_array(configs, configs_counts):
    tot = sum(configs_counts)
    lines = [r'{| class="wikitable sortable"',
             f"!Répartition!!Nb possibilités!!Probabilité",
             "|-",
             f"|Total||{tot}||{1.0}"]
    for i in range(len(configs)):
        val = configs_counts[i]
        prob = val / tot
        lines.append("|-")
        lines.append(f"|{configs[i]}||{val}||{genlib.formatted_proportion(prob)}")
    lines.append("|}")

    with open("out" + os.sep + "wikitable.txt", 'w', encoding='utf-8') as f:
        f.write(lines[0])
        for i in range(1, len(lines)):
            f.write("\n" + lines[i])


def print_configs_with_probs():
    configs = configslib.generate_configs()
    total_count = comb(NB_NUMS * NB_SUITS, NB_NUMS)
    total_count_debug = 0
    configs_counts = []
    for config in configs:
        amount = configslib.count(config)
        configs_counts.append(amount)
        print("{0}: {1}".format(config, rdesc(amount, TOTAL_NB_HANDS)))
        total_count_debug = total_count_debug + amount

    if total_count_debug == total_count:
        print("Count of all configs successfully calculated.")
    else:
        print("Warning: total count does not match.")
        return
    generate_wiki_array(configs, configs_counts)


print_configs_with_probs()
