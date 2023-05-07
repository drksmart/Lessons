def average(x):
    a = sum(x)
    b = len(x)
    return a/b


base = [int(number) for number in input('Give me a list of numbers to average: ').split()]

print(average(base))