age = int(input('How old are you? '))


def age_test():
    if age>=18 and age<=40:
        print('Look at what a nice adult you are!')
    elif age<18:
        print('Such a baby!!')
    else:
        print('Damn, you\'re old!')

age_test()

print('The end')