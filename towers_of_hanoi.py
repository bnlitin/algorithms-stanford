###################################################################
# Class: Algorithms: Design and Analysis, Stanford
# Project: Towers of Hanoi
# Author: Boris Litinsky
# Date: 10/28/2014
# Description: Recursive algorithm to solve Towers of Hanoi
###################################################################

def hanoi(n, source, helper, target):
    if n > 0:
        print "n",n,"source",source,"helper",helper,"target",target
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print source, helper, target