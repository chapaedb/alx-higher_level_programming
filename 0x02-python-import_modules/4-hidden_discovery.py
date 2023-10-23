#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4 as my_hidden_module

    my_hidden_names = dir(my_hidden_module)
    for my_hidden_name in my_hidden_names:
        if my_hidden_name[:2] != "__":
            print(my_hidden_name)
