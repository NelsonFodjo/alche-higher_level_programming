#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary.values())



a_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

print(best_score(a_dictionary))