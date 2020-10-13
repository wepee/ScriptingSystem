from functions import *


try:

    fileName = "sav" + datetime.datetime.now().strftime(data["source"]["dateFormat"])

    zipName = fileName + ".zip"

    tarName = fileName + ".tar.gz"

    clean(fileName)

    getZip(data["source"]["url"])

    zipName = fileName + ".zip"

    checkZip(zipName)

    extractZip(zipName)

    makeTarfile(tarName, data["source"]["name"])

    upload(tarName)

except Exception as e:
    print(e)
    logging.critical(e)
