array = [1,2,3,4,5,8,10,300]


def double_array(array1):
    array2 = []
    for i in range(0, len(array1)):
        array2.append(array1[i])
    final_array = array1 + array2
    return final_array

print(double_array(array))
