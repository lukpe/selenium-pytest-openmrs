from faker import Faker
from utils.excel_driver import ExcelDriver


class PatientData:
    @staticmethod
    def get_data():
        faker = Faker()

        data = {
            "first_name": faker.first_name_female(),
            "last_name": faker.last_name_female(),
            "gender": "Female",
            "birth_date": faker.date_of_birth(),
            "addr_street": faker.street_address(),
            "addr_city": faker.city(),
            "addr_country": faker.country(),
            "addr_postal": faker.postcode(),
            "addr_phone": faker.msisdn(),
        }
        for item in data.items():
            excel = ExcelDriver()
            excel.set_value(item[0], item[1])
        return data

    @staticmethod
    def get_relative_name(n, relationship_type):
        faker = Faker()
        name = faker.name()
        excel = ExcelDriver()
        excel.set_value(f"relative_{n}", f"{relationship_type}: {name}")
        return name
