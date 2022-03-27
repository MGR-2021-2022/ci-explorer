class ResultsHelper:
    def add_results_nested(target, source):
        for row in target.items():
            for key in row[1].keys():
                target[row[0]][key] += source[row[0]][key]
        return target

    def add_results(target, source):
        for key in target.keys():
            target[key] += source[key]
        return target