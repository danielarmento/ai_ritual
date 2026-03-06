#!/usr/bin/env python3
import numpy as np
from deepengine import Dense, ReLU, Sigmoid, Model

# Load weights
data = np.load("weights.npz")
W0, b0 = data["W_0"], data["b_0"]
W1, b1 = data["W_1"], data["b_1"]

# Build model
model = Model(
    layers=[
        Dense(2, 4),
        ReLU(),
        Dense(4, 1),
        Sigmoid()
    ],
    loss=None
)

model.layers[0].W = W0
model.layers[0].b = b0
model.layers[2].W = W1
model.layers[2].b = b1

# Test XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]], float)

print("\n=== XOR Demo Results ===")
for x in X:
    pred = model.predict(x.reshape(1,-1))[0][0]
    print(f"{x} → {pred:.4f}")
