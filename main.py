import logging
logging.basicConfig(filename="test1.log",level=logging.INFO)

l1=[]
l = [3,4,5,6,7,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,6657,6),{"key1":"sudh",234:[23,45,656]}]
class ABC:
    def reverse(self):

        try:
            for i in l:
                l1.insert(0,i)
            logging.info(l1)
        except:
            logging.info("There must be more than one element is a list")

    def access_234(self):
        try:
            logging.info(l[7][0])
        except:
            logging.info("No such element")

    def access_456(self):
        try:
            logging.info(l[5][1])
        except:
            logging.info("No such element")

    def list_collection(self):
        try:
            logging.info(l[6])
        except:
            logging.info("No such element")

    def access_sudh(self):
        try:
            logging.info(l[8]["key1"])
        except:
            logging.info("No such element")
    def display_keys(self):
        try:


            for i in l:
                if type(i) == dict:
                    for j in i:
                        logging.info(j)

        except:
            logging.info("There is no dictionary")

    def display_values(self):
        try:

            for i in l:
                if type(i) == dict:
                    for j in i:
                        logging.info(i[j])
        except:
            logging.info("There is no dictionary")




obj = ABC()
obj.reverse()
obj.access_234()
obj.access_456()
obj.list_collection()
obj.access_sudh()
obj.display_keys()
obj.display_values()
