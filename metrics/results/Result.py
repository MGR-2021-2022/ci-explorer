import math
import statistics


class Result:
    def print(self):
        pass

    def __add__(self, o):
        pass

    def standard_mean_deviation(self, elements: list, avg: float) -> str:
        square_sum = 0
        for element in elements:
            square_sum += math.pow(avg - element, 2)
        return self.round(math.sqrt(square_sum/len(elements)))

    def percentage_formatted(self, num: float) -> str:
        return self.round(num * 100)

    def round(self, num: float) -> str:
        return "{:.2f}".format(round(num, 2))

    def avg(self, elements: list) -> float:
        elements_sum = 0
        for element in elements:
            elements_sum += element
        return elements_sum/len(elements)

    def median(self, elements: list) -> str:
        return self.round(statistics.median(elements))
