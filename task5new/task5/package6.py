import logging
logging.basicConfig(filename="test.log",level=logging.INFO)


try:
    class affiliates:
        def aff(self):
            logging.info("The affiliates you have are x,y,z")
    class non_affiliates(affiliates):
        def num_non_aff(self):
            logging.info("Number of non affiliates is:")

except:
        logging.info("You don't have any affiliates")



