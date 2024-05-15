import configparser
import requests

class Facebook():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        if len(config.sections()) <= 0:
            print("config.ini not detected! Please put config.ini in root directory!")
        self.config = config['facebook']
        
    def get_me_data(self):
        url=f"{self.config['baseURL']}/me?access_token={self.config['userToken']}"   
        resp = requests.get(url=url)
        data = resp.json()
        print("here is the data: ",data)
        
        