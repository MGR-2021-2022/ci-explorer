from metrics.results.Result import Result


class CountLinesWrittenResult(Result):
    def __init__(self, pr_number=0, comparison_to_previous_array: list = None, fail_comparison_to_pr_array: list = None, fix_comparison_to_pr_array: list = None,
                 total_lines_array: list = None):
        self.pr_number = pr_number;

        if comparison_to_previous_array is None:
            comparison_to_previous_array = []
        if fail_comparison_to_pr_array is None:
            fail_comparison_to_pr_array = []
        if fix_comparison_to_pr_array is None:
            fix_comparison_to_pr_array = []
        if total_lines_array is None:
            total_lines_array = []
        self.comparison_to_previous_array = comparison_to_previous_array
        self.fail_comparison_to_pr_array = fail_comparison_to_pr_array
        self.fix_comparison_to_pr_array = fix_comparison_to_pr_array
        self.total_lines_array = total_lines_array

    def __add__(self, o):
        return CountLinesWrittenResult(self.pr_number + o.pr_number, self.comparison_to_previous_array + o.comparison_to_previous_array, self.fail_comparison_to_pr_array + o.fail_comparison_to_pr_array,
                                     self.fix_comparison_to_pr_array + o.fix_comparison_to_pr_array, self.total_lines_array + o.total_lines_array)

    def add_to_comparison_to_previous_array(self, value: float):
        self.comparison_to_previous_array.append(value)

    def add_to_fail_comparison_to_pr_array(self, value: float):
        self.fail_comparison_to_pr_array.append(value)

    def add_to_fix_comparison_to_pr_array(self, value: float):
        self.fix_comparison_to_pr_array.append(value)

    def add_to_total_lines_array(self, value: float):
        self.total_lines_array.append(value)

    def increment_pr_number(self):
        self.pr_number += 1

    def failure_bigger(self) -> float:
        failure_bigger_count = 0
        total_count = len(self.fail_comparison_to_pr_array)
        for i in range(0, total_count):
            failure_bigger_count += self.fail_comparison_to_pr_array[i] > self.fix_comparison_to_pr_array[i]
        return failure_bigger_count/total_count

    def print(self):
        # print("pulls: " + str(self.pr_count) + " | commits: " + str(
        #     self.commit_count) + " | average: " + str(
        #     self.commit_count / self.pr_count))

        # print(str(len(self.total_lines_array)) + " " + str(len(self.comparison_to_previous_array)) + " " +
        #       self.round(self.avg(self.total_lines_array)) + " " + self.median(self.total_lines_array) + " " + self.standard_mean_deviation(self.total_lines_array, self.avg(self.total_lines_array)))

        # print(self.round(self.avg(self.fail_comparison_to_pr_array)) + " " + self.standard_mean_deviation(self.fail_comparison_to_pr_array, self.avg(self.fail_comparison_to_pr_array)) + " " + self.median(self.fail_comparison_to_pr_array) + " " +
        #      self.round(self.avg(self.fix_comparison_to_pr_array)) + " " + self.standard_mean_deviation(self.fix_comparison_to_pr_array, self.avg(self.fix_comparison_to_pr_array)) + " " + self.median(self.fix_comparison_to_pr_array) + " " + self.round(self.failure_bigger()))
        counter = 0
        last = -1
        for fail_comparision_to_pr in self.comparison_to_previous_array:
            # if last == fail_comparision_to_pr:
            #     continue
            print(" ", end="")
            print(fail_comparision_to_pr, end="")
            # print(" ")
            # print(fail_comparision_to_pr)
        # print(" ")
        # for fix_comparision_to_pr in self.fix_comparison_to_pr_array:
        #     # if last == fix_comparision_to_pr:
        #     #     continue
        #     print(" ", end="")
        #     print(fix_comparision_to_pr, end="")
        #     counter += 1
        #     last = fix_comparision_to_pr

        #     if counter > 1000:
        #         counter = 0
        #         print(" ")
        print(" ")

