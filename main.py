import time
import traceback
from typing import List

from github import Github, PaginatedList, CheckRun, PullRequest, RateLimitExceededException, Repository
from sqlalchemy import select, desc

from DbManager import DbManager
from SqlAlchemyBase import Session
from model.Commit import Commit as CommitModel
from model.Repository import Repository as RepositoryModel
from model.CheckRun import CheckRun as CheckRunModel
from model.PullRequest import PullRequest as PullRequestModel
from repository.RepositoryRepository import RepositoryRepository
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
    if checks == None:
        return
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
        user_model = user_repository.findOrCreate(name=commit.commit.author.email)
        files_changed = generateChangedFilesJson(commit.files)
        commit_model = CommitModel(hash=commit.sha, author_id=user_model.id, modified_lines=commit.stats.total,
                                   modified_files=files_changed, order_number=counter,
                                   created_at=commit.commit.committer.date, pull_request_id=pull_request_model.id)
        db_manager.save(commit_model, False)
        inspectChecks(commit.get_check_runs(), commit_model)


def set_db() -> (DbManager, UserRepository, RepositoryRepository, Session):
    db_session = Session()
    db_manager = DbManager(db_session)
    user_repository = UserRepository(db_manager)
    repository_repository = RepositoryRepository(db_manager)
    return db_manager, user_repository, repository_repository, db_session


def connect_repo():
    global g
    g = Github(base_url="https://api.github.com", login_or_token="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")


def save_repo(db_manager: DbManager, user_repository: UserRepository, repository_repository: RepositoryRepository
              ) -> (Repository, RepositoryModel):
    # repo_name = 'microsoft/vscode'
    # repo_name = 'django/django'
    # repo_name = 'bitcoin/bitcoin'
    # repo_name = 'facebook/lexical'
    # repo_name = 'hashicorp/terraform'
    # repo_name = 'laravel/framework'
    # repo_name = 'diasurgical/devilutionX'
    # repo_name = 'flutter/flutter'
    # repo_name = 'starship/starship'
    repo_name = 'microsoft/CBL-Mariner'
    #MarlinFirmware / Marlin
    # nuxt / framework

    repo = g.get_repo(repo_name)
    owner = repo.owner
    user_model = user_repository.findOrCreate(owner.login)
    repo_model = repository_repository.findOrCreate(name=repo_name, owner_id=user_model.id, created_at=repo.created_at, language=repo.language, topics=repo.get_topics())
    db_manager.save(repo_model)
    print(repo.name)
    return repo_model, repo


def get_last_pull_number(repo_model: RepositoryModel):
    if len(repo_model.pull_requests) == 0:
        return 0
    return db_session.execute(select(PullRequestModel.number).
                              where(PullRequestModel.repository_id == repo_model.id).order_by(desc("id"))).fetchone()[0]

def inspect_pull(pull: PullRequest, pull_request_model: PullRequestModel):

    commits = pull.get_commits()
    inspectCommits(pull.get_commits(), pull_request_model)
    print("---")
    print("Pull number(id): " + str(pull.number))
    print("Commits number: " + str(commits.totalCount))
    print("Api hits left: " + str(g.rate_limiting[0]))


def skip_pull(current: int, destination: int):
    return destination != 0 and destination is not None and current >= destination


def remove_pull_request(pull_request_model: PullRequestModel):
    global db_manager
    for commit_model in pull_request_model.commits:
        for check_model in commit_model.check_runs:
            db_manager.remove(check_model)
        db_manager.remove(commit_model)
    db_manager.remove(pull_request_model)

def remove_repo(repository_model: RepositoryModel):
    global db_manager
    for pull_model in repository_model.pull_requests:
        remove_pull_request(pull_model)
    db_manager.remove(repository_model)



def inspects_pulls(pulls, main_branch_name: str, last_pull_number = 0):
    """
    :param pulls: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequest.PullRequest`
    """
    pulls = iter(pulls)
    pull = next(pulls, 0)
    next_pull = True
    failed_pull = 0
    failed_pull_counter = 0
    previous = 0
    while pull != 0:
        if skip_pull(pull.number, last_pull_number):
            print("Already fetched. Skipping pull request with number:" + str(pull.number))
            try:
                previous = pull
                pull = next(pulls, 0)
            except Exception as e:
                print("Failed next(): 1")
                pull = previous
                pass
            continue
        if pull.base.ref != "main" and pull.base.ref != "master" and pull.base.ref != "develop":
            print("Not main. Skipping pull request with number:" + str(pull.number))
            try:
                previous = pull
                pull = next(pulls, 0)
            except Exception as e:
                print("Failed next(): 2")
                pull = previous
                pass
            continue
        try:
            pull_request_model = PullRequestModel(number=pull.number, repository_id=repo_model.id,
                                                  status=pull.state, merged=pull.merged,
                                                  created_at=pull.created_at)
            db_manager.save(pull_request_model, False)
            inspect_pull(pull, pull_request_model)
        except Exception as e:
            print("Fail due to internal error on PR: " + str(pull_request_model.number))
            if pull_request_model != None:
                remove_pull_request(pull_request_model)
                if failed_pull == pull_request_model.number and not isinstance(e, RateLimitExceededException):
                    failed_pull_counter += 1
                else:
                    failed_pull = pull_request_model.number
                    failed_pull_counter = 1

            if failed_pull_counter >= 5:
                pull_request_model = PullRequestModel(number=pull.number, failed_to_fetch=True)
                db_manager.save(pull_request_model)
                print(str(pull.number) + "marked as failed to fetch")
                next_pull = True
            else:
                next_pull = False
            traceback.print_exc()
            if isinstance(e, RateLimitExceededException):
                print("Waiting 10 min")
                time.sleep(600)
                next_pull = True
            pass
        if next_pull is True:
            try:
                previous = pull
                pull = next(pulls, 0)
            except Exception as e:
                print("Failed next(): 3")
                pull = previous
                pass
    repo_model.finished = True
    db_manager.save(repo_model)
    print("Successfully finished data download for: " + str(repo_model.name))


(db_manager, user_repository, repository_repository, db_session) = set_db()
connect_repo()
(repo_model, repo) = save_repo(db_manager, user_repository, repository_repository)

pulls = repo.get_pulls('closed')

# pull_to_rm = db_manager.query(PullRequestModel).filter(PullRequestModel.number==134402).first()
# remove_last_pull_request(pull_to_rm)
# remove_repo(repo_model)

for i in range(1, 100):
    last_pull_number = get_last_pull_number(repo_model)
    inspects_pulls(pulls, 'master', last_pull_number)
inspects_pulls(pulls, 'master', last_pull_number)


# usunąć globale
# przesunąć więcej do funkcji
# dodać typy i wyeliminować żółte opisy
# dodać wyszukiwanie repo samorzutnie

# dodac jaki master
# lepiej radzic sobie z errorami