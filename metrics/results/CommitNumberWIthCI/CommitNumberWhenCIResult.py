from typing import Dict

from metrics.results.CommitNumberWIthCI.CITypeResult import CITypeResult
from metrics.results.Result import Result


class CommitNumberWhenCIResult(Result):
    ga_label = 'github_action'
    tp_label = 'third_party'
    no_ci_label = 'no_ci'

    def __init__(self):
        self.results: Dict[str, CITypeResult] = {
            'github_action': CITypeResult(0, 0),
            'third_party': CITypeResult(0, 0),
            'no_ci': CITypeResult(0, 0)
        }

    def __add__(self, o):
        results = {}
        for label in self.results.keys():
            results[label] = self.results[label] + o.results[label]
        group_result = CommitNumberWhenCIResult()
        group_result.results = results
        return group_result

    def addCommits(self, label: str, commits: int):
        self.results[label].add_commits(commits)

    def print(self):
        for label in self.results.keys():
            print(label)
            self.results[label].print()
