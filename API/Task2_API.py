import requests
import json

def random_fox():

    params={
        'image':'https://randomfox.ca/floof/',
        'link':'https://randomfox.ca/?i=38'
    }
    response=requests.get('https://randomfox.ca/floof/',params=params).json()
    print(response)

random_fox()