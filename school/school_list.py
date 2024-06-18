# from school.school import School
class SchoolList:

    def __init__(self):
        self.schools =  []

    def add_school(self, new_school):
        for name in self.schools:
            if name.school_name == new_school.school_name:
                print("Duplicate Entry Found..")
        self.schools.append(new_school)
        print("School Added Successfully..!") 
    
    
    def add_address(self, search_id_address, new_address_obj):
           for sch in self.schools:
               if sch.school_id == search_id_address:
                   sch.address = new_address_obj
                   print(f"{sch.school_name} School Address Added..")
                   
    def show(self):
        for sch in self.schools:
            print(sch)
        
    def update_school(self, school_id_for_update):
        for sch in self.schools:
            if sch.school_id == int(school_id_for_update):
                sch.school_name = input("Enter New School Name: ")
                print("Name Updated..")

    def search_school(self, search_school_name):
        for name in self.schools:
            if search_school_name in name.school_name:
                print(f"\nSchool ID: {name.school_id} \nSchool Name: {name.school_name} \nEstablish Year: {name.establish_year}")
            else:
                print("Not available..")


    def delete_school(self, delete_school_id):
        for sch in self.schools:
            if sch.school_id == int(delete_school_id):
                self.schools.remove(sch)
                print("School Deleted..")


    def seach_school_incity(self, school_city_name):
        for city in self.schools:
            if city.address.city == school_city_name:
                print(f"\nSchool ID: {city.school_id} \nSchool Name: {city.school_name} \nEstablish Year: {city.establish_year}")
                
                
    def my_standard(self, school_obj, sch_id, standard_obj):
        for sch in self.schools:
            if sch.school_id == sch_id:
                school_obj.add_standard(sch, standard_obj)
    
    def show_standards(self, sch_id):
        for sch in self.schools:
            if sch_id == sch.school_id: 
                print(f"Id: {sch.school_id}  \nSchool Name: {sch.school_name}")
                for std in sch.standards:
                    print(std)
    
    def add_student(self, standard_obj, sch_id, standard, student_obj):
        for sch in self.schools:
            if sch_id == sch.school_id:
                for std in sch.standards:
                    if std.standard_name == standard:
                        standard_obj.add_student(std, student_obj)
                            
                            
    def show_students(self, student_obj, sch_id, standard):
        for sch in self.schools:
            if sch_id == sch.school_id:
                print(sch.school_name)
                student_obj.show_students(sch, standard)
                
    
    def shift_standard(self, standard_obj, sch_id, current_standard, student_roll, next_standard):
        for sch in self.schools:
            if sch.school_id == sch_id:
                standard_obj.shift_standard(sch, current_standard, student_roll, next_standard)
                

    # def shift_standard(self, standard_obj, sch_id, current_standard, next_standard):
    #     for sch in self.schools:
    #         if sch.school_id == sch_id:
    #             standard_obj.shift_standard(sch, current_standard, next_standard)
    
