#Answers are:
#size    first      last      median
#10        25        29        21
#100      615        587      518
#1000    10297      10184    8921

def median_pivot(array):
    first = array[0]
    last = array[-1]
    if len(array) % 2 == 0: # even
        med = array[(len(array) // 2)-1]
    else:
        med = array[(len(array) + 1) // 2]
    
    elements = [first,med,last]
    elements.sort()
    median = elements[1]
    print "median array",array,"list",elements,"pivot",median
    return median

def qsort(array,pivot):
    global count
    count = 0
    _qsort(array, 0, len(array), pivot)
    print "Sorted Array=",array
    print "Comparisons=",count,"pivot=",pivot
    return array    
 
def _qsort(array, l, r, pivot):
    global count

    if r - l > 1:
        if (pivot == 'last'):
            array[r-1], array[l] = array[l], array[r-1]
        elif (pivot == 'med'):
            median = median_pivot(array[l:r])
            m = array.index(median)
            array[m], array[l] = array[l], array[m]
            print "swapping",array[m],"for",array[l],"index:",m,l
            
        p = array[l]
        i = l + 1
        count += r-l -1

        #print "full array  ",array,"l=",l,"r=",r,"i=",i,"p=",p    
        for j in range(l+1, r):
            if array[j] < p:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[l], array[i-1] = array[i-1], array[l] 
        _qsort(array, l, i-1, pivot)
        _qsort(array, i, r, pivot)
        
    
#unsorted = [int(v) for v in open("QuickSort.txt").read().split()]
#unsorted = [3,9,8,4,6,10,2,5,7,1]
#unsorted = [int(v) for v in open("10.txt").read().split()]
#qsort(unsorted, 'first')
#qsort(unsorted, 'last')
qsort(unsorted,'med')


