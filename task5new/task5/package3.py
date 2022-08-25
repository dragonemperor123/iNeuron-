import logging
logging.basicConfig(filename="test.log",level=logging.INFO)


try:
    class class_name:
        def name(self):
            logging.info("the name of your class is class!")

    class time(class_name):
        def timing(self):
            logging.info("The timing of your class class is 3-8PM!")
except:
        logging.info("Name not defined")


