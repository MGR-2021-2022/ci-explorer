from metrics.results.Result import Result


class IsInspectionEnoughResult(Result):
    def __init__(self, pulls: int = 0, pushes: int = 0, pushes_after_pass: int = 0, pulls_with_after_pass: int = 0,
                 pushes_after_pass_array: list = []):
        self.pulls = pulls
        self.pushes_after_pass_array = pushes_after_pass_array
        self.pushes = pushes
        self.pushes_after_pass = pushes_after_pass
        self.pulls_with_after_pass = pulls_with_after_pass

    def __add__(self, o):
        return IsInspectionEnoughResult(self.pulls + o.pulls, self.pushes + o.pushes,
                                        self.pushes_after_pass + o.pushes_after_pass,
                                        self.pulls_with_after_pass + o.pulls_with_after_pass,
                                        self.pushes_after_pass_array + self.pushes_after_pass_array)

    def add_to_pulls(self, pulls: int):
        self.pulls += pulls

    def add_to_pushes(self, pushes: int):
        self.pushes += pushes

    def add_to_pushes_after_pass(self, pushes_after_pass: int):
        self.pushes_after_pass += pushes_after_pass
        self.pushes_after_pass_array.append(pushes_after_pass)

    def add_to_pulls_with_after_pass(self, pulls_after_pass: int):
        self.pulls_with_after_pass += pulls_after_pass

    def print(self):
        print("Commits (tested) after pass in pr: " + str(self.pushes_after_pass / self.pulls) + " (" + str(self.pulls) + ") - smd - " + str(self.standard_mean_deviation(self.pushes_after_pass_array, self.pushes_after_pass / self.pulls)))
        print("Pull requests with commits after pass: " + str(self.pulls_with_after_pass / self.pulls * 100.0) + "% (" + str(self.pulls) + ")")
        # print("pulls: " + str(self.pr_count) + " | commits: " + str(
        #     self.commit_count) + " | average: " + str(
        #     self.commit_count / self.pr_count))



