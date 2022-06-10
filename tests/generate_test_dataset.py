
import requests


API_LINK = 'http://127.0.0.1:4000/'


def upload_image(filename):
    file = {'file': open(filename, 'rb')}
    return requests.post(API_LINK+'upload', files=file).text


def convert_photos(photos):
    return [upload_image(photo) for photo in photos]


def create_users():
    usernames = ['john', 'ed', 'admin', 'kyle', 'tim']
    passwords = ['123', '123', '123', '123', '123']
    names = ['John Doe', 'Edward Dji', 'Admin', 'Kyle Stwart', 'Tim Taylor']
    address = ['Travessa da Rua do Eucalipto', 'Travessa da Rua do Eucalipto',
               'Travessa da Rua do Eucalipto', 'Travessa da Rua do Eucalipto', 'Travessa da Rua do Eucalipto']
    birthday = ['18/10/1954', '23/12/1999',
                '1/10/1978', '11/7/2001', '18/9/1979']
    postals = ['6300 - 132', '6300 - 132',
               '6300 - 132', '6300 - 132', '6300 - 132']
    citys = ['Guarda', 'Guarda', 'Guarda', 'Guarda', 'Guarda']
    countrys = ['Portugal', 'Portugal', 'Portugal', 'Portugal ', 'Portugal']
    email = ['john@ua.pt', 'ed@ua.pt',
             'admin@ua.pt', 'kyle@ua.pt', 'tim@ua.pt']
    phone = ['961211212', '961211212', '961211212', '961211212', '961212141']
    for i in range(5):

        data = {
            'username': usernames[i],
            'password': passwords[i],
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


def create_hotels():
    names = ['Axix', 'Dorals', 'PortoInn', 'Dafcan', ' Irdalis']
    citys = ['Porto ', ' Lisboa ', ' Guarda', ' Aveiro', ' Coimbra']
    countrys = ['Portugal', 'Portugal', 'Portugal', 'Portugal', 'Portugal']
    price = ['49.55', '43.55', '419.55', '479.55', '42.55']
    persons = ['1', '1', '2', '2', '1']
    photos = convert_photos(['hotel0.jpg', 'hotel1.jpg',
                             'hotel2.jpg', 'hotel3.jpeg', 'hotel4.jpg'])
    description = [
        'O hotel ocupa um antigo palácio do século XIX – Casa Daurella® - ampliado e atualizado com o máximo rigor arquitectónico para criar um hotel moderno, funcional e de grande categoria no qual coexistem a arte e a singularidade do passado com o conforto mais actual.',
        'Este luxuoso hotel boutique, situado num edifício histórico do século XIX restaurado, conta com elegantes e confortáveis quartos totalmente renovados, desenhados para oferecer o máximo de bem-estar aos seus hóspedes. ',
        'O nosso hotel conta com uma magnífica piscina ao ar livre na açoteia e uma zona de solário com vistas para o centro da cidade, que tornarão a sua estadia connosco ainda mais agradável. ',
        'Arte e cultura? Lojas de design e vida noturna? Monumentos históricos e gastronomia? O que quer que esteja à procura, o nosso hotel boutique no centro de é a opção perfeita para desfrutar desta linda cidade no seu melhor momento. ',
        'Wi-Fi gratuito, mini-ginásio, sauna, espaço negócios e oferta vasta de salas para reuniões e eventos de todos os tipos.'
    ]

    for i in range(5):
        data = {
            'name': names[i],
            'city': citys[i],
            'country': countrys[i],
            'price': price[i],
            'persons': persons[i],
            'photos': photos[i],
            'description': description[i],
        }
        requests.post(url=API_LINK+'hotel', data=data)


def create_estates():
    names = ['Porto Resort', 'Lisbon Open', 'Nortenho', 'Ria Pia', 'Queima']
    owner_username = ['john', 'ed', 'john', 'kyle', 'tim']
    citys = ['Porto, ', ' Lisboa ', ' Guarda', ' Aveiro', ' Coimbra']
    countrys = ['Portugal', 'Portugal', 'Portugal', 'Portugal', 'Portugal']
    price = ['49.55', '43.55', '419.55', '479.55', '42.55']
    persons = ['1', '1', '2', '2', '1']
    photos = convert_photos(['estate0.png', 'estate1.jpeg',
                             'estate2.jpeg', 'estate3.jpeg', 'estate4.jpeg'])
    description = [
        'Casa de Campo no Litoral: Sauna, Caiaques e Cinema em Casa',
        'Apartamento na Praça do Centro Histórico com Lareira e Escritório Residencial',
        'Cabana Própria para Crianças Perto de Trilhos de Caminhada e do Lago',
        'Venha desfrutar com a sua parceira na melhor noite oferecida pelo Dafcan',
        'Irdalis, onde garantimos a sua satisfacão e claro a do seu parceiro!'
    ]

    for i in range(5):
        i = (i)
        data = {

            'owner_username': owner_username[i],
            'name': names[i],
            'city': citys[i],
            'country': countrys[i],
            'price': price[i],
            'persons': persons[i],
            'photos': photos[i],
            'description': description[i],
        }
        requests.post(url=API_LINK+'estate', data=data)


def create_transports():
    origin_city = ["Porto", "Aveiro", "Algarve", "Aveiro", "Lisboa"]
    origin_country = ["Portugal", "Portugal",
                      "Portugal", "Portugal", "Portugal"]
    destination_city = ["Barcelona", "Madrid", "Salamanca", "Vigo", "Sevilha"]
    destination_country = ["Espanha", "Espanha",
                           "Espanha", "Espanha", "Espanha"]
    company = ["TAP", "TAP", "Seas", "FlixBus", "CP"]
    price = ["11", "12", "13", "14", "15"]
    photos = convert_photos(['trans0.jpeg', 'trans1.jpg',
                             'trans2.jpg', 'trans3.jpg', 'trans4.jpg'])
    description = [
        'A TAP disponibiliza tarifas à medida das suas viagens e para todos os perfis de viajante',
        'A TAP disponibiliza tarifas à medida das suas viagens e para todos os perfis de viajante',
        'Para facilitar um transporte o mais económico e ecológico possível',
        'Save with FlixBus! Save money with our unbeatably cheap bus tickets, save time with our detailed bus schedules and punctual buses and save the environment',
        'Consulte os horários dos diferentes comboios da CP. Disponível online para os comboios Alfa Pendular, Intercidades, Internacional, Regional e Urbanos.'
    ]
    method = ["Avião", "Avião", "Barco", "Autocarro", "Comboio"]
    for i in range(5):
        data = {
            'origin_city': origin_city[i],
            'origin_country': origin_country[i],
            'destination_city': destination_city[i],
            'destination_country': destination_country[i],
            'company': company[i],
            'price': price[i],
            'photos': photos[i],
            'description': description[i],
            'method': method[i]

        }
        requests.post(url=API_LINK+'transport', data=data)


def create_rent_a_cars():
    countries = ["Portugal", "Portugal", "Portugal", "Portugal", "Portugal"]
    cities = ["Porto", "Aveiro", "Algarve", "Aveiro", "Lisboa"]
    companies = ["UA", "UA", "UA", "UA", "UA"]
    prices = ["10", "15", "16", "17", "18"]
    models = ["Audi R8", "BMW e30", "Renault Kiger",
              "Porsche 911", "Lamborghini"]
    photos = convert_photos(['car0.jpg', 'car1.jpg',
                             'car2.jpeg', 'car3.jpeg', 'car4.jpeg'])
    description = [
        'O Audi R8 Coupé V10 quattro é um puro Audi ao nível mais elevado',
        'The BMW E30 is the second generation of BMW 3 Series, which was produced from 1982 to 1994 and replaced the E21 3 Series.',
        'Go where your curiosity takes you with the Renault Kiger. Its stunning yet muscular SUV stance is crafted to complement your free spirit.',
        'The legendary 911. The identity of the Porsche brand - since 1963.',
        'The Lamborghini Huracán is the perfect fusion of technology and design. With its crisp, streamlined lines, designed to cut through the air and tame the road.'
    ]
    for i in range(5):
        data = {
            'city': cities[i],
            'country': countries[i],
            'company': companies[i],
            'price': prices[i],
            'model': models[i],
            'description': description[i],
            'photos': photos[i]
        }
        requests.post(url=API_LINK+'rentacar', data=data)


def create_attractions():
    names = ["Tour da Cidade", "O Bairro",
             "Teatro", "Cinema", "Rooftop Amoreiras"]
    countries = ["Portugal", "Portugal", "Portugal", "Portugal", "Portugal"]
    cities = ["Porto", "Aveiro", "Algarve", "Aveiro", "Lisboa"]
    prices = ["10", "15", "5", "3", "5"]
    photos = convert_photos(['att0.jpg', 'att1.jpg',
                             'att2.jpeg', 'att3.jpg', 'att4.jpg'])
    description = [
        "Porto or Oporto is the second-largest city in Portugal, the capital of the Porto District, and one of the Iberian Peninsula's major urban areas.",
        'Um espaço descontraído e confortável com uma cozinha única.',
        'O Teatro e o GrETUA promovem um programa de leituras de textos dramáticos, com especial incidência em dramaturgia contemporânea.',
        'Novo Bilhete Família! É mesmo à tua medida · Em cartaz · Próximas Estreias · IMAX · Espetáculos · Pré-Venda.',
        'O Miradouro Amoreiras 360 Panoramic View é um espaço mágico na cidade de Lisboa. Um local singular que permite aos seus visitantes disfrutarem de uma vista.'
    ]
    for i in range(5):
        data = {
            'name': names[i],
            'country': countries[i],
            'city': cities[i],
            'price': prices[i],
            'description': description[i],
            'photos': photos[i]
        }
        requests.post(url=API_LINK+'attraction', data=data)


def gen_test_db():
    create_users()
    create_attractions()
    create_hotels()
    create_estates()
    create_transports()
    create_rent_a_cars()


gen_test_db()
