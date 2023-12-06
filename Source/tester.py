from data.employee_data import Employee_data
from model.employee_model import Employee
a = Employee_data()
#b=a.employeeConstructor()
#print(b)
#self,id,name,address,cell_phone,email,title,home_phone
p=Employee("2806009975","Gauti Guðmundsson","Austurbrekku 18","6222412","Gautigudmunds@gmail.com","Cabin Crew")
a.add_employee_data(p)
