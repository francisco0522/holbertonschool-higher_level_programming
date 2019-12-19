#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = max(a_dictionary.value())
        return[i for i, num in a_dictionary.items() if num == val][0]
