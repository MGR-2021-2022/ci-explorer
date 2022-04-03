from SqlAlchemyBase import Session
from metrics.calculations.CommitterChangeCalc import CommitterChangeCalc
from metrics.calculations.FailedTests.GroupsFactory import GroupsFactory
from metrics.calculations.FailedTestsCalc import FailedTestsCalc
from metrics.calculations.FlickeringTestsCalc import FlickeringTestsCalc
from metrics.calculations.ReactionTimeCalc import ReactionTimeCalc
from metrics.results.FlickeringTestsResult import FlickeringTestsResult
from model.Repository import Repository

db_session = Session()
repos = db_session.query(Repository).all()

total_result = None
groupsFactory = GroupsFactory()


for repo in repos:
    # result = FlickeringTestsCalc.execute(repo)

    # result = FailedTestsCalc.execute(repo, groupsFactory.getInspectionTimeGroups())
    # result = FailedTestsCalc.execute(repo, groupsFactory.getUserCommitNumberGroups())

    #6
    result = ReactionTimeCalc.execute(repo)

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