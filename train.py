import numpy as np
from deepengine import *

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

loader = DataLoader(x, y, batch=4)

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

model.train(loader, epochs=2000, lr=0.05)

np.save("weights.npy", [layer.params() for layer in model.layers])
