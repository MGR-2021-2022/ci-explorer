from metrics.results.Result import Result


#7


class CommitterChangeResult(Result):
    def __init__(self, pr_count=0, authors_count=0, first_and_last=0, always=0):
        self.pr_count = pr_count
        self.authors_count = authors_count
        self.always = always
        self.first_and_last = first_and_last

    def __add__(self, o):
        return CommitterChangeResult(self.pr_count + o.pr_count, self.authors_count + o.authors_count,
                                     self.first_and_last + o.first_and_last, self.always + o.always)

    def increment_pr_count(self):
        self.pr_count += 1

    def add_to_authors_count(self, authors_count: int):
        self.authors_count += authors_count

    def add_to_first_and_last(self, first_and_last: int):
        self.first_and_last += first_and_last

    def add_to_always(self, always: int):
        self.always += always

    def print(self):
        print("pulls: " + str(self.pr_count) 
              + " | authors: " + str(self.authors_count) + " (average: " + str(self.authors_count / self.pr_count) + 
              ")| first and last same: " + str(self.first_and_last) + " (average: " 
              + str(self.first_and_last / self.pr_count) + ")| always same author: " 
              + str(self.always) + " (average: " + str(self.always / self.pr_count) + ")")
        print(str(self.pr_count))
        print(str(self.authors_count))
        print(str(self.authors_count / self.pr_count))
        print(str(self.first_and_last))
        print(str(self.first_and_last / self.pr_count))
        print(str(self.always))
        print(str(self.always / self.pr_count))
        print()
