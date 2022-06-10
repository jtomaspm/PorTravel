from settings import API_LINK, SEARCH_TERMS
import requests


def get_destination_id(obj, table):
    destinations = requests.get(API_LINK+'destination').json()
    print(obj)
    print(destinations)
    for d in destinations:
        if d['table_id'] == obj['id'] and d['table'] == table:
            return d['id']


def filter_data(query, data):
    res = []
    for elem in data:
        terms = []
        for term in SEARCH_TERMS:
            if term in elem:
                terms.append(elem[term])
        for t in terms:
            if query.lower() in t.lower():
                res.append(elem)
                break
    return res
