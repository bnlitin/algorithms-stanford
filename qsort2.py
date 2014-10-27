count = 0

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)
    return array
 
def _quicksort(array, start, stop):
    global count

    if stop - start > 0:
        pivot, left, right = array[stop], start, stop
        print "array",array,"start",start,"stop",stop,"pivot",pivot,"cmp",(stop-start)
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)


#unsorted = [int(v) for v in open("QuickSort.txt").read().split()]
#unsorted = [3,9,8,4,6,10,2,5,7,1]
unsorted = [int(v) for v in open("10.txt").read().split()]
#print quicksort(unsorted)
#unsorted = [3,8,2,5,1,4,7,6]
print quicksort(unsorted)
print "total comparisons", count