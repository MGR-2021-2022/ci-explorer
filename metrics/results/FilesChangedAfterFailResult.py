from metrics.results.Result import Result


class FilesChangedAfterFailResult(Result):
    def __init__(self, fails=0, modified_src=0, modified_test=0, modified_config=0):
        self.fails = fails
        self.modified_src = modified_src
        self.modified_test = modified_test
        self.modified_config = modified_config

    def __add__(self, o):
        return FilesChangedAfterFailResult(
            self.fails + o.fails,
            self.modified_src + o.modified_src,
            self.modified_test + o.modified_test,
            self.modified_config + o.modified_config
        )

    def add_to_files(self, src, test, config):
        self.modified_src += src
        self.modified_test += test
        self.modified_config += config

    def increment_fails(self):
        self.fails += 1

    def print(self):
        print("Fails: " + str(self.fails))
        print("Time src files were modified: " + str(self.modified_src) + " " + str(self.modified_src/self.fails))
        print("Time test files were modified: " + str(self.modified_test) + " " + str(self.modified_test/self.fails))
        print("Time config files were modified: " + str(self.modified_config) + " " + str(self.modified_config/self.fails))
        print()
