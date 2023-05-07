# job_opening = ("Software Engineer", "New York City", 100000)
#
# position, city, salary = job_opening
#
# print(position)
# print(city)
# print(salary)

# address = ("35 Elm Street", "San Francisco", "CA", "94107")
#
# street, *city_and_state, zipcode = address
#
# print(street)
# print(city_and_state)
# print(zipcode)

def sum_of_evens_and_odds(tup):
    evens = 0
    odds = 0
    for num in tup:
        if num % 2 == 0:
            evens += num
        else:
            odds += num
    return [evens,odds]

print(sum_of_evens_and_odds((2, 4, 6)))











