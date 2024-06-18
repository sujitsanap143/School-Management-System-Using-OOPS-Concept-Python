from exception.myvalidation import Myvalidation
# from address import Address
class SchoolBase:
    _school_id_counter = 0

    def __init__(self):
        self.school_id = SchoolBase.__increament()
        # self.school_id = self.__increament()
        
    @classmethod
    def __increament(cls):
        cls._school_id_counter += 1
        return cls._school_id_counter

class School(SchoolBase):
    def __init__(self, school_name, establish_year, address = None):
        self.school_name = school_name
        self.establish_year = establish_year
        self.address = address
        self.standards = []
        SchoolBase.__init__(self)

            
    def add_standard(self,sch, standard_obj):
        sch.standards.append(standard_obj)
        print("Standard Added..!")


    def __str__(self):
        
        standards_info = " th, ".join(str(standard.standard_name) for standard in self.standards)
        # standards_info = ""
        # for standard in self.standards:
        #     standards_info += str(standard)
         
        if self.address != None and self.standards != None:
            return f"\nId: {self.school_id} \nSchool Name: {self.school_name} \nEstablish Year: {self.establish_year} \nAddress: {self.address} \nStandards: {standards_info} th"
        
        elif self.standards != []:
            return f"\nId: {self.school_id} \nSchool Name: {self.school_name} \nEstablish Year: {self.establish_year} \nStandards: {standards_info} th"
        
        elif self.address != None:
            return f"\nId: {self.school_id} \nSchool Name: {self.school_name} \nEstablish Year: {self.establish_year} \nAddress: {self.address}"

        else:
            return f"\nId: {self.school_id} \nSchool Name: {self.school_name} \nEstablish Year: {self.establish_year}"
        
    def validate(name, establish_year):
        if len(name.strip()) == 0 and len(establish_year) != 4:
            raise Myvalidation("School Name is Empty And Invalid Year..")
        elif len(name.strip()) == 0 and len(establish_year) == 4:
            raise Myvalidation("School Name Is Invalid..")
        elif len(establish_year) != 4 and len(name.strip()) != 0:
            raise Myvalidation ("Establish Year Is Wrong..")
        else:
            return True
        
        
    
    
    
    
    
    
    
    
    
    
# address1 = Address("abc area", "Pune", "Maharashtra", 411028)        
# school1  = School("vps", 2017, address1)

# school2 = School("Tps", 2019)
# print(school1)
# print(school2)

        
