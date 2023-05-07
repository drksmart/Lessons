question_list ={"Question 1: What is the value of pi? ":"3.14",
                "Question 2: Who was the first President of the U.S.A.? ":"George Washington",
                "Question 3: What is the name of the Portland basketball team? ":"Trailblazers",
                "Question 4: How many in a dozen? ":"12",
                "Question 5: Does baking bread smell good (Y/N)? ":"Y"}
question_results = []
quiz_score = []

for question in question_list:
    if input(question) == question_list[question]:
        question_results.append(question + " was answered correctly")
        quiz_score.append(1)
    else:
        question_results.append(question + " was answered incorrectly")
        quiz_score.append(0)

for results in question_results:
    print(results)

print("{:.1%}".format(sum(quiz_score)/len(quiz_score)))


