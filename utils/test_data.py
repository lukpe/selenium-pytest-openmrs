import os

from faker import Faker

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class PatientData:
    @staticmethod
    def get_data():
        faker = Faker()

        data = {
            'first_name': faker.first_name_female(),
            'last_name': faker.last_name_female(),
            'birth_date': faker.date_of_birth(),
            'addr_street': faker.street_address(),
            'addr_city': faker.city(),
            'addr_country': faker.country(),
            'addr_postal': faker.postcode(),
            'addr_phone': faker.msisdn(),
            'relatives': None,
        }
        return data

    @staticmethod
    def get_value(value):
        faker = Faker()
        method = getattr(faker, value)
        data = method()
        return data
