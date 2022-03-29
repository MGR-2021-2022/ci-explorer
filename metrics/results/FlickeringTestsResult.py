from metrics.results.Result import Result


class FlickeringTestsResult(Result):
    def __init__(self, pushes=0, flickering_tests=0):
        self.pushes = pushes
        self.flickering_tests = flickering_tests

    def __add__(self, o):
        return FlickeringTestsResult(
            self.pushes + o.pushes,
            self.flickering_tests + o.flickering_tests
        )

    def increment_pushes(self):
        self.pushes += 1

    def increment_flickering_tests(self):
        self.flickering_tests += 1

    def print(self):
        print("Pushes: " + str(self.pushes))
        print("Flicerking tests: " + str(self.flickering_tests))


