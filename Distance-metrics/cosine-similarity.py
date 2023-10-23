import math

# Define two text documents
document1 = "This is the first document."
document2 = "This document is the second document."

# Tokenize the documents (split into words and remove punctuation)
def tokenize(text):
    text = text.lower()  # Convert to lowercase
    text = text.split()  # Split into words
    text = [word.strip(".,?!") for word in text]  # Remove punctuation
    return text

document1_words = tokenize(document1)
document2_words = tokenize(document2)

# Create a set of unique words in both documents
unique_words = set(document1_words + document2_words)

# Create word vectors for each document
vector1 = [document1_words.count(word) for word in unique_words]
vector2 = [document2_words.count(word) for word in unique_words]

# Calculate the dot product
dot_product = sum(vector1[i] * vector2[i] for i in range(len(unique_words)))

# Calculate the magnitude (Euclidean norm) of each vector
magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
magnitude2 = math.sqrt(sum(x ** 2 for x in vector2))

# Calculate the cosine similarity
cosine_similarity = dot_product / (magnitude1 * magnitude2)

# Print the cosine similarity
print(f"Cosine Similarity: {cosine_similarity}")
