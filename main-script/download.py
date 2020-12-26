import logging
import json
import datetime
import urllib.request

with open('./config.json', 'r') as file:
    data = json.load(file)

def getZip(url):
    to = "sav" + datetime.datetime.now().strftime(data["source"]["dateFormat"])
    try:
        urllib.request.urlretrieve(url, to + ".zip")
        logging.info("Telechargement du fichier %s effectuée avec succes ", data["source"]["zipName"])
        return to
    except Exception as e:
        logging.error(e)