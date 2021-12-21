from news.models import nieuwsweb 

class Newweb:

    def __init__(self,url):
        self.url = url
        self.listarticleobject = ""
        self.listarticleelement = ""
        self.listarticlename = ""
        self.linkarticleobject =  ""
        self.linkarticleelement = ""
        self.linkarticlename = ""
        self.titlearticleobject = ""
        self.titlearticleelement = ""
        self.titlearticlename = ""
        self.descarticleobject = ""
        self.descarticleelement = ""
        self.descearticlename = ""

    def list_info(self):
        print("nu komen er een paar vragen voor de lijst van artikelen.\n")
        self.listarticleobject = input("Voer naam van object in. Bijv, div li enz\n  ")
        self.listarticleelement = input("Voer element in. Bijv, class:  id: \n ")
        self.listarticlename = input("Voer naam in.\n")

    def link_info(self):
       print("De vragen die nu komen zijn voor de link naar de artikel\n")
       self.linkarticleobject = input("Voer naam van object in. Bijv, div li enz\n  ")
       self.linkarticleelement = input("Voer element in. Bijv, class:  id:\n ")
       self.linkarticlename = input("Voer naam in.\n")

    def title_info(self):
       print("Vragen voor elke titel van artikel\n")
       self.titlearticleobject = input("Voer naam van object in. Bijv, div li enz \n ")
       self.titlearticleelement = input("Voer element in. Bijv, class:  id:\n ")
       self.titlearticlename =  input("Voer naam in.\n")

    def description_info(self):
        print("Vragen voor elke omschrijving van artikel\n")
        self.descarticleobject = input("Voer naam van object in. Bijv, div li enz\n  ")
        self.descarticleelement = input("Voer element in. Bijv, class:  id:\n ")
        self.descearticlename = input("Voer naam in.\n")

    def info_save(self):
        
        web= nieuwsweb( url = self.url,
        listarticleobject = self.listarticleobject,
        listarticleelement = self.listarticleelement,
        listarticlename = self.listarticlename,
        linkarticleelement = self.linkarticleelement,
        linkarticleobject = self.linkarticleobject,
        linkarticlename =   self.linkarticlename ,
        titlearticleelement = self.titlearticleelement,
        titlearticleobject = self.titlearticleobject,
        titlearticlename = self.titlearticlename,
        descarticleobject = self.descarticleobject,
        descarticleelement = self.descarticleelement,
        descearticlename = self.descearticlename)
        web.save()
             