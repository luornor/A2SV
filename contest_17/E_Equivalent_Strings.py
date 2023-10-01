def are_strings_equivalent(s1, s2):
    # Check if the two strings are equal
    if s1 == s2:
        return True

    n = len(s1)

    # Check if the two strings can be obtained by swapping their halves
    half = n // 2
    a1= sorted(s1[:half])
    a2=sorted(s1[half:])
    b1=sorted(s2[:half])
    b2=sorted(s2[half:])
    #a1 is equivalent to b1, and a2 is equivalent to b2
    #a1 is equivalent to b2, and a2 is equivalent to b1
    if (a1==b1 and a2==b2) or (a1==b2 and a2==b1):
        return True

    return False

# Read input strings
s1 = input()
s2 = input()

# Check if the strings are equivalent and print the result
if are_strings_equivalent(s1, s2):
    print("YES")
else:
    print("NO")
