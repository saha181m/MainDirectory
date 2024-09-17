import requests
import json


class RickAndMorty:
    def __init__(self,body):
        self.body=body


    def get_new_api(self):
        self.body = json.dumps({
                "characters": "https://rickandmortyapi.com/api/character",
                "locations": "https://rickandmortyapi.com/api/location",
                "episodes": "https://rickandmortyapi.com/api/episode"
        })
        self.response = requests.get('https://rickandmortyapi.com/api', data=self.body)
        return self.response.status_code


    def get_new_post_character(self):
        self.response = requests.get('https://rickandmortyapi.com/api/character/2')
        return self.response.json()





