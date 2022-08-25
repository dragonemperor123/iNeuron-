import logging
logging.basicConfig(filename="test.log",level=logging.INFO)

#Object
#Here we will make 10 classes and 10 objects

class ineuron:
    try:
        def course(self):
            logging.info("You have been enrolled")

    except:
        logging.info("You have not been enrolled")

class students:
    try:
        def number(self):
            logging.info("The number of students is as follows")

    except:
        logging.info("No students enrolled")

class class_name:
    try:
        def name(self):
            logging.info("the name of your class is class!")
    except:
        logging.info("Name not defined")

class class_type:
    try:
        def type(self):
            logging.info("The type of your class is parent")
    except:
        logging.info("Class not defined")


class number_of_courses:
    try:
        def num_courses(self):
            logging.info("the number of courses is x")
    except:
        logging.info("No courses")

class affiliates:
    try:
        def aff(self):
            logging.info("The affiliates you have are x,y,z")
    except:
        logging.info("You don't have any affiliates")

class blog:
    try:
        def blogs(self):
            logging.info("The blogs you have created are a,b,c")
    except:
        logging.info("you dont have any blogs")

class internships:
    try:

        def int(self):
            logging.info("The internships you have under your belt are l,m,n")

    except:
        logging.info("You don't have any internships!!")

class jobs:
    try:

        def job(self):
            logging.info("Your current job is t")
    except:
        logging.info("You are unemployed!")

class material_covered:
    try:
        def material(self):
            logging.info("You are upto date with the current portion. Go ahead now!")
    except:
        logging.info("You are behind the current portion! Catch up quickly!")


obj1 = ineuron()
obj2 = students()
obj3 = class_name()
obj4 = class_type()
obj5 = number_of_courses()
obj6 = affiliates()
obj7 = blog()
obj8 = internships()
obj9 = jobs()
obj10 = material_covered()


obj1.course()
obj2.number()
obj3.name()
obj4.type()
obj5.num_courses()
obj6.aff()
obj7.blogs()
obj8.int()
obj9.job()
obj10.material()




