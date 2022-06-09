from settings import API_LINK
import requests


def get_destination_id(obj, table):
    destinations = requests.get(API_LINK+'destination').json()
    print(obj)
    print(destinations)
    for d in destinations:
        if d['table_id'] == obj['id'] and d['table'] == table:
            return d['id']
