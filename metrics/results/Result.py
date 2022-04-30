import math


class Result:
    def print(self):
        pass

    def __add__(self, o):
        pass

    def standard_mean_deviation(self, elements: list, avg: float) -> float:
        square_sum = 0
        for element in elements:
            square_sum += math.pow(avg - element, 2)
        return math.sqrt(square_sum/len(elements))
