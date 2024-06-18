from school.school import School
from school.school_list import SchoolList
from school.address import Address
from school.standard import Standard
from school.students import Students
from exception.myvalidation import Myvalidation

school_list_obj = SchoolList()

def main():
    while True:
        user_input = input("""
                        Provide Your Input: 
                        1. Add School
                        2. Add Address
                        3. Show School
                        4. Search School Using Name Keywords
                        5. Delete School Using ID
                        6. Update School Using ID
                        7. Seach Schools In City
                        8. Add Standard to School
                        9. Show Standards
                        10.Add Students
                        11.Show Students
                        12.Move Students
                        13.Exit
                        """)
        if user_input == '1':
            
            try:
                school_name = input("Please Provide Name of School: ")
                establish_year = input("Please Provide Establish Year: ")
                School.validate(school_name, establish_year)
            except Myvalidation as e:
                print(e)
                continue
            
            school_obj = School(school_name.title(), establish_year)
            school_list_obj.add_school(school_obj)
        
        elif user_input == '2':
            sch_id = int(input("Enter School Id For Add School Address: "))
            area = input("Enter School Area Name: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            pincode = input("Enter Pincode: ")
            new_address_obj = Address(area.title(), city.title(), state.title(), pincode)
            school_list_obj.add_address(sch_id, new_address_obj)
            
        elif user_input == '3':
            school_list_obj.show() 

        elif user_input == "4":
            search_school_name = input("Provide School Name for Search: ")
            school_list_obj.search_school(search_school_name)

        elif user_input == '5':
            delete_school_id = input("Provide School Id To Delete School: ")
            school_list_obj.delete_school(delete_school_id)

        elif user_input == '6':
            school_list_obj.show()
            school_id = input("\nProvide School Id To Update: ")
            school_list_obj.update_school(school_id)
        
        elif user_input == '7':
            school_city_name = input("Enter City Name to print Schools in the City: ")
            school_list_obj.seach_school_incity(school_city_name.istitle())
        
        elif user_input == '8':
            sch_id = int(input("Enter School Id For Add Standard: "))
            standard = input("Enter Standard Add To School: ")
            standard_obj = Standard(standard)
            school_list_obj.my_standard(school_obj, sch_id, standard_obj)
                
        elif user_input == '9':
            sch_id = int(input("Enter School Id to Show Standards: "))
            school_list_obj.show_standards(sch_id)             
        
        elif user_input == '10':
            sch_id = int(input("Enter School Id to Add Students: "))
            standard = input("Enter Standard for Adding Student: ")
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ") 
            student_obj = Students(roll, name, age)
            school_list_obj.add_student(standard_obj, sch_id, standard, student_obj)
            
        elif user_input == '11':
            sch_id = int(input("Enter School Id for Show Students: "))
            standard = input("Enter Standard for show students: ")
            school_list_obj.show_students(student_obj, sch_id, standard)        
        
        elif user_input == '12':
            sch_id = int(input("Enter School ID for Move Student One Standard To Another Standard: "))
            current_standard = input("Enter Current Standard for Move Students: ")
            student_roll = input("Enter Roll No To Shift Standard: ")
            next_standard = input("Enter Next Standard for Students: ")
            school_list_obj.shift_standard(standard_obj, sch_id, current_standard, student_roll, next_standard)
            
            
        # elif user_input == '12':
        #     sch_id = int(input("Enter School ID for Move Student One Standard To Another Standard: "))
        #     current_standard = input("Enter Current Standard for Move Students: ")
        #     next_standard = input("Enter Next Standard for Students: ")
        #     school_list_obj.shift_standard(standard_obj, sch_id, current_standard, next_standard)
        
        elif user_input == '13':
            print("Your Exited..")
            break
        else:
            print("Invalid Input..")

main()