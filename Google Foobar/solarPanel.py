import math


def solution(area):
    square = []
    while area > 0:
        area_sqrt = math.floor(math.sqrt(area))
        calculated_sqr = int(area_sqrt ** 2)
        square.append(calculated_sqr)
        area -= calculated_sqr

    return square


print(solution(15324))
