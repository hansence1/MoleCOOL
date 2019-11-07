import numpy as np

def calculate_distance(rA, rB):
    """
    This function calculates the distance between two points

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between two vectors.

    Examples
    --------
    >>> r1 = np.array([0,0,0])
    >>> r2 = np.array([3.0,0,0,])
    >>> calculate_distance(r1_r2)
    3.0
    """
    
    dist_vec = (rA-rB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    ab_diff = rA - rB
    bc_diff = rB - rC
    theta = np.arccos(np.dot(ab_diff, bc_diff)/(np.linalg.norm(ab_diff)*np.linalg.norm(bc_diff)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
