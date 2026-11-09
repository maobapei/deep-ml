
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	count = Counter(tuple(pair) for pair in data)
	tp = count[(1, 1)]
	tn = count[(0, 0)]
	fp = count[(0, 1)]
	fn = count[(1, 0)]
	return [[tp, fn],[fp, tn]]
