import pytest
import requests
import json
from Task3_API import *

@pytest.fixture()
def post():
    return RickAndMorty
class TestNewAPICharacter:
    def test_get_new_api(self,post):
        try:
            assert post.get_new_api(self)==200
            print("\n")
            print(f"Статус кода:{post.get_new_api(self)}")
        except AssertionError:
            print('код неверный')

    def test_get_new_post_character(self,post):
        try:
            assert post.get_new_post_character(self)['name'] == 'Morty Smith'
            print("\n")
            print(f"Name:{post.get_new_post_character(self)['name']}")
        except:
            print('Другое значение name')