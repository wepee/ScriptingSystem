import logging
import datetime
import urllib.request
import zipfile
import json
import os
import time
import tarfile
import os.path

with open('./config.json', 'r') as file:
    data = json.load(file)


def getZip(url):
    to = "sav" + datetime.datetime.now().strftime(data["source"]["dateFormat"]) + ".zip"
    try:
        urllib.request.urlretrieve(url, to)
        logging.info("Telechargement du fichier %s effectuée avec succes ", data["source"]["name"])
        return to
    except Exception as e:
        logging.error(e)


def checkZip(zipName):
    with zipfile.ZipFile(zipName) as zip:
        if zip.namelist()[0].split(".")[-1] != data["source"]["ext"]:
            logging.error(zip.namelist())
            logging.error("Mauvais type : le fichier zippé ne contient pas de fichier db")
        else:
            metadata = os.stat(zipName)
            logging.info("Le fichier .db a été trouvé")
            logging.info("Date du fichier %s", time.localtime(metadata.st_mtime))


def extractZip(zipName):
    with zipfile.ZipFile(zipName, 'r') as zfile:
        zfile.extractall()


def makeTarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


# mise en place du fichier de log
logging.basicConfig(filename=data["log"]["filename"], level=logging.DEBUG, format='%(asctime)s -- %(levelname)s -- %(message)s')

zipName = getZip(data["source"]["url"]);

checkZip(zipName)

extractZip(zipName)

makeTarfile(zipName.split('.')[0] + ".tar.gz", zipName)
