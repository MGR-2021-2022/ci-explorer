from metrics.results.Result import Result


class MonthResult(Result):
    def __init__(self, date, minutes=0, pushes=0, minutes_array=None):
        if minutes_array is None:
            minutes_array = []
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

    def print(self, order_number: int, original_time: int):
        # print("Avg time: " + str(self.minutes/self.pushes) + "m (" + str(self.pushes) + ") - sd: " + str(self.standard_mean_deviation(self.minutes_array, self.minutes/self.pushes)))
        print(str(order_number) + " " + str(self.pushes) + " " + self.round(self.minutes/self.pushes) + " " + str(self.standard_mean_deviation(self.minutes_array, self.minutes/self.pushes) + " " +
                                                                                                                  self.round((self.minutes/self.pushes)/original_time)))
