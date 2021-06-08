import configparser

config=configparser.RawConfigParser()
config.read('.\\config\\confiq.ini')

class Readconfiq():

    @staticmethod
    def getUrl(self):
        url=config.get('Basic Info','baseUrl')
        return url

    def getUseremail(self):
        useremail=config.get('Basic Info','userName')

    def getPassword(self):
        password = config.get('Basic Info', 'password')