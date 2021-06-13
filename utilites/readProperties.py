import configparser

config=configparser.RawConfigParser()
config.read('.\\config\\confiq.ini')

class Readconfiq():

    @staticmethod
    def getUrl():
        url=config.get('Basic Info','baseUrl')
        return url

    @staticmethod
    def getUseremail():
        useremail=config.get('Basic Info','userName')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('Basic Info', 'password')
        return password