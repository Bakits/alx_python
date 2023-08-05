#!/usr/bin/python3
def best_score(b_dictionary):
    if not b_dictionary:
        return None

    return max(b_dictionary, key=b_dictionary.get)
