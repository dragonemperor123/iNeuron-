import logging
logging.basicConfig(filename="test6.log",level=logging.INFO)
#Packages working

from task5 import package1
from task5 import package2
from task5 import package3
from task5 import package4
from task5 import package5
from task5 import package6
from task5 import package7
from task5 import package8
from task5 import package9
from task5 import package10
from task5.package1 import fsds
from task5.package10 import self_learning
from task5.package2 import placed
from task5.package3 import time
from task5.package4 import child
from task5.package5 import info_course
from task5.package6 import non_affiliates
from task5.package7 import video
from task5.package8 import completed_internships
from task5.package9 import dream_job

obj1 = fsds()
obj2 = placed()
obj3 = time()
obj4 = child()
obj5 = info_course()
obj6 = non_affiliates()
obj7 = video()
obj8 = completed_internships()
obj9 = dream_job()
obj10 = self_learning()

obj1.course()
obj1.admit()
obj2.number()
obj2.status()
obj3.name()
obj3.timing()
obj4.type()
obj4.child_class()
obj5.num_courses()
obj5.info_courses()
obj6.aff()
obj6.num_non_aff()
obj7.blogs()
obj7.videos()
obj8.int()
obj8.completed()
obj9.job()
obj9.dream()
obj10.material()
obj10.learn()
