def solve(queries):
    arr = []
    first_occurrence = {}
    
    for query in queries:
        if query[0] == 'insert':
            x, y = query[1], query[2]
            
            if y in first_occurrence:
                index = first_occurrence[y]
                arr.insert(index + 1, x)
                
                for key in list(first_occurrence.keys()):
                    if first_occurrence[key] > index:
                        first_occurrence[key] += 1
            else:
                arr.append(x)
            
            # If x is not already in the dictionary, add it
            if x not in first_occurrence:
                first_occurrence[x] = len(arr) - 1
        
        elif query[0] == 'remove':
            w = query[1]
            if w in first_occurrence:
                index = first_occurrence[w]
                arr.pop(index)
                
                del first_occurrence[w]
                
                # Update the dictionary: shift all subsequent elements' indices by -1
                for key in list(first_occurrence.keys()):
                    if first_occurrence[key] > index:
                        first_occurrence[key] -= 1
                        
                #recheck the first occurrence of w in the list
                if w in arr:
                    first_occurrence[w] = arr.index(w)
    
    return arr

q = int(input().strip())
queries = []

for _ in range(q):
    query = input().strip().split()
    if query[0] == 'insert':
        queries.append((query[0], int(query[1]), int(query[2])))
    elif query[0] == 'remove':
        queries.append((query[0], int(query[1])))

print(*solve(queries))

