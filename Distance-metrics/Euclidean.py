import math

def euclidean_distance(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality.")
    
    squared_distance = sum((x - y) ** 2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance

# Example usage with two points in 4-dimensional space
point1 = (1, 2, 3, 4)
point2 = (5, 6, 7, 8)

distance = euclidean_distance(point1, point2)
print(f"The Euclidean distance between {point1} and {point2} is {distance}")
