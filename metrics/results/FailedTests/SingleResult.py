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
        print("Passes: " + str(self.passes))
        print("Fails: " + str(self.fails))
        print("Total: " + str(self.passes + self.fails))
