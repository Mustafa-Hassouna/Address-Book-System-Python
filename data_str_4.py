from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["number","name","age","Jop"]
datas = [
    [1,"mustafa",19,"eng"],
    [2,"sara",16,"no_jop"],
    [3,"samia",30,"web_dis"]
]
datas.append([4,"ahmed",22,"footballer"])
for data in datas:
    x.add_row(data)
print(x)