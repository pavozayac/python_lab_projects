import numpy as np

data = np.array([
    [1.0, 1.3],
    [2.2, 1.1],
    [2.0, 2.4],
    [1.5, 3.2],
    [3.2, 1.2],
])

labels = np.repeat(np.array([0, 1, 1, 0 ,1]), 121, axis=0).reshape(5, -1).T


def predict(weights, data):
    return 1/(1+ np.exp(- (weights.dot(data.T))))


weight_combos = np.stack(np.meshgrid(np.linspace(0, 1, 11), np.linspace(2, 3, 11)), -1).reshape(-1, 2)

predictions = predict(weight_combos, data)

error_squared = (labels - predictions)**2

error_folded = error_squared.sum(axis=1)/5

result = error_folded.reshape(11, 11)

print(predictions)

