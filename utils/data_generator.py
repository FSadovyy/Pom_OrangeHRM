from faker import Faker

fake = Faker()


def first_name():
    return fake.first_name()


def last_name():
    return fake.last_name()


def custom_id():
    return fake.numerify(text='test######')


def wrong_username():
    return fake.email()


def wrong_password():
    return fake.password()
