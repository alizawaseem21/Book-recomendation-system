import numpy as np

# Define the coordinates of two points in n-dimensional space
point1 = np.array([1,2,3,47,6,5,4,3])  # Replace with the actual coordinates
point2 = np.array([6,7,4,3,5,6,7,7])  # Replace with the actual coordinates

# Calculate the Manhattan distance
manhattan_distance = np.sum(np.abs(point1 - point2))

# Print the result
print(f"The Manhattan distance between point1 and point2 is {manhattan_distance}")
