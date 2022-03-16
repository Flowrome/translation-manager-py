from os import mkdir, path
from tabnanny import check


def language():
    return 'en-US'


def checkFolders():
    if (path.exists('./inputs') == False):
        mkdir('inputs')
    if (path.exists('./inputs-multiple') == False):
        mkdir('inputs')
    if (path.exists('./outputs') == False):
        mkdir('outputs')
    if (path.exists('./outputs/exported-xlsx') == False):
        mkdir('outputs/exported-xlsx')
    if (path.exists('./outputs/exported-xlsx-multiple') == False):
        mkdir('outputs/exported-xlsx-multiple')
    if (path.exists('./outputs/merged-translations') == False):
        mkdir('outputs/merged-translations')
    if (path.exists('./outputs/merged-translations-multiple') == False):
        mkdir('outputs/merged-translations-multiple')


checkFolders()
