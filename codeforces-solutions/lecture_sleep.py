"""
Your friend Mishka and you attend a calculus lecture. Lecture lasts n minutes. 
Lecturer tells ai theorems during the i-th minute.
Mishka is really interested in calculus, though it is so hard to stay awake for all the time of lecture. 
You are given an array t of Mishka's behavior. 
If Mishka is asleep during the i-th minute of the lecture then ti will be equal to 0, 
otherwise it will be equal to 1.
When Mishka is awake he writes down all the theorems he is being told — ai during the i-th minute. 
Otherwise he writes nothing.
You know some secret technique to keep Mishka awake for k minutes straight.
However you can use it only once. You can start using it at the beginning of any minute between 1 and n-k+1.
If you use it on some minute i then Mishka will be awake during minutes j such that
and will write down all the theorems lecturer tells.
You task is to calculate the maximum number of theorems Mishka will be able to write down if you use your technique
only once to wake him up.
    
[1 3 5 2 5 4]
[1 1 0 1 0 0]
1 + 3 + 2
at start he can write = 6 thoerems

if we use secret technique at the first minute
[1 1 1 1] he can write 1+3+5+2=11 thoerems

if we use it at the second minute
he can write [1 1 1 1 ] = 3+5+2+5 = 15 thorems

if we use it at the third minute he can write
[1 1 1 1] = 5+2+5+4 = 16 thoerems
"""
# 0 to 4
# max_theorems = current = before
# secret_technique = 0
# for start in range(n-k+1):
#     while secret_technique-start<k:
#         if behaviour[secret_technique]==0:
#             current+= theorems[secret_technique]
#         secret_technique+=1
#     max_theorems = max(max_theorems,current)

#     if behaviour[start]==0:
#         current-=theorems[start]





# read in the input values
n, k = map(int, input().split())  # n is the total number of minutes, k is the number of minutes we can keep Mishka awake
a = list(map(int, input().split()))  # a is the array of theorems taught during each minute
t = list(map(int, input().split()))  # t is the array indicating whether Mishka is awake or asleep during each minute

# initialize the maximum number of theorems Mishka can write down
max_theorems = 0

# loop over all possible starting points for using the secret technique
for start in range(n - k + 1):
    # create a new array indicating which minutes Mishka is awake for
    # set it to True if t[i] is True or if i is between start and start + k - 1
    awake = [t[i] or (i >= start and i < start + k) for i in range(n)]
    # calculate the total number of theorems Mishka can write down
    # by summing up the values of a for which the corresponding value of awake is True
    theorems = sum([a[i] for i in range(n) if awake[i]])
    # update the maximum number of theorems observed so far
    max_theorems = max(max_theorems, theorems)

# print out the maximum number of theorems Mishka can write down
print(max_theorems)
        




