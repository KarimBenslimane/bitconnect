import base64

USER = 'cHl0aG9u'
PSWD = 'cm9vdA=='


def getUser():
    return base64.b64decode(USER).decode('utf-8')


def getPass():
    return base64.b64decode(PSWD).decode('utf-8')
