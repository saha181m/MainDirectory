import requests
import json

def random_dog():

    params={
        'api_key':'e07f1a96-7b99-4f0d-91db-00668ea34a90',
        'fileSizeBytes':'342649'
    }
    response=requests.get('https://random.dog/woof.json',params=params).json()
    print(response)

random_dog()