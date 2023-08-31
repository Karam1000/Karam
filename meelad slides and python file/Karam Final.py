Name : Karam Abuqasem
Delivery Date : 31/8/2023
Eng.Mohanad Alkrunz
class Course:
    def __init__(self, course_id, course_name, course_mark):
        self.course_id = course_id
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_students = 0

    def __init__(self, student_id, student_number, student_name, student_age):
        self.student_id = student_id
        self.student_number = student_number
        self.student_name = student_name
        self.student_age = student_age
        self.courses_list = []
        Student.total_students += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)


students_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit\n"
                              "Enter your choice:"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    new_student = Student(Student.total_students, student_number, student_name, student_age)
                    students_list.append(new_student)
                    print("Student Added Successfully")
                    break
                except ValueError:
                    print("Invalid Age. Please enter a valid age.")

        elif selection == 2:
            student_number_to_delete = input("Enter Student Number to delete: ")
            for student in students_list:
                if student.student_number == student_number_to_delete:
                    students_list.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student not found.")

        elif selection == 3:
            student_number_to_display = input("Enter Student Number to display: ")
            for student in students_list:
                if student.student_number == student_number_to_display:
                    print("Student Details:")
                    print(f"Student ID: {student.student_id}")
                    print(f"Student Name: {student.student_name}")
                    print(f"Student Age: {student.student_age}")
                    print("Student Courses:")
                    student.get_student_courses()
                    break
            else:
                print("Student not found.")

        elif selection == 4:
            student_number_to_average = input("Enter Student Number to calculate average: ")
            for student in students_list:
                if student.student_number == student_number_to_average:
                    average = student.get_student_average()
                    print(f"Student Average Mark: {average}")
                    break
            else:
                print("Student not found.")

        elif selection == 5:
            student_number_to_add_course = input("Enter Student Number to add course: ")
            for student in students_list:
                if student.student_number == student_number_to_add_course:
                    course_name = input("Enter Course Name: ")
                    course_mark = int(input("Enter Course Mark: "))
                    new_course = Course(len(student.courses_list) + 1, course_name, course_mark)
                    student.enroll_course(new_course)
                    print("Course Added Successfully")
                    break
            else:
                print("Student not found.")

        elif selection == 6:
            print("Exiting the program.")
            break

        else:
            print("Invalid selection. Please choose a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid option.")
