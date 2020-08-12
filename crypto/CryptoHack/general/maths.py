#!/usr/bin/python3
import math
def gcd(a, b):
    while(b!=0):
        t = b
        b = a % b
        a = t
    return a
# print(gcd(8, 12))
# print(gcd(66528, 52920))
p = 26513
q = 32321
def egcd(a, b):
    if(a==0):
        return (b, 0, 1)
    else:
        quot, remainder = divmod(b, a)
        g, x, y = egcd(remainder, a)
        return (g, y-quot*x, x)
def format(a, b):
    s = egcd(a, b)
    print('gcd is {remainder} = ({u})*{a}+({v})*{b}'.format(remainder=s[0], u=s[1], v=s[2], a=a, b=b))
# format(p,q)
