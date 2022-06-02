#!/usr/bin/python3

class Animal:

    move = False

    def __init__(self, name, specie, age, sound):
        self.name = name
        self.specie = specie
        self.age = age
        self.sound = sound

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Animal should have a name")
        if type(value) is not str:
            raise TypeError("value must be a string")
        self.__name = value

    @property
    def specie(self):
        return self.__specie

    @specie.setter
    def specie(self, value):
        if value is None:
            raise ValueError("Give me a specie")
        if type(value) is not str:
            raise TypeError("value must be a string")
        self.__specie = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value is None:
            raise ValueError("Give the animal age")
        if type(value) is not int:
            raise TypeError("value must be a integer")
        self.__age = value

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        if type(value) is not str:
            raise TypeError("value must be a string")
        self.__sound = value

    def move(self):
        Animal.move = True

    def stop(self):
        Animal.move = False

    def show(self):
        if Animal.move is True:
            print("I'm here running, hello, watch me!")
        else:
            print("I'm hiddign very quieto, leave alone!")

    def cry(self):
        for i in range(7):
            print(self.sound, end=' ')
        print()


class acuatic():

    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def sound(self):
        print("we acuatics do gloo gloo gloo")
