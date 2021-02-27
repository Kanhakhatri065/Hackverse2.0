"""
    Team: Babayaga
    Author: Kanha Khatri
"""
import os
import pathlib
from git import Repo
from zipfile import ZipFile


def clone_repo(repo_link, repo_name):
    destination_folder_path = str(pathlib.Path().absolute()) + '/' + repo_name
    print(destination_folder_path)
    Repo.clone_from(repo_link, destination_folder_path)


def compiling_github_repo(repo_name, user_id):
    dir_listing = os.listdir(str(os.getcwd()) + '/' + repo_name)
    files_present = []

    for file in dir_listing:
        files_present.append(file)

    shell_command = "cd " + str(pathlib.Path().absolute()) + "/" + repo_name + " && make"
    os.system(shell_command)

    dir_listing = os.listdir(str(os.getcwd()) + '/' + repo_name)

    compiled_files = []
    for file in dir_listing:
        if file in files_present:
            continue
        else:
            compiled_files.append(file)

    if len(compiled_files) == 0:
        os.system('rm -rf ' + repo_name + '/')
        return 0

    zip_file = ZipFile(str(user_id) + '.zip', 'w')
    for file in compiled_files:
        os.system("cd " + repo_name + "/ && mv " + str(file) + " ../")
        zip_file.write(str(file))
        os.system("mv " + str(file) + " " + repo_name + "/")

    zip_file.close()
    os.system('rm -rf ' + repo_name + '/')

    return 1


def clone_and_compile(repo_link, user_id):
    repo_name = ''
    count_forward_slashes = 0

    if repo_link.find("https://github.com") == -1 and repo_link.find("https://www.github.com") == -1:
        return 'no-git-repo'

    for ch in repo_link:
        if ch == '/':
            count_forward_slashes += 1
        else:
            if count_forward_slashes >= 4:
                repo_name += ch

    if repo_name.find('.git') != -1:
        repo_name = repo_name[:-(len('.git'))]
    else:
        repo_link += '.git'

    clone_repo(repo_link, repo_name)

    flag = compiling_github_repo(repo_name, user_id)

    if flag == 0:
        return 'xxx-no-comp'

    return repo_name
