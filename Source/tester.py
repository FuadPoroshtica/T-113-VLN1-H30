#
from prettytable import PrettyTable
x = PrettyTable()
x.field_name = ["id","Name"]
x.add_row(["12","George"])
x.add_row(["16","Harold"])
x.add_row(["19","Alex"])
x.add_row(["51","Sinclair"])
print(x)