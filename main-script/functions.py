import logging
import datetime
import urllib.request
import zipfile
import json
import os
import tarfile
import os.path
import pysftp

with open('./config.json', 'r') as file:
    data = json.load(file)

# mise en place du fichier de log
logging.basicConfig(filename=data["log"]["filename"], level=logging.DEBUG,
                    format='%(asctime)s -- %(levelname)s -- %(message)s')

def clean(fileName):
    logging.info("Nettoyage de la dernière sauvegarde")
    files = {fileName + '.zip', fileName + '.tar.gz', 'dumb.db'}
    for i in files:
        if os.path.exists(i):
            os.remove(i)

def getZip(url):
    to = "sav" + datetime.datetime.now().strftime(data["source"]["dateFormat"])
    try:
        urllib.request.urlretrieve(url, to + ".zip")
        logging.info("Telechargement du fichier %s effectuée avec succes ", data["source"]["zipName"])
        return to
    except Exception as e:
        logging.error(e)


def checkZip(zipName):
    logging.info("verifiation du zip :" + zipName )
    try:
        with zipfile.ZipFile(zipName) as zip:
            if zip.namelist()[0].split(".")[-1] != data["source"]["ext"]:
                raise NameError("Mauvais type : le fichier zippé ne contient pas de fichier db")
            else:
                date = (datetime.datetime(*zip.infolist()[0].date_time[0:6]))
                logging.info("Le fichier .db a été trouvé")
                logging.info("Date du fichier : " + str(date))
    except Exception as e:
        logging.error(e)


def extractZip(zipName):
    logging.info("Extraction du fichier :" + zipName )
    try:
        with zipfile.ZipFile(zipName, 'r') as zfile:
            zfile.extractall()
    except Exception as e:
        logging.error(e)


def makeTarfile(output_filename, source_dir):
    logging.info("Compression en tar.gz du fichier :" + output_filename )
    try:
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        logging.info("L'archive %s a bien été crée !", output_filename)
    except Exception as e:
        logging.error(e)


def upload(fileName):
    try:
        with pysftp.Connection(data["dest"]["hostname"], username=data["dest"]["username"], password=data["dest"]["password"]) as sftp:
            sftp.put(fileName)  # upload file to public/ on remote
    except Exception as e:
        print(e)


def get(fileName):
    try:
        with pysftp.Connection(data["dest"]["hostname"], username=data["dest"]["username"], password=data["dest"]["password"]) as sftp:
            sftp.get(fileName)  # get a remote file
    except Exception as e:
        print(e)

