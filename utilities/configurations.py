import configparser

def getConfig():
    f = open('./utilities/properties.ini', 'r') #test if path is correct
    config = configparser.ConfigParser()
    config.read('./utilities/properties.ini')
    return config

def getUsername() -> str:
    return 'echan03'

def getToken() -> str:
    return 'secret'

