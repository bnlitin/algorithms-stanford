# bubble sort

def bubblesort(x):
    if len(x) <= 1:
        return x
    else:
        while True:
            swapped = False
            for i in range(len(x)-1):
                if (x[i] > x[i+1]):
                    x[i], x[i+1] = x[i+1], x[i]
                    swapped = True
            if swapped == False:
                break
        return x

def main():
    print bubblesort([])    
    print bubblesort([4])  
    print bubblesort([4,3])  
    print bubblesort([4,3,2,1])
    
    
if __name__ == '__main__':
    main()