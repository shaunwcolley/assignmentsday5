n1 = [1,2,4,6,9,1,2]

def largest(numbers):

    num = numbers[0]
    for i in range(0, len(numbers)):
    #for i in range(i1 + 0, len(numbers)):
        if numbers[i] > num:
            num = numbers[i]
    return num

print(largest(n1))
