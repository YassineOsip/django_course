class Person:

    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def affchicherLesInfos(self):
        print("le nom est :" + self.nom)
        print("le prenom est :" + self. prenom)
        print("le age est : {}".format(str(self.age)))

class Humain:
    pass

class Etudiant(Person,Humain):
    def __init__(self, nom, prenom, age,ne):
        super().__init__(nom, prenom, age)
        self.ne = ne


houssam = Etudiant("aghmir","houssam",18,"D123456")
houssam.affchicherLesInfos()
print(houssam.ne)