if float(input("Question 1: What is the value of pi to two decimals? ")) == 3.14:
    with open("question_results","w") as results:
        results.write("Question 1: Correct\n")
    with open("quiz_score","w") as scores:
        scores.write("1\n")
else:
    with open("question_results","w") as results:
        results.write("Question 1: Incorrect\n")
    with open("quiz_score","w") as scores:
        scores.write("0\n")


if input("Question 2: Who was the first President of the U.S.A.? ") == "George Washington":
    with open("question_results","a") as results:
        results.write("Question 2: Correct\n")
    with open("quiz_score","a") as scores:
        scores.write("1\n")
else:
    with open("question_results","a") as results:
        results.write("Question 2: Incorrect\n")
    with open("quiz_score","a") as scores:
        scores.write("0\n")


if input("Question 3: What is the name of the Portland basketball team? ") == "Trailblazers":
    with open("question_results","a") as results:
        results.write("Question 3: Correct\n")
    with open("quiz_score","a") as scores:
        scores.write("1\n")
else:
    with open("question_results","a") as results:
        results.write("Question 3: Incorrect\n")
    with open("quiz_score","a") as scores:
        scores.write("0\n")


if int(input("Question 4: How many in a dozen? ")) == 12:
    with open("question_results","a") as results:
        results.write("Question 4: Correct\n")
    with open("quiz_score","a") as scores:
        scores.write("1\n")
else:
    with open("question_results","a") as results:
        results.write("Question 4: Incorrect\n")
    with open("quiz_score","a") as scores:
        scores.write("0\n")


if input("Question 5: Does baking bread smell good? ") == "Yes":
    with open("question_results","a") as results:
        results.write("Question 5: Correct\n")
    with open("quiz_score","a") as scores:
        scores.write("1\n")
else:
    with open("question_results","a") as results:
        results.write("Question 5: Incorrect\n")
    with open("quiz_score","a") as scores:
        scores.write("0\n")

print("Here are the results for each question:\n\n")

with open("question_results","r") as result_list:
    for line in result_list:
        print(line)
