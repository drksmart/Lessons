question_results = []
quiz_score = []

if float(input("Question 1: What is the value of pi to two decimals? ")) == 3.14:
    question_results.append("Question 1: Correct\n")
    quiz_score.append(1)
else:
    question_results.append("Question 1: Incorrect\n")
    quiz_score.append(0)

if input("Question 2: Who was the first president of the U.S.A.? ") == "George Washington":
    question_results.append("Question 2: Correct\n")
    quiz_score.append(1)
else:
    question_results.append("Question 2: Incorrect\n")
    quiz_score.append(0)

print("\nHere are the individual question results:\n")

for result in question_results:
    print(result)

percent = "{:.1%}".format(sum(quiz_score)/len(quiz_score))

print("\nAnd here is your final score:\n")
print(percent)