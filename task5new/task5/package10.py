import logging
logging.basicConfig(filename="test.log",level=logging.INFO)

try:
    class material_covered:

        def material(self):
            logging.info("You are upto date with the current portion. Go ahead now!")
    class self_learning(material_covered):
        def learn(self):
            logging.info("You have completed the c,v which are not taught yet")

except:
        logging.info("You are behind the current portion! Catch up quickly!")