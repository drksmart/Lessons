alist = [3,5,12,-2,17,-52,7080]

def max_test(number_list):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value


print(max_test(alist))


