class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is :", self.surname)

    def display_father_name(self):
        print("The fathername is :", self.father_name)


class mother:
    def __init__(self, eye_color,name):
        self.eye_color=eye_color
        self.mother_name=name

    def display_eye_color(self):
        print("eye_color is :", self.eye_color)

    def display_mother_name(self):
        print("The mothername is :", self.mother_name)
    

class son(father,mother):
    def __init__(self,name,surname,father_name,eye_color,mother_name):
        self.name=name
        father.__init__(self,surname,father_name)
        mother.__init__(self,eye_color,mother_name)
        
    def display_name(self):
        print("name is :", self.name)
        self.display_eye_color()
        self.display_mother_name()
        self.display_surname()
        self.display_father_name()


son_obj=son("chandu","ms","suresh","Balck","somu")
son_obj.display_name()


