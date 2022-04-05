from SqlAlchemyBase import Session
from metrics.calculations.CommitterChangeCalc import CommitterChangeCalc
from metrics.calculations.FailedTests.GroupsFactory import GroupsFactory
from metrics.calculations.FailedTestsCalc import FailedTestsCalc
from metrics.calculations.FilesChangedAfterFailCalc import FilesChangedAfterFailCalc
from metrics.calculations.FlickeringTestsCalc import FlickeringTestsCalc
from metrics.calculations.NumberOfCommitsCalc import NumberOfCommitsCalc
from metrics.calculations.ReactionTimeCalc import ReactionTimeCalc
from metrics.results.FlickeringTestsResult import FlickeringTestsResult
from model.Repository import Repository

db_session = Session()
repos = db_session.query(Repository).all()

total_result = None
groupsFactory = GroupsFactory()


for repo in repos:
    # result = FlickeringTestsCalc.execute(repo)



    #1a
    # todo opcjonalnie dodać inne grupy dla innych repo
    # result = FailedTestsCalc.execute(repo, groupsFactory.getInspectionTypeGroups())

    #1b
    # result = FailedTestsCalc.execute(repo, groupsFactory.getInspectionTimeGroups())

    #1c
    # result = FailedTestsCalc.execute(repo, groupsFactory.getIsAuthorGroups())

    #1d
    # result = FailedTestsCalc.execute(repo, groupsFactory.getUserCommitNumberGroups())

    #1e
    # result = FailedTestsCalc.execute(repo, groupsFactory.getTechnologyGroups())

    #1f
    # result = FailedTestsCalc.execute(repo, groupsFactory.getSourceCodeLinesChanged())

    # 1f
    # result = FailedTestsCalc.execute(repo, groupsFactory.getTestCodeLinesChanged())

    #2
    result = FilesChangedAfterFailCalc.execute(repo)

    #4
    # result = NumberOfCommitsCalc.execute(repo)

    #6
    # result = ReactionTimeCalc.execute(repo)

    #7
    # result = CommitterChangeCalc.execute(repo)

    print(repo.name)
    result.print()
    if total_result is None:
        total_result = result
    else:
        total_result = result + total_result

print("In total:")
total_result.print()