from metrics.results.Result import Result


#4


class NumberOfCommitsResult(Result):
    def __init__(self, pr_count: int = 0, commit_count: int = 0):
        self.pr_count = pr_count
        self.commit_count = commit_count

    def __add__(self, o):
        return NumberOfCommitsResult(self.pr_count + o.pr_count, self.commit_count + o.commit_count)

    def increment_pr_count(self):
        self.pr_count += 1

    def add_to_commit_count(self, commit_count: int):
        self.commit_count += commit_count

    def print(self):
        print("pulls: " + str(self.pr_count) + " | commits: " + str(
            self.commit_count) + " | average: " + str(
            self.commit_count / self.pr_count))
