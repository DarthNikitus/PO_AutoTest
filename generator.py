import random
import datetime
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


class Person:
    def __init__(self, full_name, firstname, lastname, midlname, age, department, salary, email, current_address, permanent_address, mobile, birth_date):
        self.full_name = full_name
        self.firstname = firstname
        self.lastname = lastname
        self.midlname = midlname
        self.age = age
        self.department = department
        self.salary = salary
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address
        self.mobile = mobile
        self.birth_date = birth_date

def generated_pass_number():

    yield random.randint(1000000, 9000000)
#
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        midlname=faker_ru.middle_name(),
        age=random.randint(20,50),
        department=faker_ru.job(),
        salary=random.randint(1000,5000),

        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),

        mobile = faker_ru.msisdn(),
        birth_date=faker_ru.date(),


    )

def generated_true_or_false():
    if 0 == random.randint(0, 100) % 2:
        return True
    else:
        return False

# def generated_time():
#     return time_start, time_end
#
time_end = datetime.datetime.utcnow().isoformat() + "Z"
time_start = datetime.datetime.utcnow().isoformat() + "Z"
