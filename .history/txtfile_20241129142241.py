# Calculate the learning metric for each animal, ignoring the 4th trial for C2R
learning_results = {}

for animal, vector in animal_vectors.items():
    # Ensure the vector has at least 5 values
    if len(vector) >= 5:
        # Convert strings to integers
        vector = list(map(int, vector))
        if animal == "C2R":
            numerator = vector[4] + vector[2]  # Use 5th + 3rd trial for C2R
        else:
            numerator = vector[4] + vector[3]  # Use 5th + 4th trial for other animals
        denominator = vector[0] + vector[1]  # 1st + 2nd trial

        if denominator > 0:  # Avoid division by zero
            learning_metric = numerator / denominator
            learning_results[animal] = "Learning" if learning_metric > 1 else "No Learning"
        else:
            learning_results[animal] = "Undefined (Denominator = 0)"
    else:
        learning_results[animal] = "Insufficient Data"

# Print the learning results
print("\nLearning Results (Updated for C2R):")
for animal, result in learning_results.items():
    print(f"{animal}: {result}")
