from datetime import datetime


# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   


dt_start = datetime.strptime(date_start, '%m-%d-%Y')
dt_stop = datetime.strptime(date_stop, "%m-%d-%Y")

days_a = dt_stop - dt_start






#  'Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'
#localtime = time.localtime(time.time())
#print ("Local current time :", localtime)




####b)  
date_start = '12312013'  
date_stop = '05282015'  


dt_start = datetime.strptime(date_start, "%m%d%Y")
dt_stop = datetime.strptime(date_stop, "%m%d%Y")

days_b = dt_stop - dt_start


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

dt_start = datetime.strptime(date_start, "%d-%b-%Y")
dt_stop = datetime.strptime(date_stop, "%d-%b-%Y")

days_c = dt_stop - dt_start


print(days_a, days_b, days_c)
