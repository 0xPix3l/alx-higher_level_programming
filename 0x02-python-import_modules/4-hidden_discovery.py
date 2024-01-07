#!/usr/bin/python3
if __name__ == "__main__":
    def new_in_list(my_list, idx, element):
        a = my_list.copy()
        a[idx] = element
        return a

