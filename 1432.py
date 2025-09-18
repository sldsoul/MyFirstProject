from faker import Faker

fake = Faker()

random_name = fake.name()
random_address = fake.address()

print("Случайное имя:", random_name)
print("Случайный адрес:", random_address)
