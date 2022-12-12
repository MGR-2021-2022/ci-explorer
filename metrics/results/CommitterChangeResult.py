from metrics.results.Result import Result


#7


class CommitterChangeResult(Result):
    def __init__(self, pr_count=0, authors_count=0, first_and_last=0, always=0, authors_array=None):
        if authors_array is None:
            authors_array = []
        self.pr_count = pr_count
        self.authors_count = authors_count
        self.always = always
        self.first_and_last = first_and_last
        self.authors_array = authors_array

    def __add__(self, o):
        return CommitterChangeResult(self.pr_count + o.pr_count, self.authors_count + o.authors_count,
                                     self.first_and_last + o.first_and_last, self.always + o.always, self.authors_array + o.authors_array)

    def increment_pr_count(self):
        self.pr_count += 1

    def add_to_authors_count(self, authors_count: int):
        self.authors_count += authors_count
        self.authors_array.append(authors_count)

    def add_to_first_and_last(self, first_and_last: int):
        self.first_and_last += first_and_last

    def add_to_always(self, always: int):
        self.always += always

    def print(self):
        # print("pulls: " + str(self.pr_count)
        #       + " | authors: " + str(self.authors_count) + " (average: " + str(self.authors_count / self.pr_count) +
        #       ")| first and last same: " + str(self.first_and_last) + " (average: "
        #       + self.round(self.first_and_last / self.pr_count) + ")| always same author: "
        #       + str(self.always) + " (average: " + str(self.always / self.pr_count) + ")")
        for authors in self.authors_array:
            print(" ", end = "")
            print(authors, end = "")
        print("")
        # print(str(self.pr_count) + " " + str(self.authors_count) + " " + self.round(self.authors_count / self.pr_count) + " " + self.standard_mean_deviation(self.authors_array, self.authors_count / self.pr_count) + " " + str(self.first_and_last) + " " + self.percentage_formatted(self.first_and_last / self.pr_count)
        #       + " " + str(self.always) + " " + self.percentage_formatted(self.always / self.pr_count))
