from termcolor import colored
import enchant
dict_ref = enchant.Dict("en_US")


answer = "butts"


def word_check(user_guess):

    pos1 = user_guess[0]==answer[0]
    pos2 = user_guess[1]==answer[1]
    pos3 = user_guess[2]==answer[2]
    pos4 = user_guess[3]==answer[3]
    pos5 = user_guess[4]==answer[4]

    answer_check=answer
    user_guess_check=user_guess

    if pos1 == True:
        answer_check = answer[:0]+'0'+answer[1:]
        user_guess_check = user_guess[:0]+'0'+user_guess[1:]
    if pos2 == True:
        answer_check = answer_check[0:1]+'0'+answer_check[2:]
        user_guess_check = user_guess_check[0:1]+'0'+user_guess_check[2:]
    if pos3 == True:
        answer_check = answer_check[0:2]+'0'+answer_check[3:]
        user_guess_check = user_guess_check[0:2]+'0'+user_guess_check[3:]
    if pos4 == True:
        answer_check = answer_check[0:3]+'0'+answer_check[4:]
        user_guess_check = user_guess_check[0:3]+'0'+user_guess_check[4:]
    if pos5 == True:
        answer_check = answer_check[0:4]+'0'
        user_guess_check = user_guess_check[0:4]+'0'


    if user_guess_check[0]!='0':
        pos1_loc = answer_check.find(user_guess_check[0])
        if pos1_loc!=-1:
            answer_check = answer_check[0:pos1_loc]+'1'+answer_check[pos1_loc+1:]
            user_guess_check = user_guess_check[:0]+'1'+user_guess_check[1:]
        else:
            user_guess_check = user_guess_check[:0] + '2' + user_guess_check[1:]

    if user_guess_check[1]!='0':
        pos2_loc = answer_check.find(user_guess_check[1])
        if pos2_loc!=-1:
            answer_check = answer_check[0:pos2_loc]+'1'+answer_check[pos2_loc+1:]
            user_guess_check = user_guess_check[0:1]+'1'+user_guess_check[2:]
        else:
            user_guess_check = user_guess_check[0:1]+'2'+user_guess_check[2:]

    if user_guess_check[2]!='0':
        pos3_loc = answer_check.find(user_guess_check[2])
        if pos3_loc!=-1:
            answer_check = answer_check[0:pos3_loc]+'1'+answer_check[pos3_loc+1:]
            user_guess_check = user_guess_check[0:2]+'1'+user_guess_check[3:]
        else:
            user_guess_check = user_guess_check[0:2]+'2'+user_guess_check[3:]

    if user_guess_check[3]!='0':
        pos4_loc = answer_check.find(user_guess_check[3])
        if pos4_loc!=-1:
            answer_check = answer_check[0:pos4_loc]+'1'+answer_check[pos4_loc+1:]
            user_guess_check = user_guess_check[0:3]+'1'+user_guess_check[4:]
        else:
            user_guess_check = user_guess_check[0:3]+'2'+user_guess_check[4:]

    if user_guess_check[4]!='0':
        pos5_loc = answer_check.find(user_guess_check[4])
        if pos5_loc!=-1:
            answer_check = answer_check[0:pos5_loc]+'1'+answer_check[pos5_loc+1:]
            user_guess_check = user_guess_check[0:4]+'1'
        else:
            user_guess_check = user_guess_check[0:4]+'2'

    user_guess_result=""

    i = 0
    while i < 5:
        if user_guess_check[i] == '0':
            user_guess_result = user_guess_result + colored(user_guess[i],'green')
        elif user_guess_check[i] == '1':
            user_guess_result = user_guess_result + colored(user_guess[i],'yellow')
        else:
            user_guess_result = user_guess_result + colored(user_guess[i],'red')
        i += 1
    print(user_guess_result)


i = 1
while i < 7:
    if i == 1:
        user_guess = input("What's your first guess? ")
        while dict_ref.check(user_guess)==False:
            user_guess = input("Your guess needs to be a real word. Try again! ")
        while len(user_guess)!=5:
            user_guess=input("Your guess needs to be 5 letters. Try again! ")
        word_check(user_guess)
        if user_guess == answer:
            print("Congratulations! You got it right in 1 guess!!!")
        else:
            print("Not quite. Try again!")
            i += 1
    elif i != 1:
        user_guess = input("Time for guess #"+str(i)+": ")
        while dict_ref.check(user_guess)==False:
            user_guess = input("Your guess needs to be a real word. Try again! ")
        while len(user_guess)!=5:
            user_guess=input("Your guess needs to be 5 letters. Try again! ")
        word_check(user_guess)
        if user_guess == answer:
            print("Congratulations! You got it right in "+str(i)+" guesses!!!")
            break
        else:
            if i!=6:
                print("Not quite. Try again!")
                i += 1
            else:
                print("Sorry, no more guesses. Don't worry, you'll get it next time!")
                break






