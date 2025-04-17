from faker import Faker


class RandomUser:
    def __init__(self, faker: Faker):
        self.faker = faker
        self.first_name = self.faker.first_name()
        self.last_name = self.faker.last_name()
        self.email = self.faker.email()
        self.phone = self.faker.phone_number()
        self.password = self.faker.password()


user = RandomUser(Faker())
