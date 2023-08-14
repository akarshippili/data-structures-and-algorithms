# just playing with Comparable classes in python
class Person:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    

    def __str__(self):
        return f'Person [name: {self.name}, age: {self.age}, nationality: {self.nationality}]'
    
    def __eq__(self, __value: object) -> bool:
        if(not isinstance(__value, Person)): raise Exception("Cannot compare Person with " + type(__value))
        return self.age - __value.age == 0 
    
    def __lt__(self, __value):
        if(not isinstance(__value, Person)): raise Exception("Cannot compare Person with " + str(type(__value)))
        return self.age - __value.age < 0 

Person1 = Person("akarsh", 22, "indian")
Person2 = Person("maitrey", 21, "american")
Person3 = Person("Elon Musk", 50, "South African")


persons = [Person1, Person2, Person3]
for person in persons: print(person)
persons.sort()
for person in persons: print(person)
print(Person1 > Person2, Person2 > Person3)
