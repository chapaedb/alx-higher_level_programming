#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("Division by zero")
            division = 0
        except TypeError:
            print("Wrong type")
            division = 0
        except IndexError:
            print("Index out of range")
            division = 0
        finally:
            result_list.append(division)
    return result_list
