"""
Vitaly has an array of n distinct integers. 
Vitaly wants to divide this array into three non-empty sets
so as the following conditions hold:
The product of all numbers in the first set is less than zero (<0).
The product of all numbers in the second set is greater than zero (>0).
The product of all numbers in the third set is equal to zero.
Each number from the initial array must occur in exactly one set.
Input
The first line of the input contains integer n (3≤n≤100). 
The second line contains n space-separated distinct integers a1,a2,...,an — the array elements.

Output
In the first line print integer n1 (n1>0) — the number of elements in the first set. 
Then print n1 numbers — the elements that got to the first set.

In the next line print integer n2 (n2>0) — the number of elements in the second set.
Then print n2 numbers — the elements that got to the second set.

In the next line print integer n3 (n3>0) — the number of elements in the third set. 
Then print n3 numbers — the elements that got to the third set.
"""


def solve(elements):
    elements.sort()
    set_neg = [elements[0]]
    elements.pop(0)
    set_pos = [x for x in elements if x!=0]
    set_zero =[x for x in elements if x==0]
  
    num_neg = [x for x in set_pos if x<0]

    if len(num_neg)%2==1:
        set_zero.append(set_pos[0])
        set_pos.pop(0)
           
    print(len(set_neg),*set_neg)
    print(len(set_pos),*set_pos)
    print(len(set_zero),*set_zero)


n = int(input())
elements = list(map(int,input().split()))
solve(elements)

