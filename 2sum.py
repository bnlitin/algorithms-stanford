
def loadDiction(infile):    
    with open(infile, 'r') as f:
        diction = set()
        for line in f:
            num = int(line.strip())
            diction.add(num)
    return diction

def twoSum(diction):
    matches = 0
    for t in range(-10000,10001,1):
        for x in diction:
            y = t-x
            if x != y and y in diction:
                matches += 1
                print "total matches=",matches," with ","x=",x,"y=",y,"t=",t
                break
            
    print "total matches=",matches     
    return matches

# total matches= 427
def main():
    diction = loadDiction('algo1-programming_prob-2sum.txt')   
    twoSum(diction)

    
if __name__ == "__main__":
    main()