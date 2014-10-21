# bubble sort

def bubblesort(x):
    if len(x) <= 1:
        return x
    elif len(x) == 2:
        if x[0] < x[1]:
            return x
        else:
            return [x[1],x[0]]
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
    print bubblesort([4,3,2,1])
    
    
if __name__ == '__main__':
    main()