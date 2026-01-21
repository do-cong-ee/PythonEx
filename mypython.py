from fractions import Fraction

n = int(input())
arr = list(map(int,input().split()))

if n == 1 :
    print(arr[0]*arr[0])
else :
    ans = 1
    for i in arr :
        ans*=i
    exponent = Fraction(2,n)
    result = ans **float(exponent)
    print(int(round(result)))