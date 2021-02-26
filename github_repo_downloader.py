import os
import pathlib
from git import Repo


def clone_repo(repo_link, repo_name):
    destination_folder_path = str(pathlib.Path().absolute()) + '/' + repo_name
    print(destination_folder_path)
    Repo.clone_from(repo_link, destination_folder_path)


def compiling_github_repo(repo_name):
    shell_command = "cd " + str(pathlib.Path().absolute()) + "/" + repo_name + " && make"
    os.system(shell_command)


def clone_and_compile(repo_link):
    repo_name = ''
    count_forward_slashes = 0
    for ch in repo_link:
        if ch == '/':
            count_forward_slashes += 1
        else:
            if count_forward_slashes >= 4:
                repo_name += ch

    if repo_name.find('.git') != -1:
        repo_name = repo_name[:-(len('.git'))]

    clone_repo(repo_link, repo_name)

    compiling_github_repo(repo_name)


if __name__ == "__main__":
    print("Link of the github repo")
    repo_link = input()
    clone_and_compile(repo_link)
