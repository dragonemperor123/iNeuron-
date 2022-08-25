import logging
logging.basicConfig(filename="test4.log",level=logging.INFO)

#Access Modifiers
#public members can be called from inside or outside the class. protected members can be called from inside the child class. But not
#during object call. Private variables can only be accessed inside the class
try:
    class ineuron:
        name = 'Adwait'
        _surname = 'Sawant'
        __branch = 'Mumbai'

        def course(self):
            logging.info("You have been enrolled")
            logging.info("Name is:")
            logging.info(self.name)
            logging.info("surname is:")
            logging.info(self._surname)
            logging.info("Branch is:")
            logging.info(self.__branch)

    class fsds(ineuron):
        def admit(self):
            logging.info("you have been registered in the fsds batch")
            logging.info(self._surname)

except:
        logging.info("You have not been enrolled")
try:
    class students:
        name = "Adwait"
        _rollno = 21
        __college = "Amity"

        def number(self):
            logging.info("The number of students is as follows")
            logging.info("Name is:")
            logging.info(self.name)
            logging.info("Roll number is:")
            logging.info(self._rollno)
            logging.info("College is:")
            logging.info(self.__college)

    class placed(students):
        def status(self):
            logging.info("The number of placed students are as follows")
            logging.info(self._rollno)

except:
        logging.info("No students enrolled")

try:
    class class_name:
        name = "Class"
        _id = 3
        __accmod = "private"
        def name(self):
            logging.info("the name of your class is class!")
            logging.info(self.name)
            logging.info("The id is:")
            logging.info(self._id)
            logging.info("The access modifier of this variable is:")
            logging.info(self.__accmod)

    class time(class_name):
        def timing(self):
            logging.info("The timing of your class class is 3-8PM!")
            logging.info(self._id)


except:
        logging.info("Name not defined")


try:
    class class_type:
        type = "Parent"
        _set = "Yes"
        __mutable = "No"
        def type(self):
            logging.info("The type of your class is parent")
            logging.info(self.type)
            logging.info("Is it set:")
            logging.info(self._set)
            logging.info("Is it mutable")
            logging.info(self.__mutable)

    class child(class_type):
        def child_class(self):
            logging.info("The type of your class is child")
            logging.info(self._set)


except:
        logging.info("Class not defined")

try:
    class number_of_courses:
        name = "fsds"
        _number = 4
        __total = 10

        def num_courses(self):
            logging.info("the number of courses is x")
            logging.info(self._number)
            logging.info("name of course")
            logging.info(self.name)
            logging.info("Total courses")
            logging.info(self.__total)

    class info_course(number_of_courses):
        def info_courses(self):
            logging.info("The information about the courses is as follows")
            logging.info(self._number)


except:
        logging.info("No courses")

try:
    class affiliates:
        number = 8
        _location = "Mumbai"
        __slots = 8
        def aff(self):
            logging.info("The affiliates you have are x,y,z")
            logging.info(self.number)
            logging.info("Location of them")
            logging.info(self._location)
            logging.info("Slots")
            logging.info(self.__slots)

    class non_affiliates(affiliates):
        def num_non_aff(self):
            logging.info("Number of non affiliates is:")
            logging.info(self._location)


except:
        logging.info("You don't have any affiliates")

try:
    class blog:
        name = "High School"
        _pages = 10
        __type = "Story"

        def blogs(self):
            logging.info("The blogs you have created are a,b,c")
            logging.info("Name of blog")
            logging.info(self.name)
            logging.info("Number of pages")
            logging.info(self._pages)
            logging.info("Type of blog")
            logging.info(self.__type)

    class video(blog):
        def videos(self):
            logging.info("The videos you have created are as follows")
            logging.info(self._pages)




except:
        logging.info("you dont have any blogs")

try:
    class internships:
        number = 0
        _category = "Fresher"
        __education = "BCA Graduate"



        def int(self):
            logging.info("The internships you have under your belt are l,m,n")

    class completed_internships(internships):
        def completed(self):
            logging.info("The internships you have completed are m")
            logging.info(self._category)



except:
        logging.info("You don't have any internships!!")

try:
    class jobs:
        name = "TataIQ"
        _category = "Fresher"
        __salary = "6 LPA"
        def job(self):
            logging.info("Your current job is t")

    class dream_job(jobs):
        def dream(self):
            logging.info("your dream job is x")
            logging.info(self._category)


except:
        logging.info("You are unemployed!")

try:
    class material_covered:
        course = "fsds"
        _latest = "MongoDB"
        __self_studied = 2

        def material(self):
            logging.info("You are upto date with the current portion. Go ahead now!")


    class self_learning(material_covered):
        def learn(self):
            logging.info("You have completed the c,v which are not taught yet")
            logging.info(self._latest)




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