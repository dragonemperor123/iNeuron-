import logging
logging.basicConfig(filename="test2.log",level=logging.INFO)
#constructor
#we will create 10 classes with constructors
#constructor is the __init__ function, non parameterized in this case. it is called by default if we don't call it explicitly.
class ineuron:
    try:
        def __init__(self):
            logging.info("You have been enrolled")

    except:
        logging.info("You have not been enrolled")

class students:
    try:
        def __init__(self):
            logging.info("The number of students is as follows")

    except:
        logging.info("No students enrolled")

class class_name:
    try:
        def __init__(self):
            logging.info("the name of your class is class!")
    except:
        logging.info("Name not defined")

class class_type:
    try:
        def __init__(self):
            logging.info("The type of your class is parent")
    except:
        logging.info("Class not defined")


class number_of_courses:
    try:
        def __init__(self):
            logging.info("the number of courses is x")
    except:
        logging.info("No courses")

class affiliates:
    try:
        def __init__(self):
            logging.info("The affiliates you have are x,y,z")
    except:
        logging.info("You don't have any affiliates")

class blog:
    try:
        def __init__(self):
            logging.info("The blogs you have created are a,b,c")
    except:
        logging.info("you dont have any blogs")

class internships:
    try:

        def __init__(self):
            logging.info("The internships you have under your belt are l,m,n")

    except:
        logging.info("You don't have any internships!!")

class jobs:
    try:

        def __init__(self):
            logging.info("Your current job is t")
    except:
        logging.info("You are unemployed!")

class material_covered:
    try:
        def __init__(self):
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


obj1.__init__()
obj2.__init__()
obj3.__init__()
obj4.__init__()
obj5.__init__()
obj6.__init__()
obj7.__init__()
obj8.__init__()
obj9.__init__()
obj10.__init__()