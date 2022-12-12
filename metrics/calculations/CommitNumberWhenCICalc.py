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
            ],
            'django/django': [
                Grouping(CommitNumberWhenCIResult.ga_label, 15002, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 4001, 15002),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 4000)
            ],
            'bitcoin/bitcoin': [
                Grouping(CommitNumberWhenCIResult.ga_label, 19118, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 4727, 19117),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 4726)
            ],
            'facebook/lexical': [
                Grouping(CommitNumberWhenCIResult.ga_label, 19, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 0, 0),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 19)
            ],
            'hashicorp/terraform': [
                Grouping(CommitNumberWhenCIResult.ga_label, 26844, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 145, 26843),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 144)
            ],
            'laravel/framework': [
                Grouping(CommitNumberWhenCIResult.ga_label, 31541, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 5, 31540),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 4)
            ],
            'diasurgical/devilutionX': [
                Grouping(CommitNumberWhenCIResult.ga_label, 521, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 0, 520),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 0)
            ],
            'flutter/flutter': [
                Grouping(CommitNumberWhenCIResult.ga_label, 21082, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 0, 21081),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 0)
            ],
            'starship/starship': [
                Grouping(CommitNumberWhenCIResult.ga_label, 0, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 0, 0),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 0)
            ],
            'microsoft/CBL-Mariner': [
                Grouping(CommitNumberWhenCIResult.ga_label, 100, 999999),
                Grouping(CommitNumberWhenCIResult.tp_label, 0, 99),
                Grouping(CommitNumberWhenCIResult.no_ci_label, 0, 00)
            ]
        }

        pull_numbers = []
        for pull in repo.pull_requests:
            if pull.number in pull_numbers:
                continue
            pull_numbers.append(pull.number)

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