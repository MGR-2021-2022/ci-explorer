import csv

from pydriller import Repository, Commit, Git
from git import Commit as GitCommit, Repo

# repo = Repo('pydriller')
git = Git('pydriller')
# commit = Repository('pydriller').git.get_commit('948c0a69420c51a5d0291e4b2a24c898d4cdf15a')
commits_number = 0
changed_files = 0
changed_lines = 0
with open('commits_after_fail.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        if(row[0] != '9867c4812860097f1d14f2a0de007cba13a1ec90' and row[0] != '02c6cb8f0328f9b7c830f1620667ccab9bf5ea18'):
            if (row[0] != 'a4a2e5feb4d4ec2f4355eecdb9f3189797f04541' and row[0] != '759a51dd4c3182d09e2fae85bc853e093c050f6c'):
                if (row[0] != '251117390f9801ec9c395811d6aa5469a9896c5e' and row[0] != '6b62a3c8fc0a203a15f04ab84263bcf9f3fc74fa'):
                    if (row[0] != '6a74f185e45633b955d5c1c29852b2dea7cec773' and row[0] != 'e07d075a54a4126a2ee0781be529ee1f3ecfc180'):
                        if (row[0] != 'fbd96ac6c02363fc91e456d9442dd09cdf6cc8c3' and row[0] != '81fcb5567d6e8226184f6596fe4c12fb58c1eb69'):
                            if (row[0] != '89bf7766341cf0e3d3d1d50ac626cbe8065f8b8e' and row[0] != '52ca36dbef24650b85795abe94b61e85797e2d16'):
                                commit = git.get_commit(row[0])
                                print('commit: ' + row[0])
                                print('changed files number: ' + str(len(commit.modified_files)))
                                print('changed lines number: ' + str(commit.lines))
                                commits_number += 1;
                                changed_files += len(commit.modified_files)
                                changed_lines += commit.lines

print('total commits: ' + str(commits_number))
print('total modified files: ' + str(changed_files))
print('avg modified files: ' + str(changed_files/commits_number))
print('total modified lines: ' + str(changed_lines))
print('avg modified lines: ' + str(changed_lines/commits_number))