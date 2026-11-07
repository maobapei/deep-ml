import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	normal_loss = np.mean((y_true - np.dot(X, w))**2)
	L2_penalty = alpha * np.sum(w ** 2)
	L = normal_loss + L2_penalty
	return L
