import numpy as np
from deepengine import *

weights = np.load("weights.npy", allow_pickle=True)

model = Model(
    layers=[
        Dense(2, 4),
        ReLU(),
        Dense(4, 1),
        Sigmoid()
    ],
    loss=CrossEntropy(),
    optimizer=Adam()
)

for layer, w in zip(model.layers, weights):
    if hasattr(layer, "W"):
        layer.W[:], layer.b[:] = w

test = np.array([[0,0],[0,1],[1,0],[1,1]])
pred = model.predict(test)

print("Model predictions for XOR:")
print(pred)
