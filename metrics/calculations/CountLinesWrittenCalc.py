from metrics.calculations.Calc import Calc
from metrics.results.CountLinesWrittenResult import CountLinesWrittenResult
from metrics.results.Result import Result
from model.Repository import Repository


class CountLinesWrittenCalc(Calc):
    def execute(repo: Repository) -> Result:
        result = CountLinesWrittenResult()
        pull_numbers = []
        for pull in repo.pull_requests:
            if pull.number in pull_numbers:
                continue
            pull_numbers.append(pull.number)
            prev_fail = False
            total_lines = 0
            failed_lines = 0
            fix_array = []
            failed_array = []
            for commit in pull.commits:
                curr_fail = False
                curr_lines = commit.modified_lines
                total_lines += curr_lines
                if commit.has_checks():
                    for check in commit.check_runs:
                        if check.has_problem():
                            curr_fail = True
                            break

                    if prev_fail and failed_lines != 0 and curr_lines != 0 and not curr_fail:
                        result.add_to_comparison_to_previous_array(curr_lines/failed_lines)
                        fix_array.append(curr_lines)
                        failed_array.append(failed_lines)

                    # only first fail
                    if not prev_fail and curr_fail:
                        failed_lines = curr_lines

                    prev_fail = curr_fail

                    if not curr_fail:
                        failed_lines = 0
                # only first fail
                # else:
                #     failed_lines += curr_lines


            if len(fix_array) > 0:
                result.add_to_total_lines_array(total_lines)
                for fix_lines in fix_array:
                    result.add_to_fix_comparison_to_pr_array(fix_lines / total_lines)

                for failed_lines in failed_array:
                    result.add_to_fail_comparison_to_pr_array(failed_lines / total_lines)

        return result
