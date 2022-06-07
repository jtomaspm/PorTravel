from server import db, User, Destination, Hotel, Estate, Transport, Rent_A_Car
import os


def restart_db():
    os.remove("database.db")
    db.create_all()


def create_users(amount):
    for i in range(amount):
        i = str(i)
        user = User(
            username='username'+i,
            password='password',
            name='name',
            address='address',
            bithdate='dd/mm/yyyy',
            postal='1234-123',
            city='city',
            country='country',
            email='email'+i+'@email.com',
            phone='+351 999666333'
        )
        db.session.add(user)
    db.session.commit()


def create_destinations(amount):
    for i in range(amount):
        i = str(i)
        destination = Destination(
            origin_city=''+i,
            origin_country=''+i,
            destination_city=''+i,
            destination_country=''+i,
            company=''+i,
            price=i,
            package=''+i
        )
        db.session.add(destination)
    db.session.commit()


def create_hotels(amount):
    for i in range(amount):
        i = str(i)
        hotel = Hotel(
            name=''+i,
            city=''+i,
            country=''+i,
            price=i,
            persons=i,
            photos=''+i
        )
        db.session.add(hotel)
    db.session.commit()


def create_estates(amount):
    for i in range(amount):
        i = str(i)
        estate = Estate(
            name=''+i,
            owner_username=''+i,
            city=''+i,
            country=''+i,
            price=i,
            persons=i,
            photos=''+i
        )
        db.session.add(estate)
    db.session.commit()


def create_transports(amount):
    for i in range(amount):
        i = str(i)
        transport = Transport(
            origin_city=''+i,
            origin_country=''+i,
            destination_city=''+i,
            destination_country=''+i,
            company=''+i,
            price=i,
            method=''+i
        )
        db.session.add(transport)
    db.session.commit()


def create_rent_a_cars(amount):
    for i in range(amount):
        i = str(i)
        rent_a_car = Rent_A_Car(
            city=''+i,
            country=''+i,
            company=''+i,
            price=i,
            model=''+i
        )
        db.session.add(rent_a_car)
    db.session.commit()


def gen_test_db(amount):
    restart_db()
    create_users(amount)
    create_destinations(amount)
    create_hotels(amount)
    create_estates(amount)
    create_transports(amount)
    create_rent_a_cars(amount)


# restart_db()
gen_test_db(5)
