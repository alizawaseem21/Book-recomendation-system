def minkowski_distance(point1, point2, p):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality.")

    distance = 0
    for i in range(len(point1)):
        distance += abs(point1[i] - point2[i]) ** p

    return distance ** (1 / p)

# Define the coordinates of two points in n-dimensional space
point1 = [3,6,5,4]  # Replace with the actual coordinates
point2 = [5,7,8,9]  # Replace with the actual coordinates

# Define the value of p (the order of the Minkowski distance)
p = 2  # Change to the desired value of p (e.g., 1 for Manhattan, 2 for Euclidean)

# Calculate the Minkowski distance
minkowski_distance_value = minkowski_distance(point1, point2, p)

# Print the result
print(f"The Minkowski distance between point1 and point2 is {minkowski_distance_value}")
