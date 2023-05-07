

def quiz_loop(question_list):
    question_results = []
    quiz_score = []
    for question in question_list:
        if input(question) == question_list[question]:
            question_results.append(question + " -- CORRECT!")
            quiz_score.append(1)
        else:
            question_results.append(question + " -- WRONG!")
            quiz_score.append(0)
    print("\nHere's your results!\n")
    for results in question_results:
        print(results)
    print("\nHere's your score!\n")
    print("{:.1%}".format(sum(quiz_score) / len(quiz_score)))

question_list = [{"Question 1: What is the value of pi? ":"3.14",
                "Question 2: Who was the first President of the U.S.A.? ":"George Washington",
                "Question 3: What is the name of the Portland basketball team? ":"Trailblazers",
                "Question 4: How many in a dozen? ":"12",
                "Question 5: Does baking bread smell good (Y/N)? ":"Y"},
                 {"Question 1: What is the value of butts? ": "3.14",
                  "Question 2: Who was the first President of the U.S.A.? ": "George Washington",
                  "Question 3: What is the name of the Portland basketball team? ": "Trailblazers",
                  "Question 4: How many in a dozen? ": "12",
                  "Question 5: Does baking bread smell good (Y/N)? ": "Y"},
                {"Question 1: What is the value of your mom? ":"3.14",
                "Question 2: Who was the first President of the U.S.A.? ":"George Washington",
                "Question 3: What is the name of the Portland basketball team? ":"Trailblazers",
                "Question 4: How many in a dozen? ":"12",
                "Question 5: Does baking bread smell good (Y/N)? ":"Y"}
                 ]

continue = True

while continue:
    user_input = input("Would you like to take a fun quiz (Y/N)?")

    quiz_loop(question_list)

if input("Would you like to take a fun quiz (Y/N)?") == "Y":
    quiz_loop(question_list1)
    if input("\nDo you want to take another quiz (Y/N)?\n") == "Y":
        quiz_loop(question_list2)
        if input("\nDo you want to take another quiz (Y/N)?\n") == "Y":
            quiz_loop(question_list3)
            print("\nCongratulations! You've taken all the quizes!!")
        else:
            print("\nOkay! Thanks for playing!!")
    else:
        print("\nOkay! Thanks for playing!!")
else:
    print("\nThen go fuck yourself, you fun hating cunt!")



