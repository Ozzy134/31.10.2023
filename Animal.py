class Animal:

    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f'{self.name} подает голос')

    def move(self):
        print(f'{self.name} дергает хвостом')

class Dog(Animal):

    def __init__(self, name, legs, breed):
        super().__init__(name=name, legs=legs, species=Dog)
        self.breed = breed

    def bark(self):
        print(f'{self.breed} {self.name} лает')

class Bird(Animal):

    def __init__(self, name, wingspan, species, legs):
        super().__init__(name=name, species=species, legs=2)
        self.wingspan = wingspan

    def fly(self):
        print(f'{self.species} {self.name} летает')

dog = Dog("Геральт", 4,"доберман")
bird = Bird("Вася", 2, "попугай", 2)
dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()