def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
def change_list(list, func):
    odd_list = []

    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

alist = range(1, 12)
print(change_list(alist, is_odd))