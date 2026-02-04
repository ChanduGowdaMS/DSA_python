class father:
    def __init__(self, surname, name):
        self.surname=surname
        self.father_name=name
    def display_surname(self):
        print("surname :" , self.surname)
    def display_father_name(self):
        print("father_name :" , self.father_name)

class son(father):
    def __init__(self, name, surname, father_name):
        self.name=name
        super().__init__(surname, father_name)
    def display_name(self):
        print("name :" , self.name)

child = son("chandu", "m", "suresh")
child.display_father_name()
child.display_surname()
child.display_name()
