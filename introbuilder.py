# Program to generate an introduction for a person based on their name, age, city and profession.

import datetime

def generate_introduction(name, age, city, profession, hobby):
    return f"""Hello! My name is {name}. I am {age} years old and I live in {city}.\n
    I work as a {profession} and in my free time I enjoy {hobby}.\n
    Nice to meet you!\n"""

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")
hobby = input("Enter your hobby: ")

introduction = generate_introduction(name, age, city, profession, hobby)

today = datetime.date.today().isoformat()
introduction += f" \n Logged on: {today}"

introduction = "*" * 100 + "\n" + introduction + "\n" + "*" * 100

print(introduction)