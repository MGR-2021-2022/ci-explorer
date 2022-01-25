# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import time
from typing import List

from github import Github, PaginatedList, CheckRun, PullRequest

from DbManager import DbManager
from SqlAlchemyBase import Session
from model.Commit import Commit as CommitModel
from model.Repository import Repository as RepositoryModel
from model.CheckRun import CheckRun as CheckRunModel
from model.PullRequest import PullRequest as PullRequestModel
from repository.UserRepository import UserRepository


def generateChangedFilesJson(files: List):
    files_json = {}
    for file in files:
        files_json[file.filename] = file.changes
    return files_json

def generateChangedLabelsJson(labels: PaginatedList):
    labels_json = {}
    for label in labels:
        labels_json[label] += label
    return label

def inspectChecks(checks: PaginatedList, commit_model: CommitModel):
    global db_manager
    order = 0

    for check in checks:
        order += 1
        check_model = CheckRunModel(github_id=check.id, name=check.name, check_suit_id=check.check_suite_id,
                                    status=check.status, conclusion=check.conclusion, order_number=order,
                                    total_count=checks.totalCount, commit_id=commit_model.id,
                                    started_at=check.started_at, finished_at=check.completed_at)
        db_manager.save_to_db(check_model)


def inspectCommits(commits: PaginatedList, pull_request_model: PullRequestModel):
    global db_manager, user_repository
    counter = 0
    for commit in commits:
        counter += 1
        user_model = user_repository.findOrCreate(name=commit.commit.author.name)
        files_changed = generateChangedFilesJson(commit.files)
        commit_model = CommitModel(hash=commit.sha, author_id=user_model.id, modified_lines=commit.stats.total,
                                   modified_files=files_changed, order_number=counter,
                                   created_at=commit.commit.author.date, pull_request_id=pull_request_model.id)
        db_manager.save_to_db(commit_model)
        inspectChecks(commit.get_check_runs(), commit_model)


db_session = Session()
db_manager = DbManager(db_session)
user_repository = UserRepository(db_manager)

g = Github(base_url="https://api.github.com", login_or_token="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")

repo_name = 'ishepard/pydriller'
repo = g.get_repo(repo_name)
language = repo.language
labels = repo.get_labels()
owner = repo.owner
user_model = user_repository.findOrCreate(owner.name)
repo_model = RepositoryModel(name=repo_name, owner_id=user_model.id)
db_manager.save_to_db(repo_model)

print(repo.name)

pulls = repo.get_pulls('closed')

for pull in pulls:
    pull_request_model = PullRequestModel(hash=pull.id, repository_id=repo_model.id, status=pull.state, created_at=pull.created_at)
    db_manager.save_to_db(pull_request_model)

    print(pull.number)

    inspectCommits(pull.get_commits(), pull_request_model)

