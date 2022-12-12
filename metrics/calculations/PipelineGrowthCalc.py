from metrics.calculations.Calc import Calc
from metrics.results.PipelineGrowthResult.PipelineGrowthResult import PipelineGrowthResult
from metrics.results.Result import Result
from model.Repository import Repository


#10


class PipelineGrowthCalc(Calc):
    def execute(repo: Repository) -> Result:
        result = PipelineGrowthResult()

        inspected_checks = []

        for pull in repo.pull_requests:
            for commit in pull.commits:
                if commit.has_checks():
                    if commit.has_checks_in(inspected_checks):
                        continue
                    commit.add_check_to(inspected_checks)
                    if commit.has_failed_inspection():
                        continue

                    earliest_start = commit.get_inspection_start()
                    latest_end = commit.get_inspection_end()

                    if earliest_start is not None and latest_end is not None:
                        time = latest_end - earliest_start
                        result.addMinutes(earliest_start, time.seconds // 60)

        return result