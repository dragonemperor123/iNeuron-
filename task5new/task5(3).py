import logging
logging.basicConfig(filename="test3.log",level=logging.INFO)
#inheritance is shown with its properties
try:
    class ineuron:

        def course(self):
            logging.info("You have been enrolled")

    class fsds(ineuron):
        def admit(self):
            logging.info("you have been registered in the fsds batch")



except:
        logging.info("You have not been enrolled")
try:
    class students:

        def number(self):
            logging.info("The number of students is as follows")

    class placed(students):
        def status(self):
            logging.info("The number of placed students are as follows")

except:
        logging.info("No students enrolled")

try:
    class class_name:
        def name(self):
            logging.info("the name of your class is class!")

    class time(class_name):
        def timing(self):
            logging.info("The timing of your class class is 3-8PM!")
except:
        logging.info("Name not defined")


try:
    class class_type:
        def type(self):
            logging.info("The type of your class is parent")
    class child(class_type):
        def child_class(self):
            logging.info("The type of your class is child")

except:
        logging.info("Class not defined")

try:
    class number_of_courses:

        def num_courses(self):
            logging.info("the number of courses is x")

    class info_course(number_of_courses):
        def info_courses(self):
            logging.info("The information about the courses is as follows")
except:
        logging.info("No courses")

try:
    class affiliates:
        def aff(self):
            logging.info("The affiliates you have are x,y,z")
    class non_affiliates(affiliates):
        def num_non_aff(self):
            logging.info("Number of non affiliates is:")

except:
        logging.info("You don't have any affiliates")

try:
    class blog:

        def blogs(self):
            logging.info("The blogs you have created are a,b,c")
    class video(blog):
        def videos(self):
            logging.info("The videos you have created are as follows")



except:
        logging.info("you dont have any blogs")

try:
    class internships:


        def int(self):
            logging.info("The internships you have under your belt are l,m,n")
    class completed_internships(internships):
        def completed(self):
            logging.info("The internships you have completed are m")
except:
        logging.info("You don't have any internships!!")

try:
    class jobs:
        def job(self):
            logging.info("Your current job is t")
    class dream_job(jobs):
        def dream(self):
            logging.info("your dream job is x")

except:
        logging.info("You are unemployed!")

try:
    class material_covered:

        def material(self):
            logging.info("You are upto date with the current portion. Go ahead now!")
    class self_learning(material_covered):
        def learn(self):
            logging.info("You have completed the c,v which are not taught yet")

except:
        logging.info("You are behind the current portion! Catch up quickly!")

obj1 = fsds()
obj2 = placed()
obj3 = time()
obj4 = child()
obj5 = info_course()
obj6 = non_affiliates()
obj7 = video()
obj8 = completed_internships()
obj9 = dream_job()
obj10 = self_learning()

obj1.course()
obj1.admit()
obj2.number()
obj2.status()
obj3.name()
obj3.timing()
obj4.type()
obj4.child_class()
obj5.num_courses()
obj5.info_courses()
obj6.aff()
obj6.num_non_aff()
obj7.blogs()
obj7.videos()
obj8.int()
obj8.completed()
obj9.job()
obj9.dream()
obj10.material()
obj10.learn()