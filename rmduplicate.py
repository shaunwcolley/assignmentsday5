names1 = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

#print(names)
#The following prints every duplicate name once.
#for i1 in range(0,len(names1)):
#    name1 = names1[i1]
#    for i2 in range(i1+1,len(names1)):
#        if i2 != i1:
#            name2 = names1[i2]
#            if name2 == name1:
#                names2 += [name]
#print(names)
def rmduplicate(names):
    unique_names = []
    for name in names1:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

print(rmduplicate(names1))
