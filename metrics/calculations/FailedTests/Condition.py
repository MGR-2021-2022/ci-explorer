from model.PullRequest import PullRequest


class Condition:
    def isFulfilled(self, pull: PullRequest) -> bool:
        return False
