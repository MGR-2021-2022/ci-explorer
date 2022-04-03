from metrics.results.Result import Result


#6


class ReactionTimeResult(Result):
    def __init__(self, pushes: int = 0, reaction_time: int = 0):
        self.pushes = pushes
        self.reaction_time = reaction_time

    def __add__(self, o):
        return ReactionTimeResult(self.pushes + o.pushes, self.reaction_time + o.reaction_time)

    def increment_pushes(self):
        self.pushes += 1

    def add_to_reaction_time(self, reaction_time: int):
        self.reaction_time += reaction_time

    def print(self):
        print("hours: " + str(self.reaction_time) + " | commits: " + str(self.pushes) + " | average: "
              + str(self.reaction_time / self.pushes))
