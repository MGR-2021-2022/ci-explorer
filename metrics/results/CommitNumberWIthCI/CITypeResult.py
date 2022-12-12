from metrics.results.Result import Result


class CITypeResult(Result):
    def __init__(self, pulls:int = 0, commits:int = 0, commits_array: list = None):
        if commits_array is None:
            commits_array = []
        self.pulls = pulls
        self.commits = commits
        self.commits_array = commits_array

    def __add__(self, o):
        return CITypeResult(self.pulls + o.pulls, self.commits + o.commits, self.commits_array + o.commits_array)

    def add_commits(self, commits):
        self.commits += commits
        self.commits_array.append(commits)
        self.pulls += 1

    def print(self):
        # print("Avg commits: " + str(self.commits/self.pulls) + " (" + str(self.pulls) + ") - sd - " + str(self.standard_mean_deviation(self.commits_array, self.commits/self.pulls)))
        for commits in self.commits_array:
            # print(" ", end="")
            print(commits)


        #
        # if len(self.commits_array) == 0:
        #     print()
        #     return
        # print(str(self.pulls) + " " + self.round(self.commits/self.pulls) + " " + self.standard_mean_deviation(self.commits_array, self.commits/self.pulls))
