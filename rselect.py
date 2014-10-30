
import random

def rselect(array, i):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = random.choice(array)

        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
                
        if i == len(less):
            return pivot
        elif i < len(less):
            return rselect(less,i)
        else:
            return rselect(greater,i-len(less+equal))
    else:
        return array[0]
    
#unsorted = [int(v) for v in open("QuickSort.txt").read().split()]
unsorted = [3,9,8,4,6,10,2,5,7,1]
unsorted = [10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(unsorted)
#unsorted = [int(v) for v in open("1000.txt").read().split()]
print rselect(unsorted,5)


