# build pet adoption service

from pet import Pet
import sqlite3

def db_insert(pet):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    sql = "INSERT INTO pets (name, species, age, sex) values ('{}', '{}', '{}', '{}')".format(pet.name, pet.species, pet.age, pet.sex)
    c.execute(sql)
    conn.commit()
    conn.close()

while True:
    response = input("(e)nter a pet or (f)ile or (q)uit:")
    if response == "q":
        break

    if response == "e":
        name = input("name: " )
        species = input("species: ")
        age = input("age: ")
        sex = input("sex: ")
        p = Pet(name, species, age, sex)
        db_insert(p)

    if response == "f":
        file = input("filename: ")
        with open(file) as f:
            for line in f:
                name, species, age, sex = line.strip().split(',')
                p = Pet(name, species, age, sex)
                db_insert(p)