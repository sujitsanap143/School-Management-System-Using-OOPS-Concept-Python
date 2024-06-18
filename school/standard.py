
class Standard:
    def __init__(self, standard_name):
        self.standard_name = standard_name
        self.students = []
        
    def __str__(self):
        return f"Standard: {self.standard_name} th"
    
    
    def add_student(self, std, student_obj):
        std.students.append(student_obj)
        # print(std.students)
        print("Student Added Successfully..")
        
        
    # def empty_student(self, std):
    #     if len(std.students) == 0:
    #         print("No Students in this Class..")
            
    
    def shift_standard(self, sch, current_standard, student_roll, next_standard):
        for std in sch.standards:
            if std.standard_name == current_standard:
                curr_stud_list = std.students  ## holding current standard list
                for stud in std.students:
                    if stud.roll == student_roll:
                        cur_stud = stud        ## holdinf student for moving
                cur_std = std
                
            if std.standard_name == next_standard:
                nex_stud_list = std.students   ## Holding next standard list 
                nex_stud_list.append(cur_stud)
                for stud in std.students:
                    if stud.roll == student_roll:
                        curr_stud_list.remove(stud)
                nex_std = std
                print(f"Name: {cur_stud.name} & {cur_std} Student Move To {nex_std}")
    
    
    
    
    
    
    # def shift_standard(self, sch, current_standard, next_standard):
    #     for std in sch.standards:
    #         if std.standard_name == current_standard:
    #             cur_stud_list = std.students
    #             cur_std = std
    #         if std.standard_name == next_standard:
    #             nex_stud_list = std.students
    #             nex_stud_list.extend(cur_stud_list)
    #             cur_stud_list.clear()
    #             nex_std = std
    #             print(f"******** {cur_std} Students Move To {nex_std} ********")
    

