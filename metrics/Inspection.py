from csvGenerator import db_session
from metrics.calculations.FlickeringTestsCalc import FlickeringTestsCalc
from metrics.results.FlickeringTestsResult import FlickeringTestsResult
from model.Repository import Repository

repos = db_session.query(Repository).all()

total_result = None
for repo in repos:
    result = FlickeringTestsCalc.execute(repo)
    print(repo.name)
    result.print()
    if total_result is None:
        total_result = result
    else:
        total_result = result + total_result

print("In total:")
total_result.print()