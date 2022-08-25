import logging
logging.basicConfig(filename="test.log",level=logging.INFO)


try:
    class class_type:
        def type(self):
            logging.info("The type of your class is parent")
    class child(class_type):
        def child_class(self):
            logging.info("The type of your class is child")

except:
        logging.info("Class not defined")


