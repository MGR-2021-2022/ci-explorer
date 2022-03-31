from metrics.results.Result import Result


class SingleResult(Result):
    def __init__(self, fails=0, passes=0):
        self.fails = fails
        self.passes = passes

    def increment_passes(self):
        self.passes += 1

    def increment_fails(self):
        self.fails += 1

    def print(self):
        print("Fails: " + str(self.fails))
        print("Passes: " + str(self.passes))
