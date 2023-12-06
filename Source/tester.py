from data.employee_data import Employee_data
from model.employee_model import Employee
from data.location_data import location_data
from model.location_model import Location
import datetime
date1 = datetime.datetime(2023,11,8,13,25)
print(date1) # 08.11.2023,13:25, 
             # 08.11.2023,16:30,

#l_instance=Location("01",2,3,4,5,6,7)
#loc_list=location_data()
#loc_mod_instance=loc_list.location_constructor()
#print(l_instance.id)
#temp=[]
#for x in loc_mod_instance:
#    print(x.id,x.country)
#    if x.id == l_instance.id:
#        x=l_instance
#        break
#for x in loc_mod_instance:
#    print(x.id,x.country)



#id,country,airport_code,flight_duration,distance,manager_name,emergency_phone
#01,Germany,HAM,3h 30m,9167 km,Isabella Garcia,49 1122334455
#02,China,SHA,11h 30m,6818 km,Chen Li,86 11443555122
#03,Italy,ROM,3h 30m,1884 km,Michael Jones,39 087654321
