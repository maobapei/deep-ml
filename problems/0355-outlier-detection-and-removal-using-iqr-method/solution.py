import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	# Your code here
	q1 = np.percentile(data, 25)
	q3 = np.percentile(data, 75)
	iqr = q3 - q1
	lower_bound = q1 - k * iqr
	upper_bound = q3 + k * iqr
	lower_bound = round(float(lower_bound), 4)
	upper_bound = round(float(upper_bound), 4)

	outlier_indices = [idx for idx, val in enumerate(data) if val < lower_bound or val > upper_bound]

	cleaned_data = [round(val, 4) for val in data if lower_bound <= val <= upper_bound]

	result = {
    'cleaned_data': cleaned_data,
    'outlier_indices': outlier_indices,
    'lower_bound': lower_bound,
    'upper_bound': upper_bound
	}
	return result
