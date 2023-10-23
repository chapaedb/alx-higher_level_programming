#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                raise TypeError("wrong type")
            if element_2 == 0:
                raise ZeroDivisionError("division by 0")
            result.append(element_1 / element_2)
        except IndexError as e:
            print(e)
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
