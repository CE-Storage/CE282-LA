import math
import numpy as np


def vector_generator(size: int, scale: int) -> np.ndarray:
    random_vector = np.random.rand(size)
    random_vector *= scale
    random_vector = np.floor(random_vector)
    return random_vector


def matrix_generator(n: int, m: int, scale: int) -> np.ndarray:
    p = []
    for i in range(n):
        p.append(vector_generator(m, scale))
    p = np.array(p)
    return p

def gram_schmidt_test(A: np.ndarray, B: np.ndarray):
    Q, R = np.linalg.qr(A)
    Q2 = -Q
    B = np.abs(B)
    Q = np.abs(Q)
    tolerance = 1e-6
    if np.allclose(Q, B, atol=tolerance):
        print("\033[32mPassed!\033[0m")
    elif np.allclose(-Q, B, atol=tolerance):
        print("\033[32mPassed!\033[0m")
    else:
        print("\033[31mFailed!\033[0m : reconstructed vector isn't equal to the starting vector")
    print("---------------")

def change_of_basis_test(va: np.ndarray, vb: np.ndarray, A: np.ndarray, B: np.ndarray):
    p = np.linalg.inv(A) @ B
    reconstructed = (p @ vb)
    tolerance = 1e-6
    if np.allclose(reconstructed, va, atol=tolerance):
        print("\033[32mPassed!\033[0m")
    else:
        print("\033[31mFailed!\033[0m : reconstructed vector isn't equal to the starting vector")
    print("---------------")

#-----------------------------------------
def sin(x):
    return math.sin(x * math.pi / 180)


def cos(x):
    return math.cos(x * math.pi / 180)


def make_vector(theta, semiMajorAxis, eccentricity, argument_of_perihelion, longitude_of_ascending_node, inclination):
    if eccentricity < 1:
        r = semiMajorAxis * (1 - eccentricity ** 2) / (1 + eccentricity * cos(theta))
    elif eccentricity == 1:
        r = 2 * semiMajorAxis / (1 + cos(theta))
    else:
        r = - semiMajorAxis * (1 - eccentricity ** 2) / (1 + eccentricity * cos(theta))
    vector = [r * (cos(argument_of_perihelion + theta) * cos(longitude_of_ascending_node)\
                   - sin(argument_of_perihelion + theta) * sin(longitude_of_ascending_node) * cos(inclination)),\
              r * (cos(theta + argument_of_perihelion) * sin(longitude_of_ascending_node)\
                   + sin(theta + argument_of_perihelion) * cos(longitude_of_ascending_node) * cos(inclination)),\
              r * sin(theta + argument_of_perihelion) * sin(inclination)]
    return np.array(vector)


# Mercury's orbit
argument_of_perihelion = 29.124
longitude_of_ascending_node = 48.331
inclination = 7.005
semiMajorAxis = 0.387098
eccentricity = 0.205630


true_anomalies = [10, 40, 80, 160, 220]
observer_vector = [70, 30, 1]
new_vectors1 = [make_vector(anomaly, semiMajorAxis, eccentricity, argument_of_perihelion, longitude_of_ascending_node, inclination) - observer_vector\
           for anomaly in true_anomalies]

# Earth's orbit
argument_of_perihelion = 288.064
longitude_of_ascending_node = 174.873174
inclination = 7.155
semiMajorAxis = 1.0000010178
eccentricity = 0.0167086

new_vectors2 = [make_vector(anomaly, semiMajorAxis, eccentricity, argument_of_perihelion, longitude_of_ascending_node, inclination) - observer_vector\
                for anomaly in true_anomalies]

# Halley's comet
argument_of_perihelion = 111.05
longitude_of_ascending_node = 59.396
inclination = 161.96
semiMajorAxis = 17.737
eccentricity = 0.96658

new_vectors3 = [make_vector(anomaly, semiMajorAxis, eccentricity, argument_of_perihelion, longitude_of_ascending_node, inclination) - observer_vector\
               for anomaly in true_anomalies]

# Random parabolic orbit
argument_of_perihelion = 40
longitude_of_ascending_node = 10
inclination = 10.007
semiMajorAxis = 0.845612
eccentricity = 1

new_vectors4 = [make_vector(anomaly, semiMajorAxis, eccentricity, argument_of_perihelion, longitude_of_ascending_node, inclination) - observer_vector\
                for anomaly in true_anomalies]

# Random hyperbolic orbit
argument_of_perihelion = 40
longitude_of_ascending_node = 10
inclination = 10.007
semiMajorAxis = 8.5001
eccentricity = 7.002

new_vectors5 = [make_vector(anomaly, semiMajorAxis, eccentricity, argument_of_perihelion, longitude_of_ascending_node, inclination) - observer_vector\
                for anomaly in true_anomalies]

vectors = np.array([new_vectors1, new_vectors2, new_vectors3, new_vectors4, new_vectors5])