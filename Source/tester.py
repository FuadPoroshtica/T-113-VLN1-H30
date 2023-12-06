from data.employee_data import Employee_data
from model.employee_model import Employee
a = Employee_data()
b=a.employee_constructor()
#print(b)
#self,id,name,address,cell_phone,email,title,home_phone
p=Employee("2806009975","Gauti Guðmundsson","Austurbrekka 2","6222412","Gautigudmunds@gmail.com","Cabin Crew")
a.modify_employee_data(b,p)
