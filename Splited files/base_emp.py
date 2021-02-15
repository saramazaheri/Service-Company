import sql3
import csv

class base_empo:
    def __init__(self, name, lastname, email, password, phone, id, birth_place, city, education, gender, unemployed, emergency):
        self.name = name
        self.lastname= lastname
        self.email= email
        self.password= password
        self.phone= phone
        self.id= id
        self.birth_place= birth_place
        self.city= city
        self.education= education
        self.gender= gender
        self.unemployed= unemployed
        self.emergency= emergency

        def getname(self):
            return self.name and self.lastname

        def getemail(self):
            return self.email

        def getpass(self):
            return self.password    
            
        def getphone(self):
            return self.phone

        def get_id(self):
            return self.id

        def get_education(self):
            return self.education

        def get_gender(self):
            return self.gender
        