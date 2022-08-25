import logging
logging.basicConfig(filename="test.log",level=logging.INFO)

try:
    class students:

        def number(self):
            logging.info("The number of students is as follows")

    class placed(students):
        def status(self):
            logging.info("The number of placed students are as follows")

except:
        logging.info("No students enrolled")

