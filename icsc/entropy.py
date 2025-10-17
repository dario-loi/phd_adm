import numpy as np


probabilities = np.array([0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.05, 0.04, 0.03, 0.02, 0.10])
print("Log probabilities are", np.log2(probabilities, where=(probabilities>0)))
print("Entropy is", -np.sum(probabilities * np.log2(probabilities, where=(probabilities>0))))