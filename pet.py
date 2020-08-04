class Pet:
    
    def __init__(self, name="molly", species = "dog", age = 3, sex="female", **kwarg):
        self.name = name
        self.species = kwarg["species"] if "species" in kwarg else species
        self.age = kwarg["age"] if "age" in kwarg else age
        self.sex = kwarg["sex"] if "sex" in kwarg else sex

    def __str__(self):
        return "{} is a {} and is {} years old and is {}.".format(self.name, self.species, self.age, self.sex)

    def __repr__(self):
        return self.__str__