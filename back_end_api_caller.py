"""
    Team:Babayaga
    Author: Kanha Khatri
"""
import requests
import github_repo_downloader
from firebase_admin import credentials, initialize_app, storage
import os


class apiCaller:
    def __init__(self):
        cred = credentials.Certificate("apiKey.json")
        initialize_app(cred, {'storageBucket': "distributed-compiler.appspot.com"})
        self.host_id = 0
        self.git_url = ''
        self.user_id = ''
        self.zip_file_download_link = ''
        self.repo_name = ''
        self.file_name = ''
        self.node = ''

    def get_job(self):
        is_job_available = 'None'
        while is_job_available == 'None':
            response = requests.get("https://distributed-compiler.herokuapp.com/api/getJob/")
            is_job_available = response.json()['git']
        job = response.json()
        self.git_url = job['git']
        self.user_id = job['id']
        self.repo_name = github_repo_downloader.clone_and_compile(self.git_url, self.user_id)
        self.node = job['node']
        self.file_name = str(self.user_id) + '.zip'
        bucket = storage.bucket()
        blob = bucket.blob(self.file_name)
        blob.upload_from_filename(self.file_name)
        blob.make_public()
        self.zip_file_download_link = blob.public_url
        os.system('rm ' + self.file_name)
        os.system('rm -rf ' + self.repo_name + '/')

        status_code = 9
        while status_code == 9:
            response = requests.get("https://distributed-compiler.herokuapp.com/api/jobDone/?host="
                                + str(self.host_id) + "&user=" + self.user_id +
                                "&down=" + self.zip_file_download_link + "&node=" +
                                self.node)
            status_code = response.json()['code']


if __name__ == "__main__":
    ap = apiCaller()
    ap.get_job()