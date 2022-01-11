# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import time

from github import Github, PaginatedList, CheckRun, PullRequest

from SqlAlchemyBase import Session
from model.Commit import Commit as CommitModel
from model.User import User as UserModel
from model.Repository import Repository as RepositoryModel
from model.CheckRun import CheckRun as CheckRunModel
from model.PullRequest import PullRequest as PullRequestModel
from SqlAlchemyBase import Base as Model



def getChecksResult(checks: PaginatedList):
    global db_session
    for check in checks:
        check_model = CheckRunModel(hash=check.id)
        db_session.add(check_model)


def getPullChecks(pull: PullRequest, pull_request_model: PullRequestModel):
    global db_session, author
    counter = 0
    for commit in pull.get_commits():
        counter += 1
        user_model = UserModel(name=commit.commit.author.name)
        saveToDb(user_model)
        commit_model = CommitModel(hash=commit.sha, author_id=user_model.id, order_number=counter,
                                   created_at=commit.commit.author.date, pull_request_id = pull_request_model.id)
        saveToDb(commit_model)
        getChecksResult(commit.get_check_runs())

def saveToDb(model: Model):
    db_session.add(model)
    db_session.commit()


db_session = Session()
db_session.commit()
users = db_session.query(UserModel).first()

# print('sukces')

start = time.time()

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", login_or_token="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")

print(g.get_rate_limit())

# Then play with your Github objects:
# repo = g.get_repo('kubernetes/kubernetes')
repo_name = 'ishepard/pydriller'
repo = g.get_repo('ishepard/pydriller')
repo_model = RepositoryModel()
saveToDb(repo_model)

print(repo.name)

pulls = repo.get_pulls('closed')

for pull in pulls:
    pull_request_model = PullRequestModel(hash=pull.id, repository_id=repo_model.id, status=pull.state, created_at=pull.created_at)
    saveToDb(pull_request_model)

    print(pull.number)

    getPullChecks(pull, pull_request_model)

done = time.time()
print("time spent:")
print(done - start)

