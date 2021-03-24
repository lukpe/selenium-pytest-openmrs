import os

from faker import Faker
from utils.excel_driver import ExcelDriver

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
        for item in data.items():
            excel = ExcelDriver()
            excel.set_value(item[0], item[1])
        return data

    @staticmethod
    def get_value(name):
        faker = Faker()
        method = getattr(faker, name)
        value = method()
        return value
