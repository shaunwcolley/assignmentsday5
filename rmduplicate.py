names1 = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

def rmduplicate(names):
    unique_names = []
    for name in names1:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

print(rmduplicate(names1))
