#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:28:12 2019

@author: isegura
"""

#Problem 1:​ Write a recursive method for finding the minimum element in a list of integers.

def minimum(l):
    if l is None or len(l)==0:
        #print('list is empty')
        return None
    
    if len(l)==1:
        return l[0]
    else:
        return min(l[0],minimum(l[1:]))
        
def checkPalindrome(s):
    if s is None or len(s)==0:
        #print('list is empty')
        return True
    n=len(s)-1
    return s[0]==s[n] and checkPalindrome(s[1:n])
    
def sumDigits(n):
    if type(n)!=int:
        print('n must be integer')
        return None
    if n<0:
        n=abs(n)
    if n<10:
        return n
    else:
        return n%10 + sumDigits(n//10)
      
def isSorted(l):
    if l is None or len(l)<=1:
        return True
    
    if l[0]>l[1]:
        return False
    else:
        return isSorted(l[1:])
    
    #return l[0]<=l[1] and isSorted(l[1:])
 
def russianMult(a,b):
    if a==0 or b==0:
        return 0
    if a==1:
        return b
    if a%2==0:
        return russianMult(a//2,b*2)
    if a%2!=0:
        return b+russianMult(a//2,b*2)
    
import random
def testMin():
    l=[]
    for i in range(10):
        l.append(random.randint(-10,10))
        
    print(l)
    print(minimum(l))
    l=[]
    print(minimum(l))

    
    
testMin()

s='radar'
print('checkPalindrome({})={}'.format(s,checkPalindrome(s)))

s='aab'
print('checkPalindrome({})={}'.format(s,checkPalindrome(s)))

s='a'
print('checkPalindrome({})={}'.format(s,checkPalindrome(s)))

n=random.randint(-10000,10000)
print('sumDigits({})={}'.format(n,sumDigits(n)))

l=[-5,0,1,3,4,5,8]
print('isSorted({})={}'.format(l,isSorted(l)))

l=[-5,0]
print('isSorted({})={}'.format(l,isSorted(l)))

l=[-5,0,-1]
print('isSorted({})={}'.format(l,isSorted(l)))

print('russianMult({},{})={}'.format(10,170,russianMult(10,170)))
print('russianMult({},{})={}'.format(7,32,russianMult(7,32)))
