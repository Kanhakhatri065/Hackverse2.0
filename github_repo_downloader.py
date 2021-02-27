"""
    Team: Babayaga
    Written by: Kanha Khatri
"""
import os
import pathlib
from git import Repo
from zipfile import ZipFile


def clone_repo(repo_link, repo_name):
    destination_folder_path = str(pathlib.Path().absolute()) + '/' + repo_name
    print(destination_folder_path)
    Repo.clone_from(repo_link, destination_folder_path)


def compiling_github_repo(repo_name):
    dir_listing = os.listdir(str(os.getcwd()) + '/' + repo_name)
    files_present = []

    for file in dir_listing:
        files_present.append(file)
    print("files present before compilation")
    print(files_present)

    shell_command = "cd " + str(pathlib.Path().absolute()) + "/" + repo_name + " && make"
    os.system(shell_command)

    dir_listing = os.listdir(str(os.getcwd()) + '/' + repo_name)

    compiled_files = []
    for file in dir_listing:
        if file in files_present:
            continue
        else:
            compiled_files.append(file)

    print("Files added to after compiling")
    print(compiled_files)

    if len(compiled_files) == 0:
        return 0

    zip_file = ZipFile("compiled_files.zip", 'w')
    for file in compiled_files:
        print(str(file))
        os.system("cd " + repo_name + "/ && mv " + str(file) + " ../")
        zip_file.write(str(file))
        os.system("mv " + str(file) + " " + repo_name + "/")

    zip_file.close()

    return 1


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
    else:
        repo_link += '.git'

    clone_repo(repo_link, repo_name)

    flag = compiling_github_repo(repo_name)

    if flag == 0:
        print("No files were compiled")
    else:
        print("Compiled files zipped in compiled_files.zip")


if __name__ == "__main__":
    print("Link of the github repo")
    repo_link = input()
    clone_and_compile(repo_link)
