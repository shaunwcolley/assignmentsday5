n = [7,3,300,4, -300]

def smallest(numbers):

    num = numbers[0]
    for i in range(0, len(numbers)):
    #for i in range(i1 + 0, len(numbers)):
        if numbers[i] < num:
            num = numbers[i]
    return num
print(smallest(n))
