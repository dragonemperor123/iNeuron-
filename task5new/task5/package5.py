import logging
logging.basicConfig(filename="test.log",level=logging.INFO)


try:
    class number_of_courses:

        def num_courses(self):
            logging.info("the number of courses is x")

    class info_course(number_of_courses):
        def info_courses(self):
            logging.info("The information about the courses is as follows")
except:
        logging.info("No courses")

