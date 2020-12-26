from functions import *
from download import *
from sftp import *
from mail import *

try:

    # On définit le nom de la sauvegarde
    fileName = "sav" + datetime.datetime.now().strftime(data["source"]["dateFormat"])

    # on definit le nom du zip de sauvegarde
    zipName = fileName + ".zip"

    # on definit le nom du tar.gz de sauvegarde
    tarName = fileName + ".tar.gz"

    # on nettoye les fichiers temporaires qui pourrait creer des conflits
    clean(fileName)

    # on va chercher le zip sur le server web
    getZip(data["source"]["url"])

    # on verifie le contenu du zip
    checkZip(zipName)

    # on dézip le fichier
    extractZip(zipName)

    # on le recompresse au format Tar.ge
    makeTarfile(tarName, data["source"]["name"])

    # on l'envoie sur le serveur distant
    sftpUpload(tarName)

    # on envoie un mail en cas de réussite
    mail("réussite", data["mail"]["to"], "corps")

except Exception as e:
    print(e)
    logging.critical(e)
    mail("echec", data["mail"]["to"], e)
