import logging
logging.basicConfig(filename="test2.log",level=logging.INFO)

l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"iNeuron","k3":"kumar",3:6,7:8},["iNeuron","data science"]]
class DEF:
    def extract_list(self):
        try:
            for i in l:
                if type(i) == list:
                    logging.info(i)
        except:
            logging.warning("No list list entity found")


    def extract_dict(self):
        try:
            for i in l:
                if type(i) == dict:
                    logging.info(i)

        except:
            logging.warning("No dict entity")

    def extract_tuple(self):
        try:
            for i in l:
                if type(i) == tuple:
                    logging.info(i)

        except:
            logging.warning("No dict entity")


    def extract_numeric(self):
        try:
            for i in l:
                if type(i) == tuple or dict or list:
                    for j in i:
                        if type(j) == int:
                            logging.info(j)

        except:
            logging.warning("No numeric entities")


    def summation(self):
        try:
            m = 0
            for i in l:
                if type(i) == tuple or dict or list:
                    for j in i:
                        if type(j) == int:
                            m = m + j

            logging.info(m)

        except:
            logging.warning("No numeric data")


    def odd_values(self):
        try:
            l1 = []
            for i in l:
                if type(i) == tuple or dict or list:
                    for j in i:
                        if type(j) == int:
                            if (j % 2 != 0):
                                logging.info(j)

        except:
            logging.warning("No odd values")


    def extract_ineuron(self):
        try:
            l1 = []
            for i in l:
                if type(i) == tuple or dict or list:
                    for j in i:
                        if type(j) == str:
                            if (j == "iNeuron" or i[j] == 'iNeuron'):
                                logging.info(j)

        except:
            logging.warning("No such element")

    def occurences(self):
        try:
            a = 0
            b = 0
            c = 0
            for i in l:
                if type(i) == tuple:
                    a = a + 1
                if type(i) == list:
                    b = b + 1
                if type(i) == dict:
                    c = c + 1
            logging.info(a)
            logging.info(b)
            logging.info(c)

        except:
            logging.info("No records")


    def number_of_keys(self):
        try:
            a = 0
            for i in l:
                if type(i) == dict:
                    for j in i:
                        a = a + 1

            print("Number of keys:", a)

        except:
            logging.info("No dictionary")


    def filter_string(self):
        try:
            for i in l:
                if type(i) == list or dict or tuple:
                    for j in i:
                        if type(j) == str:
                            logging.info(j)

        except:
            logging.info("No string elements")


    def filter_alphanum(self):
        try:
            for i in l:
                if type(i) == list or dict or tuple:
                    for j in i:
                        if type(j) == str and type(j) == int:
                            logging.info(j)

        except:
            logging.info("No alphanum characters")


    def multiplication(self):
        try:
            m = 1
            for i in l:
                if type(i) == list or dict or tuple:
                    for j in i:
                        if type(j) == int:
                            m = m * j
            logging.info(m)

        except:
            logging.info("One value is zero")


    def unwrap(self):
        try:
            l2 = []
            for i in l:
                if type(i) == list or dict or tuple:
                    for j in i:
                        l2.append(j)
            logging.info(l2)

        except:
            logging.info("List is not valid")


obj = DEF()
obj.odd_values()
obj.occurences()
obj.summation()
obj.number_of_keys()
obj.multiplication()
obj.unwrap()
obj.filter_string()
obj.filter_alphanum()
obj.extract_tuple()
obj.extract_numeric()
obj.extract_ineuron()
obj.extract_dict()
obj.extract_list()






