#Creating a class Class with attributes as class_name and grades
class Class:

    # Initializing the Class objects
    def __init__(self,class_name,grades_list):
        self.class_name=class_name
        self.grades_list=grades_list
    # Method to get the average grade from a list if grades
    def get_average_grade(self):
        average_grade = sum(self.grades_list)/len(self.grades_list)
        return  round(average_grade,1)
    # method to get the letter grade
    def letter_grade(self):
        if self.get_average_grade()>=95:
            return 'A+'
        elif self.get_average_grade()>=90:
            return 'A-'
        elif self.get_average_grade()>=87:
            return 'B+'
        elif self.get_average_grade()>=83:
            return 'B'
        elif self.get_average_grade()>=80:
            return 'B-'
        elif self.get_average_grade()>=77:
            return 'C+'
        elif self.get_average_grade()>=73:
            return 'C'
        elif self.get_average_grade()>=70:
            return 'C-'
        else:
            return 'F'
# Method to return the Report of a student containing class name,grades,average and letter grade
    def __str__(self):
        return "%s \n%s \n%s \n%s\n" %('Class:'+self.class_name,'Grades:'+str(self.grades_list),
                                      'Final Grade:'+str(self.get_average_grade()),'Letter Grade:'+self.letter_grade())

# Creating a class Student with attributes name, id and list of classes
class Student():
# initializing Objects
    def __init__(self,name='',id=None,classes_list=[]):
        self.name=name
        self.id=id
        self.classes_list=classes_list
        self.grades_list=[]
# Method to set id for a student
    def set_id(self,id):
        self.id=id
# Method to set the classes for a student
    def set_classes(self,classes_list):
        self.classes_list=classes_list
# Method to append new Class objects to student
    def add_new_class(self, class_name, grade_list): #
        self.classes_list.append(Class(class_name,grade_list)) #
# Method to return the Report of a student containing class name,grades,average and letter grade
    def report_classes(self):
        print(self.name + "'s Report Card:\n")
        for i in self.classes_list:  # For loop to append all the classes and grades of student
            print(i)
# Method to print the student's name,id and list of classes
    def __str__(self):
        final=''
        for i in range(len(self.classes_list)): # for loop to append classes taken by the student
            final = final + (self.classes_list[i].class_name+',')

        return "%s %s %s"%(self.name+',','ID:'+str(self.id)+',','Classess taking:'+ final.strip(','))

#Part 1
print('Part 1 Solution')
a=Class("Linear Algebra",[97,91,82]) # Creating an object of Class
print(a) # printing the Class object craeted


#Part 2
print('Part 2 Solution')
b=Student() # Creating a Student object
b.name="George" # Assigning name for student
b.set_id(120)  # Setting id
# Adding classes with class name and grades
b.add_new_class("Calculus",[100,70,95,97])
b.add_new_class("Physics",[98,79,81])
b.add_new_class("Stochastic Process",[50,100,97])
# printing Student's report card
print(b.report_classes())
print(b) # Print student object


#Part 3
print('Part 3 Solution')
#creating Class objects
print('i) Class objects are created')
cl_1=Class("Python Programming",[78,87,90])
cl_2=Class("Data Analytics",[77,91])
cl_3=Class("History",[65,89,82])
cl_4=Class("Thermodynamics",[78,43,67])
cl_5=Class("Electronics",[87,96,65])
# Testing the print function for class objects
print('ii)')
print(cl_4)
print(cl_2)


# Part 4
print('Part 4 Solution')
# i)
print('i) Student objects are created')
#Creating 2 Student objects
student_a=Student('Lisa',120,[cl_3,cl_1])
student_b=Student('Juan',121,[cl_5])
# ii)
print('ii)')
#Printing to test the report classes method
print(student_a.report_classes())
print(student_b.report_classes())
# iii)
print('iii)')
#Testing the set_classes method for a student object and verifying the same using report_classes method
student_a.set_classes([cl_2])
print(student_a.report_classes())
# iv)
print('iv)')
#Testing to add a new class and verifying the same using methods
student_b.add_new_class("Algorithms",[45,54,69])
print(student_b.report_classes())
#v)
print('v)')
#Testing the print function for the student objects
print(student_a)
print(student_b)