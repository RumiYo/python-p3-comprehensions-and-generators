#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0 ]
    return even_numbers

def make_exclamation(sentence_list):
    add_exclamation = (n + "!" for n in sentence_list )
    sentence_exclamation = list()
    for m in add_exclamation:
        sentence_exclamation.append(m)
    return sentence_exclamation 