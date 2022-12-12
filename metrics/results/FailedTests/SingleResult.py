from metrics.results.Result import Result


class SingleResult(Result):
    def __init__(self, fails=0, passes=0):
        self.fails = fails
        self.passes = passes

    def __add__(self, o):
        return SingleResult(self.fails + o.fails, self.passes + o.passes)

    def increment_passes(self):
        self.passes += 1

    def increment_fails(self):
        self.fails += 1

    def print(self):
        if self.passes + self.fails == 0:
            print('')
            return
        print(str(self.passes) + " " + self.percentage_formatted(self.passes/(self.passes + self.fails)) + " " + str(self.fails) + " " +
              self.percentage_formatted(self.fails/(self.passes + self.fails)) + " " + str(self.passes + self.fails))
        # print("Passes: " + str(self.passes))
        # print("Fails: " + str(self.fails))
        # print("Total: " + str(self.passes + self.fails))