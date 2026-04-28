#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = max(len(my_list_1), len(my_list_2))
    newlist = []
    for i in range(length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("Wrong type")
            newlist.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        except IndexError:
            print("out of range")
            newlist.append(0)
        finally:
            pass
    return newlist
