n = int(input())
a = list(map(int, input().split()))

last_occurrence = {}  # Dictionary to store the last occurrence index of each element
circled = set()  # Set to keep track of circled elements
operations = []  # List to store the indices of elements that are circled

for i in range(n):
    if a[i] not in last_occurrence or last_occurrence[a[i]] in circled:
        # Circle the element and update its last occurrence index
        circled.add(i)
        operations.append(i + 1)
        last_occurrence[a[i]] = i
    elif a[i] in circled:
        # If the element is already circled but not at its last occurrence, it's not possible
        print(-1)
        break
else:
    # All operations are valid, print the result
    print(len(operations))
    print(*operations)
