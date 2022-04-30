from metrics.calculations.Calc import Calc
from metrics.results.CommitNumberWIthCI.CommitNumberWhenCIResult import CommitNumberWhenCIResult
from metrics.results.Result import Result
from model.Repository import Repository


#5


class CommitNumberWhenCICalc(Calc):
    def execute(repo: Repository) -> Result:
        results = CommitNumberWhenCIResult()
        repository_groups = {
            'microsoft/vscode': [
                Grouping(CommitNumberWhenCIResult.ga_label, 67129, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 245, 67123),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 244)
            ]
        }

        for pull in repo.pull_requests:
            groupings = repository_groups[repo.name]
            for grouping in groupings:
                if grouping.min_pull <= pull.number <= grouping.max_pull:
                    results.addCommits(grouping.label, len(pull.commits))
        return results


class Grouping:
    def __init__(self, label, min_pull, max_pull):
        self.label = label
        self.min_pull = min_pull
        self.max_pull = max_pull