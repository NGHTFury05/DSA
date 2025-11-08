# Graphs can be represented in two common ways: using an adjacency matrix and using an adjacency list. Below are examples of both representations in Python.
# Adjacency Matrix Representation
import numpy as np 
def create_adjacency_matrix(num_vertices, edges):
    # Initialize a num_vertices x num_vertices matrix with zeros
    adjacency_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
    
    # Fill the matrix based on the edges
    for edge in edges:
        u, v = edge
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1  # For undirected graph
    
    return adjacency_matrix
# Example usage
num_vertices = 4   
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
adjacency_matrix = create_adjacency_matrix(num_vertices, edges)
print("Adjacency Matrix:")
print(adjacency_matrix)
# Output:
# Adjacency Matrix:
# [[0 1 1 0]
#  [1 0 1 0]
#  [1 1 0 1]
#  [0 0 1 0]]
# Adjacency List Representation
def create_adjacency_list(num_vertices, edges):
    # Initialize an empty list for each vertex
    adjacency_list = [[] for _ in range(num_vertices)]
    
    # Fill the adjacency list based on the edges
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # For undirected graph
    
    return adjacency_list
# Example usage
adjacency_list = create_adjacency_list(num_vertices, edges)
print("\nAdjacency List:")
for i in range(num_vertices):
    print(f"{i}: {adjacency_list[i]}")
# Output:
# Adjacency List:
# 0: [1, 2]
# 1: [0, 2]
# 2: [0, 1, 3]
# 3: [2]
# In summary, the adjacency matrix is a 2D array where the presence of an edge between vertices is indicated by a 1, while the adjacency list is a list of lists where each sublist contains the neighbors of a vertex.
