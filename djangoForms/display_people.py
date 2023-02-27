from main import People

my_people = People.select()
for person in my_people:
    print(person.name, person.PhoneNumber, person.email, person.county, person.gender, person.religion, person.password)
