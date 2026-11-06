import numpy as np

def fit_polynomial(x, y, degree):
    """
    Fit a polynomial of the given degree to (x, y) by least squares.

    Args:
        x: list/array of input values, length n
        y: list/array of target values, length n
        degree: non-negative integer, the polynomial degree

    Returns:
        List of coefficients [c_0, c_1, ..., c_degree] in increasing power order.
    """
    x_arr = np.array(x, dtype = float)
    y_arr = np.array(y, dtype = float)
    X = np.vander(x_arr, degree+1, increasing = True)
    XTX = np.dot(X.T, X)
    XTY = np.dot(X.T, y_arr)
    C = np.linalg.solve(XTX, XTY)
    return C.tolist()


