#!/usr/bin/python3

class Animal:

    __VALID_SPECIES = ("dog","cat","bird")

    def __init__(self, name, species):
        self.name = name
        self.species = species
   
    def __add__(self, value):
        return Daycare(value)
    
    def __str__(self):
        if self.species == "dog":
            sound = "Woof Woof"
        elif self.species == "cat":
            sound = "Meow Meow"
        elif self.species == "bird":
            sound = "Tweet Tweet"
        else:
            sound = "Hmm Hmm"

        return sound + ": My name is " + self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("This name isnt a string")
        if value == "":
            raise ValueError("Name cant be empty")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self,value):
        if value not in self.__VALID_SPECIES:
            raise TypeError("not a species in daycare")
        self.__species = value

class Daycare:

    def __init__(self, animals):
        self.animals = animals

    def __str__(self):
        border = "========================="
        row = "Animal #{}: {}\n"
        string = border + '\n'
        for i, v in enumerate(self.animals):
            string += row.format(i, v)
        string += border

        return string 

    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, value):
        if not isinstance(value, list):
            raise TypeError("not a list of animals")
        if not all(type(animal) is Animal for animal in value):
                raise TypeError("not an animal")
        self.__animals = value





if __name__ == "__main__":
    dog = Animal("freddy","dog")
    cat = Animal("Garfield","cat")
    bird = Animal("Big bird","bird")
    print(Daycare([bird, dog, cat]))
