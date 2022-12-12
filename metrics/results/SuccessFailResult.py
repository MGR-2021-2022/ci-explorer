from typing import Type

from metrics.results.Result import Result


#7


class SuccessFailResult(Result):
    def __init__(self, result: Type[Result] = None, success: Result = None, fail: Result = None):
        if result is not None:
            self.success = result()
            self.fail = result()
        else:
            self.success = success
            self.fail = fail

    def getSuccess(self):
        return self.success

    def getFail(self):
        return self.fail

    def print(self):
        # print("Succes:")
        # self.success.print()
        # print("Fail:")
        self.fail.print()
        # print("Total")
        # (self.success + self.fail).print()

    def __add__(self, o):
        return SuccessFailResult(None, self.success + o.success, self.fail + o.fail)