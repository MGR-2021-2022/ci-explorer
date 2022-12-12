import time

from SqlAlchemyBase import Session
from metrics.calculations.CommitNumberWhenCICalc import CommitNumberWhenCICalc
from metrics.calculations.CommitterChangeCalc import CommitterChangeCalc
from metrics.calculations.CountLinesWrittenCalc import CountLinesWrittenCalc
from metrics.calculations.FailedTests.GroupsFactory import GroupsFactory
from metrics.calculations.FailedTestsCalc import FailedTestsCalc
from metrics.calculations.FailedTestsIndividuallyCalc import FailedTestsIndividuallyCalc
from metrics.calculations.FilesChangedAfterFailCalc import FilesChangedAfterFailCalc
from metrics.calculations.FlickeringTestsCalc import FlickeringTestsCalc
from metrics.calculations.IsInspectionEnoughCalc import IsInspectionEnoughCalc
from metrics.calculations.NumberOfCommitsCalc import NumberOfCommitsCalc
from metrics.calculations.PipelineGrowthCalc import PipelineGrowthCalc
from metrics.calculations.ReactionTimeCalc import ReactionTimeCalc
from metrics.results.FlickeringTestsResult import FlickeringTestsResult
from model.Repository import Repository

db_session = Session()
repos = db_session.query(Repository).all()

total_result = None
groupsFactory = GroupsFactory()


for repo in repos:
    # if repo.name != "microsoft/vscode":
    # if repo.name != "django/django":
    # if repo.name != "bitcoin/bitcoin":
    # if repo.name != "facebook/lexical":
    # if repo.name != "hashicorp/terraform":
    # if repo.name != "laravel/framework":
    # if repo.name != "diasurgical/devilutionX":
    if repo.name == "flutter/flutter":
    # if repo.name != "starship/starship":
    # if repo.name != "microsoft/CBL-Mariner":
        print("")
        print("")
        continue

    #1a - B
    # todo opcjonalnie dodać inne grupy dla innych repo
    # result = FailedTestsIndividuallyCalc.execute(repo, groupsFactory.getInspectionTypeGroups())

    #1b - C
    # result = FailedTestsCalc.execute(repo, groupsFactory.getInspectionTimeGroups())

    #1c -- CANCELLED
    # result = FailedTestsCalc.execute(repo, groupsFactory.getIsAuthorGroups())

    #1d - D
    # result = FailedTestsCalc.execute(repo, groupsFactory.getUserCommitNumberGroups())

    #1e - E
    # result = FailedTestsCalc.execute(repo, groupsFactory.getTechnologyGroups())

    #1f - F
    # result = FailedTestsCalc.execute(repo, groupsFactory.getSourceCodeLinesChanged())

    #1g - G
    # result = FailedTestsCalc.execute(repo, groupsFactory.getTestCodeLinesChanged())

    #2 - H
    # result = FilesChangedAfterFailCalc.execute(repo)

    #3 - I
    result = CountLinesWrittenCalc.execute(repo)

    #4 - J
    # result = CommitNumberWhenCICalc.execute(repo)

    #5 - K
    # result = NumberOfCommitsCalc.execute(repo)

    #6 - L
    # result = ReactionTimeCalc.execute(repo)

    #7 - M
    # result = CommitterChangeCalc.execute(repo)

    #8 - N
    # result = FlickeringTestsCalc.execute(repo)

    #9 - O
    # result = IsInspectionEnoughCalc.execute(repo)

    #10 - P
    # result = PipelineGrowthCalc.execute(repo)

    # print(repo.name)
    # print(repo.name)
    print(repo.name, end="")
    result.print()
    print("")

    if total_result is None:
        total_result = result
    else:
        total_result = result + total_result

# print("In total:")
# total_result.print()


#     print(repo.name)
#     print(repo.name, end="")
#     result.print()
#
#     if total_result is None:
#         total_result = result
#     else:
#         total_result = result + total_result
#
# print("In total:")
# total_result.print()