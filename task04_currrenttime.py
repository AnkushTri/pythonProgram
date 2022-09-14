#Write a python script to print the current date in the following format “Sun May 
#29 02:26:23 IST 2017” 

import time
current_time=time.localtime()
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",current_time))

"""

#printing date time 
from datetime import datetime


print(datetime.now())


"""