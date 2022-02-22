from os import mkdir, path


def language():
    return 'en-US'


def checkFolders():
    if (path.exists('./inputs') == False):
        mkdir('inputs')
    if (path.exists('./outputs') == False):
        mkdir('outputs')
    if (path.exists('./outputs/exported-xlsx') == False):
        mkdir('outputs/exported-xlsx')
    if (path.exists('./outputs/merged-translations') == False):
        mkdir('outputs/merged-translations')
