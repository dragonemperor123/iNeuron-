import logging
logging.basicConfig(filename="test.log",level=logging.INFO)

try:
    class jobs:
        def job(self):
            logging.info("Your current job is t")
    class dream_job(jobs):
        def dream(self):
            logging.info("your dream job is x")

except:
        logging.info("You are unemployed!")