n = int(input())


for i in range(n+1):
    # Determine the number of spaces before the digits on each line
    spaces = " "*(n-i)*2

    # Generate the string of digits for the current line
    nums = " ".join(str(j) for j in range(i))
    
    # nums_reverse = " ".join(str(j) for j in range(i,-1,-1))
    if i!=0:
        # Print the pattern for non-zero rows
        print(spaces + nums+ " "  + str(i) + " "+ nums[::-1])
    else:
        # Print the pattern for the first row (i.e., when i is 0)
        print(spaces + str(i))


for i in range(n-1,-1,-1):

    # Determine the number of spaces before the digits on each line
    spaces = " "*(n-i)*2    
    # Generate the string of digits for the current line
    nums = " ".join(str(j) for j in range(i))
    # nums_reverse = " ".join(str(j) for j in range(i,-1,-1))
    if i!=0:
        # Print the pattern for non-zero rows
        print(spaces + nums+ " "  + str(i) + " "+ nums[::-1])
    else:
        # Print the pattern for the first row (i.e., when i is 0)
        print(spaces + str(i))



