from db_setup import restart_db
import requests


API_LINK = 'http://127.0.0.1:4000/'


def create_users(amount):
    for i in range(amount):
        i = str(i)
        data = {
            'username': 'username'+i,
            'password': 'password',
            'name': 'name',
            'address': 'address',
            'bithdate': 'dd/mm/yyyy',
            'postal': '1234-123',
            'city': 'city',
            'country': 'country',
            'email': 'email'+i+'@email.com',
            'phone': '+351 999666333'
        }
        requests.post(url=API_LINK+'user', data=data)


def create_hotels(amount):
    for i in range(amount):
        i = str(i)
        data = {
            'name': ''+i,
            'city': ''+i,
            'country': ''+i,
            'price': i,
            'persons': i,
            'photos': ''+i,
            'description': i
        }
        requests.post(url=API_LINK+'hotel', data=data)


def create_estates(amount):
    for i in range(amount):
        i = str(i)
        data = {
            'name': ''+i,
            'owner_username': ''+i,
            'city': ''+i,
            'country': ''+i,
            'price': i,
            'persons': i,
            'description': i,
            'photos': ''+i
        }
        requests.post(url=API_LINK+'estate', data=data)


def create_transports(amount):
    for i in range(amount):
        i = str(i)
        data = {
            'origin_city': ''+i,
            'origin_country': ''+i,
            'destination_city': ''+i,
            'destination_country': ''+i,
            'company': ''+i,
            'price': i,
            'description': i,
            'method': ''+i
        }
        requests.post(url=API_LINK+'transport', data=data)


def create_rent_a_cars(amount):
    for i in range(amount):
        i = str(i)
        data = {
            'city': ''+i,
            'country': ''+i,
            'company': ''+i,
            'price': i,
            'model': ''+i,
            'description': i,
            'photos': ''+i
        }
        requests.post(url=API_LINK+'rentacar', data=data)


def create_attractions(amount):
    for i in range(amount):
        i = str(i)
        data = {
            'name': ''+i,
            'country': ''+i,
            'city': ''+i,
            'price': i,
            'description': i,
            'photos': ''+i
        }
        requests.post(url=API_LINK+'attraction', data=data)


def gen_test_db(amount):
    restart_db()
    create_users(amount)
    create_attractions(amount)
    create_hotels(amount)
    create_estates(amount)
    create_transports(amount)
    create_rent_a_cars(amount)


gen_test_db(5)
