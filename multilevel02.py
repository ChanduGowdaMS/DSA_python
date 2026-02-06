class grand_father:
    def __init__(self,property):
        self.grand_father_property=property

    def display_property1(self):
        print("The grand father property is",self.grand_father_property)


class father(grand_father):
    def __init__(self,property,grand_father_property):
        self.father_property=property
        super().__init__(grand_father_property)

    def display_property2(self):
        print("The father property is",self.father_property)


class son(father):
    def __init__(self,property,father_property,grand_father_property):
        self.property=property
        super().__init__(father_property,grand_father_property)
        
    def display_property3(self):
        print("The son property is",self.property)
        self.display_property2()
        self.display_property1()

son_obj=son("bike","Car","house")


son_obj.display_property3()

