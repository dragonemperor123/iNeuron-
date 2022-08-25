import logging
logging.basicConfig(filename="test.log",level=logging.INFO)


try:
    class internships:


        def int(self):
            logging.info("The internships you have under your belt are l,m,n")
    class completed_internships(internships):
        def completed(self):
            logging.info("The internships you have completed are m")
except:
        logging.info("You don't have any internships!!")
