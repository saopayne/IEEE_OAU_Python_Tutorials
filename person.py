class person:
    name = "my name"
    age = 0

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def greet(self):
        greeting = "Hello " + self.name
        #print greeting
        return greeting

    def greet_other(self, _person):
        greeting = self.name + " shouting out to " + _person.name
        #print greeting
        return greeting

    def greet_other_name(self, _name):
        greeting = self.name + " shouting out to " + _name
        #print greeting
        return greeting

    def get_age(self):
        #print self.age
        return self.age

def how_old(person):
    print person.name, "is", person.age, "years old"

if __name__ == "__main__":
    person1 = person("Segun", 5)
    person2 = person("Femi", 17)
    people = [person1, person2]
    for p in people:
        p.greet()
    person1.name = "Jola"
    person2.greet_other(person1)
