"""If s is palindromic initially, we can operate on the interval [1,n], the answer is Yes.

Let's consider the other case. In a palindrome s, for each i in [1,⌊n/2⌋], si
=sn−i+1
 must hold. For those i, we may check whether si
=sn−i+1
 is true in the initial string. For all the illegal positions i, the operation must contain either i or n+1−i , but not both. For the legal positions, the operation must contain neither of i nor n+1−i, or both of them.

If the illegal positions is continuous (which means that they are l,l+1,…,r−1,r for some l and r), we may operate on the interval [l,r] (or [n+1−r,n+1−l]), making the string palindromic. The answer is Yes.

Otherwise, there must be some legal positions that lie between the illegal ones. Suppose the illegal positions range between [l,r] (but not continuous), and the operation is [$o_1$,o2
]. Without loss of generality, let the operation lies in the left part of the string. Then o1
≤l,r≤o2
<n+1−r must hold to correct all the illegal positions. This interval covers all the legal positions that lie between the illegal ones but does not cover their symmetrical positions. Thus, such kind of operation will produce new illegal positions. In other words, there are no valid operations in this situation. The answer is No.

Time complexity: O(n)."""
def solve(n,s):
    if s == s[::-1]:
        return "Yes"

    illegal_positions = []
    for i in range(1, n // 2 + 1):
        if s[i - 1] != s[n - i]:
            illegal_positions.append(i)

    if len(illegal_positions) <= 1:
        return "Yes"

    if illegal_positions[-1] - illegal_positions[0] == len(illegal_positions) - 1:
        return "Yes"

    return "No"
    

    #Tutorial
    # l = 0
    # r = n
    # while l < r and s[l] == s[r - 1]:
    #     l += 1
    #     r -= 1
    # if l >= r:
    #     print("Yes")
    #     return
    # while l < r and s[l] != s[r - 1]:
    #     l += 1
    #     r -= 1
    # while l < r and s[l] == s[r - 1]:
    #     l += 1
    #     r -= 1
    # if l >= r:
    #     print("Yes")
    # else:
    #     print("No")


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n,s))