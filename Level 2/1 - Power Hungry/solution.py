# Approach 1 - O(N)
def solution2(xs):
    neg = [num for num in xs if num < 0]
    pos = [num for num in xs if num > 0]

    if len(neg) % 2 != 0: neg.remove(max(neg))

    if pos or neg:
        prod = 1
        for x in pos + neg: prod *= x
        return str(prod)

    return '0'



# Approach 2 - O(NlogN)
def solution1(xs):
    xs.sort()
    
    # Edge Cases
    if len(xs) == 1 and xs[0] < 0: return str(xs[0]) # only 1 neg number
    if xs[0] == xs[-1] == 0: return '0'
    if xs[0] < 0 and xs.count(0)==len(xs)-1: return '0'
    
    # General Case
    pos_prod = 1
    neg_prod = 1
    
    i = len(xs)-1
    while (i>0 and xs[i]>0):
        pos_prod*=xs[i]
        i-=1
    
    i=0
    while(i+1<len(xs) and xs[i]<0):
        if(xs[i+1]>=0):
            break;
        neg_prod=neg_prod*xs[i]*xs[i+1]
        i+=2
    
    return str(pos_prod * neg_prod)