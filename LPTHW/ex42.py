## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is a animal
class Dog(Animal):

    def __init__(self, name):
        ## assign name to class dogs name variable
        self.name = name

## Cat is a animal
class Cat(Animal):

    def __init__(self, name):
        ## assign name to class cats name variable
        self.name = name

## Person is a object
class Person(object):

    def __init__(self, name):
        ## assign name to person classses name variable
        self.name = name
        print self.name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a class
class Employee(Person):

    def __init__(self,name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## Fish is a class
class Fish(object):
    pass

## Salmon is a class
class Salmon(Fish):
    pass

## Halibut is a class
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## assign marys pet as satan
mary.pet = satan

## frank is a employee, name frank and salary 120000
frank = Employee("Frank", 120000)

##franks pet rover
frank.pet = rover

##flipper is a fish
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
