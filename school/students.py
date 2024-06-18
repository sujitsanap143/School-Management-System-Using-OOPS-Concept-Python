
class Students:
    def __init__(self,roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age
    
    def __str__(self):
        return(f"Roll No: {self.roll} Name: {self.name} Age: {self.age}")
    
    
    def show_students(self, sch, standard):
        for std in sch.standards:
            if std.standard_name == standard:
                print(std)
                for stud in std.students:
                    print(stud)