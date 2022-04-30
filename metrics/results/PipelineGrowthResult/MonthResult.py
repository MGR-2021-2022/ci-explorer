from metrics.results.Result import Result


class MonthResult(Result):
    def __init__(self, date, minutes=0, pushes=0, minutes_array: list = []):
        self.date = date
        self.pushes = pushes
        self.minutes = minutes
        self.minutes_array = minutes_array

    def __add__(self, o):
        date = self.date if self.date is not None else o.date
        return MonthResult(date, self.pushes + o.pushes, self.minutes + o.minutes)

    def add_minutes(self, minutes):
        self.minutes += minutes
        self.pushes += 1
        self.minutes_array.append(minutes)

    def print(self):
        print("Avg time: " + str(self.minutes/self.pushes) + "m (" + str(self.pushes) + ") - sd: " + str(self.standard_mean_deviation(self.minutes_array, self.minutes/self.pushes)))
