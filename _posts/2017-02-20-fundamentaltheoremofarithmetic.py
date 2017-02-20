#Fundamental theorem of arithmetic states that:every positive integer greater
#than one can be expressed as unique product of primes.for ex,90=2*3*3*5
#Following is an application of above theorem
def primefactors(n):
    i=0
    factors=[]
#here primelist is list of all primes of a given no
    p=primelist[i]
    while p<=n:
        if n%p==0:
            factors.append(p)
            n //=p
        else:
            i +=1
            p=primelist[i]
    return factors
