#Programs/Find Duplicat Elements In Lits.Py

variable=[]
list=[12,12,45,45,85,85,63,74,95]
for i in list:
    if i not in variable:
        variable.append(i)
print(variable)