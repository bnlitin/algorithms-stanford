def merge(a,b):
    i = 0
    j = 0
    c = []
    
    for k in range(0,len(a+b)):
        print "i=",i,"j=",j,"k=",k
        if j >= len(b) or a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif i >= len(a) or b[j] < a[i]:
            c.append(b[j])
            j += 1
    return c   

def mergesort(x):
    if len(x) <= 1:
        return x
    elif len(x) == 2:
        if x[0] < x[1]:
            return x
        else:
            return [x[1],x[0]]
    else:
        a = x[0 : len(x)//2]
        b = x[len(x)//2 : len(x)]
        return merge(mergesort(a),mergesort(b))

def main():
    print mergesort([4,3,2,1])
    
    
if __name__ == '__main__':
    main()