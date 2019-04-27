def isspsp(x):
    for n in range(2, x):
        if isPrime(n):
            for s in range(2, x):
                if s*s >=x :
                    break
                if isPrime(s):
                    if n + (s*s) == x:
                        return True

    return False

def isPrime(x):
    if x == 2:
        return True
    for n in range(2,x):
        if not n==x and  x%n==0:
            return False
    return True

def generator(n):
    for i in range(n, 2147483647):#this is the maximum integer
     if isspsp(i):
         yield i



def main():
    n=int(input('Enter the n :'))
    spsp=generator(n)
    print (spsp)
    for i in spsp:
        print (i)
if __name__ == '__main__':
    main()
