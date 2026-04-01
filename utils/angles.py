import numpy as np

def calc_angle(a, b, c):
    a = np.array([a.x, a.y])
    b = np.array([b.x, b.y])
    c = np.array([c.x, c.y])

    ab = a - b
    bc = c - b

    angle = np.arccos(
        np.dot(ab, bc) / (np.linalg.norm(ab) * np.linalg.norm(bc))
    )
    return np.degrees(angle)