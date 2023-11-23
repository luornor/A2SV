# --------------------------------------
# Function to convert Edge List to Adjacency matrix
from collections import defaultdict


def edge_list_to_adjacency_list(edge_list):
	# Write your code here to convert the edge list to an adjacency matrix.
    n = max(edge_list)[0]
    adj_matrix = [[0]*(n+1) for _ in range(n+1)]

    for u,v in edge_list:
        adj_matrix[u][v]=1

    return adj_matrix

# Test case
edge_list_sample = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

# --- Student Section to Write Code ---
# Write your code for the conversion here
result_adj_matrix = edge_list_to_adjacency_list(edge_list_sample)
expected_result = [
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,1],
    [0,0,0,1]
    
]

# Print the result for verification
print("Result:", result_adj_matrix)
if result_adj_matrix == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------
