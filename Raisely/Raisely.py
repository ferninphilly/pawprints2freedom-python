import configparser
import requests

class Raisely():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        if len(config.sections()) <= 0:
            print("config.ini not detected! Please put config.ini in root directory!")
        self.config = config['raisely']
        self.baseURL = self.config['baseURL']
        self.headers = {'Authorization': f"Bearer {self.config['apikey']}","content-type":"application/json"}
        print("Here is the baseURL :",self.config['baseURL'])
        
        
    def get_me_data(self):
        url=f"{self.baseURL}/users/me"
        resp = requests.get(url=url, headers=self.headers)
        data = resp.text
        print("here is the data: ",data)
        
    def get_donations_data(self):
        url=f"{self.baseURL}/donations?createdAtFrom=2024-05-09"
        resp = requests.get(url=url, headers=self.headers)
        data = resp.json()
        print("here are the donations: ",data)