#coding:utf-8
import math


def factorial(k):
    if k==0:
        return 1
    else:
        recurse = factorial(k-1)
        product = k*recurse
        return product

def estimate_pi():
    k = 0
    total = 0
    term = 1
    const = (2*math.sqrt(2))/9801
    print(const)
    while abs(term)>=1E-15:
        num = factorial(4*k)*(1103+26390*k)
        den = factorial(k)**4*396**(4*k)
        term = num/den
        print(k,term,total)
        total += term
        k += 1
    pi = total*const
    return 1/pi
print(estimate_pi())
