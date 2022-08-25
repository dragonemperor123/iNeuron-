import logging
logging.basicConfig(filename="test.log",level=logging.INFO)


try:
    class ineuron:

        def course(self):
            logging.info("You have been enrolled")

    class fsds(ineuron):
        def admit(self):
            logging.info("you have been registered in the fsds batch")



except:
        logging.info("You have not been enrolled")