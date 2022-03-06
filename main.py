import traceback
from typing import List

from github import Github, PaginatedList, CheckRun, PullRequest, RateLimitExceededException
from sqlalchemy import select, desc

from DbManager import DbManager
from SqlAlchemyBase import Session
from model.Commit import Commit as CommitModel
from model.Repository import Repository as RepositoryModel
from model.CheckRun import CheckRun as CheckRunModel
from model.PullRequest import PullRequest as PullRequestModel
from repository.RepositoryRepository import RepositoryRepository
from repository.UserRepository import UserRepository

db_manager = None
user_repository = None
repo = repo_model = None

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
        db_manager.save(check_model, False)

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
        db_manager.save(commit_model, False)
        inspectChecks(commit.get_check_runs(), commit_model)


def set_db():
    global db_manager, user_repository, repository_repository, db_session
    db_session = Session()
    db_manager = DbManager(db_session)
    user_repository = UserRepository(db_manager)
    repository_repository = RepositoryRepository(db_manager)


def connect_repo():
    global g
    g = Github(base_url="https://api.github.com", login_or_token="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")



def save_repo():
    global db_manager, user_repository, repo, repo_model
    # repo_name = 'ishepard/pydriller'
    repo_name = 'microsoft/vscode'
    repo = g.get_repo(repo_name)
    language = repo.language
    labels = repo.get_labels()
    owner = repo.owner
    user_model = user_repository.findOrCreate(owner.name)
    repo_model = repository_repository.findOrCreate(name=repo_name, owner_id=user_model.id)
    db_manager.save(repo_model)
    print(repo.name)


def get_last_pull_number(repo_model_id: int):
    if len(repo_model.pull_requests) == 0:
        return 0
    return db_session.execute(select(PullRequestModel.number).
                              where(PullRequestModel.repository_id == repo_model_id).order_by(desc("id"))).fetchone()[0]


def skip_pull(current: int, destination: int):
    print(current)
    return destination != 0 and destination is not None and current >= destination


def remove_last_pull_request(pull_request_model: PullRequestModel):
    global db_manager
    for commit_model in pull_request_model.commits:
        for check_model in commit_model.check_runs:
            db_manager.remove(check_model)
        db_manager.remove(commit_model)
    db_manager.remove(pull_request_model)


def inspects_pulls(pulls, last_pull_number = 0):
    global db_manager
    try:
        for pull in pulls:
            if skip_pull(pull.number, last_pull_number):
                continue
            pull_request_model = PullRequestModel(number=pull.number, repository_id=repo_model.id, status=pull.state, created_at=pull.created_at)
            db_manager.save(pull_request_model, False)

            commits = pull.get_commits()
            if(g.rate_limiting[0] > commits.totalCount * 10):
                inspectCommits(pull.get_commits(), pull_request_model)
            else:
                remove_last_pull_request(pull_request_model)
                print("Due to api limitations, not proceeded with pull request: " + str(pull.id))
                break
            print(pull.number)
            print(commits.totalCount)
            print(g.rate_limiting[0])
    except Exception as e:
        print("Fail due to internal error on PR: " + str(pull_request_model.number))
        remove_last_pull_request(pull_request_model)
        traceback.print_exc()
    repo_model.finished = True
    db_manager.save(repo_model)


set_db()
connect_repo()
save_repo()

pulls = repo.get_pulls('closed')
last_pull_number = get_last_pull_number(repo_model.id)
inspects_pulls(pulls, last_pull_number)


# czytelniejsze logi
# usunąć globale
# przesunąć więcej do funkcji
# dodać typy i wyeliminować żółte opisy
# dodać datę utworzenia repozytorium
# dodać language & labels
