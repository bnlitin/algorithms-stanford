count = 0

def median_pivot(array):
    first = array[0]
    last = array[-1]
    if len(array) % 2 == 0: # even
        med = array[(len(array) // 2)-1]
    else:
        med = array[(len(array) + 1) // 2]
    
    temp = [first,med,last]
    temp.sort()
    return temp[1]
          
def quicksort(array):
    global count
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0] # user first element
        #pivot = array[-1] # use last element
        #pivot = median_pivot(array)
        
        cnt = len(array) - 1
        count += cnt
        print "array:",array,"pivot:",pivot,"comparisons",cnt

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    # Note that you want equal ^^^^^ not pivot
    else:
        return array
    
#unsorted = [int(v) for v in open("QuickSort.txt").read().split()]
#unsorted = [3,9,8,4,6,10,2,5,7,1]
unsorted = [int(v) for v in open("1000.txt").read().split()]
print quicksort(unsorted)
#unsorted = [3,8,2,5,1,4,7,6]
#print qsort(unsorted)
print "total comparisons", count
