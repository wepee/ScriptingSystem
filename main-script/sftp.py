import json
import logging
import pysftp

with open('./config.json', 'r') as file:
    data = json.load(file)

def sftpUpload(fileName):
    try:
        with pysftp.Connection(data["sftp"]["hostname"], username=data["sftp"]["username"],
                               password=data["sftp"]["password"]) as sftp:
            sftp.put(fileName)  # upload file to public/ on remote
    except Exception as e:
        logging.error(e)


def sftpDownload(fileName):
    try:
        with pysftp.Connection(data["sftp"]["hostname"], username=data["sftp"]["username"],
                               password=data["sftp"]["password"]) as sftp:
            sftp.get(fileName)  # get a remote file
    except Exception as e:
        logging.error(e)
