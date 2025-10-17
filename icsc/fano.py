import numpy as np

probabilities = np.array([0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.05, 0.04, 0.03, 0.02, 0.10])
lengths = np.array([3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4])

print("Expected length is", np.sum(probabilities * lengths))