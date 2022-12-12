from metrics.results.Result import Result


#6


class ReactionTimeResult(Result):
    def __init__(self, pushes: int = 0, reaction_time: int = 0, reaction_time_array=None):
        if reaction_time_array is None:
            reaction_time_array = []
        self.pushes = pushes
        self.reaction_time = reaction_time
        self.reaction_time_array = reaction_time_array
        
    def __add__(self, o):
        return ReactionTimeResult(self.pushes + o.pushes, self.reaction_time + o.reaction_time, self.reaction_time_array + o.reaction_time_array)

    def increment_pushes(self):
        self.pushes += 1

    def add_to_reaction_time(self, reaction_time: int):
        self.reaction_time += reaction_time
        self.reaction_time_array.append(reaction_time)

    def print(self):
        # print("hours: " + str(self.reaction_time) + " | commits: " + str(self.pushes) + " | average: "
        #       + str(self.reaction_time / self.pushes))
        for react_time in self.reaction_time_array:
            # print(" ", end="")
            print(react_time)
        # print("")
        # print(str(self.pushes)+ " " + self.round(self.reaction_time) + " "
        #       + self.round(self.reaction_time / self.pushes) + " " + self.standard_mean_deviation(self.reaction_time_array, self.reaction_time / self.pushes))

