a = [0,1,2,3,5,6,7,8,9]
#only works for 0-9, function not commented out works for any sequential missing element
#def missing_element(array):
#    full_array = list(range(0,10)) # or I could have initialized full array by each element [0,1,2,3,4,5,6,7,8,9]
#    for num in full_array:
#        if num not in array:
#            print(f"Array {array} is missing the following element: {num}")
            #can include below to append array, but places at end, more formating could include
            #array.append(num)
#    return array


b = [21,23,24,25,26]
#find missing element of any array:
def missing_element(array):
    for i in range(0, len(array)-1):
        if (array[i]+1) != array[i+1]:
            print(f"Missing element is {array[i] + 1}")
missing_element(a)
missing_element(b)
