#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        new = ""
        for i in my_string:
            if i.lower() != 'c':
                new += i
        return new
