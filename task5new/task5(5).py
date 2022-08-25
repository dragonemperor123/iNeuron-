import logging
logging.basicConfig(filename="test5.log",level=logging.INFO)

class ineuron:
    try:
        def name(self):
            logging.info("Your class name is ineuron!")

    except:
        logging.info("You have not been enrolled")

class students:
    try:
        def name(self):
            logging.info("Your class name is students")

    except:
        logging.info("No students enrolled")

class class_name:
    try:
        def name(self):
            logging.info("Your Class name is class_name")
    except:
        logging.info("Name not defined")

class class_type:
    try:
        def name(self):
            logging.info("Your class name is class_type")
    except:
        logging.info("Class not defined")


class number_of_courses:
    try:
        def name(self):
            logging.info("Your class name is number_of_courses")
    except:
        logging.info("No courses")

class affiliates:
    try:
        def name(self):
            logging.info("Your class name is affiliates")
    except:
        logging.info("You don't have any affiliates")

class blog:
    try:
        def name(self):
            logging.info("Your class name is blog")
    except:
        logging.info("you dont have any blogs")

class internships:
    try:

        def name(self):
            logging.info("your class name is internships")

    except:
        logging.info("You don't have any internships!!")

class jobs:
    try:

        def name(self):
            logging.info("Your class name is jobs")
    except:
        logging.info("You are unemployed!")

class material_covered:
    try:
        def name(self):
            logging.info("Your class name is materials_covered")
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

obj1.name()
obj2.name()
obj3.name()
obj4.name()
obj5.name()
obj6.name()
obj7.name()
obj8.name()
obj9.name()
obj10.name()