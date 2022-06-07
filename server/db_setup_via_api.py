from unicodedata import name
from db_setup import restart_db
import requests


API_LINK = 'http://127.0.0.1:4000/'


def create_users(amount):
    amount = 5
    usernames = ['john', 'ed', 'psi', 'kyle', 'tim']
    passwords = ['123', '123', '123', '123', '123']
    names = ['john', 'ed', 'psi', 'kyle', 'tim']
    address = ['Travessa da Rua do Eucalipto', 'Travessa da Rua do Eucalipto',
               'Travessa da Rua do Eucalipto', 'Travessa da Rua do Eucalipto', 'Travessa da Rua do Eucalipto']
    birthday = ['18/10/1954', '23/12/1999',
                '1/10/1978', '11/7/2001', '18/9/1979']
    postals = ['6300 - 132', '6300 - 132',
               '6300 - 132', '6300 - 132', '6300 - 132']
    citys = ['Guarda', 'Guarda', 'Guarda', 'Guarda', 'Guarda']
    countrys = ['Portugal', 'Portugal', 'Portugal', 'Portugal ', 'Portugal']
    email = ['john@ua.pt', 'ed@ua.pt', 'psi@ua.pt', 'kyle@ua.pt', 'tim@ua.pt']
    phone = ['961211212', '961211212', '961211212', '961211212', '961212141']
    for i in range(amount):
        
        data = {
            'username': usernames[i] ,
            'password': passwords[i] ,
            'name': names[i],
            'address': address[i],
            'bithdate': birthday[i],
            'postal': postals[i],
            'city': citys[i],
            'country': countrys[i],
            'email': email[i],
            'phone': phone[i]
        }
        requests.post(url=API_LINK+'user', data=data)


def create_hotels(amount):
    amount = 5 
    names = ['Axix' , 'Dorals', 'PortoInn', 'Dafcan' , ' Irdalis']
    citys=['Porto, ' , ' Lisboa ' , ' Guarda' ,' Aveiro' , ' Coimbra']
    countrys=['Portugal' , 'Portugal' , 'Portugal' , 'Portugal' , 'Portugal'  ]
    price = ['49.55' , '43.55' , '419.55' , '479.55' , '42.55'  ]
    persons = [ '1' , '1' , '2' , '2' , '1' ]
    photos = [ '1' , '1' , '2' , '2' , '1' ]
    description = ['Melhor Hotel no Porto', 'Venha para uma noite relaxada','Uma hótima estadia para casais' , ' Venha desfrutar com a sua parceira na melhor noite oferecida pelo Dafcan', 'Irdalis, onde garantimos a sua satisfacão']

    for i in range(amount):
        i2 = str(i)
        data = {
            'name':names[i],
            'city':citys[i],
            'country':countrys[i],
            'price':price[i],
            'persons':persons[i],
            'photos':photos[i], 
            'description':description[i],
        }
        requests.post(url=API_LINK+'hotel', data=data)


def create_estates(amount):
    amount = 5 
    names = ['Axix' , 'Dorals', 'PortoInn', 'Dafcan' , ' Irdalis']
    owner_username = ['john','ed','psi','kyle','tim']    
    citys=['Porto, ' , ' Lisboa ' , ' Guarda' ,' Aveiro' , ' Coimbra']
    countrys=['Portugal' , 'Portugal' , 'Portugal' , 'Portugal' , 'Portugal'  ]
    price = ['49.55' , '43.55' , '419.55' , '479.55' , '42.55'  ]
    persons = [ '1' , '1' , '2' , '2' , '1' ]
    photos = [ '1' , '1' , '2' , '2' , '1' ]
    description = ['Melhor Hotel no Porto', 'Venha para uma noite relaxada','Uma hótima estadia para casais' , ' Venha desfrutar com a sua parceira na melhor noite oferecida pelo Dafcan', 'Irdalis, onde garantimos a sua satisfacão']

    for i in range(amount):
        i = str(i)
        data = {
            
            'owner_username': owner_username[i],
            'name':names[i],
            'city':citys[i],
            'country':countrys[i],
            'price':price[i],
            'persons':persons[i],
            'photos':photos[i], 
            'description':description[i],
        }
        requests.post(url=API_LINK+'estate', data=data)


def create_transports(amount):
    origin_city = ["Porto", "Aveiro", "Algarve", "Aveiro", "Lisboa"]
    origin_country = ["Portugal", "Portugal",
                      "Portugal", "Portugal", "Portugal"]
    destination_city = ["Barcelona", "Madrid", "Salamanca", "Vigo", "Sevilha"]
    destination_country = ["Espanha", "Espanha",
                           "Espanha", "Espanha", "Espanha"]
    company = ["UA", "UA", "UA", "UA", "UA"]
    price = ["2", "2", "2", "2", "2"]
    description = ["qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja",
                   "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja"]
    method = ["Airplane", "Airplane", "Space Ship", "Bus", "Train"]
    for i in range(amount):
        data = {
            'origin_city': origin_city[i],
            'origin_country': origin_country[i],
            'destination_city': destination_city[i],
            'destination_country': destination_country[i],
            'company': company[i],
            'price': price[i],
            'description': description[i],
            'method': method[i]

        }
        requests.post(url=API_LINK+'transport', data=data)


def create_rent_a_cars(amount):
    countries = ["Portugal", "Portugal", "Portugal", "Portugal", "Portugal"]
    cities = ["Porto", "Aveiro", "Algarve", "Aveiro", "Lisboa"]
    companies = ["UA", "UA", "UA", "UA", "UA"]
    prices = ["10", "15", "5", "3", "0"]
    models = ["Audi", "BMW", "Renault", "Porshe", "Lamborghini"]
    description = ["qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja",
                   "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja"]
    photos = ["2", "2", "2", "2", "2"]
    for i in range(amount):
        data = {
            'city': cities[i],
            'country': countries[i],
            'company': companies[i],
            'price': prices[i],
            'model': models[i],
            'description': descriptions[i],
            'photos': photos[i]
        }
        requests.post(url=API_LINK+'rentacar', data=data)


def create_attractions(amount):
    amount = 5
    names = ["Tour da Cidade", "Cozinha do rei",
             "Teatro", "Cinema", "Amoreiras"]
    countries = ["Portugal", "Portugal", "Portugal", "Portugal", "Portugal"]
    cities = ["Porto", "Aveiro", "Algarve", "Aveiro", "Lisboa"]
    prices = ["10", "15", "5", "3", "0"]
    description = ["qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja",
                   "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja", "qpwjidpoqwjphfwehpofiaj fjads fadsp+jf a jdf+jdasifja"]
    photos = ["2", "2", "2", "2", "2"]
    for i in range(amount):
        data = {
            'name': names[i],
            'country': countries[i],
            'city': cities[i],
            'price': prices[i],
            'description': description[i],
            'photos': photos[i]
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
