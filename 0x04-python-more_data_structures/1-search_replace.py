#!/usr/bin/python3

def perform_search_replace(input_list, search_term, replace_term):
    new_list = list(map(lambda x: replace_term if x == search_term else x, input_list))
    return new_list
