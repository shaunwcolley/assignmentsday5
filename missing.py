a = [0,1,2,3,5,6,7,8,9]

def missing_element(array):
    full_array = list(range(0,10)) # or I could have initialized full array by each element [0,1,2,3,4,5,6,7,8,9]
    for num in full_array:
        if num not in array:
            print(f"Array {array} is missing the following element: {num}")
            #can include below to append array, but places at end, more formating could include
            #array.append(num)
    return array

missing_element(a)
