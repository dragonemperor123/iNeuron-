import logging
logging.basicConfig(filename="test.log",level=logging.INFO)

try:
    class blog:

        def blogs(self):
            logging.info("The blogs you have created are a,b,c")
    class video(blog):
        def videos(self):
            logging.info("The videos you have created are as follows")



except:
        logging.info("you dont have any blogs")
