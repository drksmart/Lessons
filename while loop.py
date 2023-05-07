number_list = []

def find_average(number_list):
    return sum(number_list)/len(number_list)

go_on = True

while go_on:
    number = float(input('Number, please: '))

    if number == 0.0:
        go_on = False
    else:
        number_list.append(number)

x = find_average(number_list)
print(x)