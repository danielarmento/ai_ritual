#!/usr/bin/env python3
import numpy as np
from deepengine import Dense, ReLU, Sigmoid, Model, CrossEntropy, DataLoader

# XOR dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([[0],[1],[1],[0]], dtype=float)

# Build model
model = Model(
    layers = [
        Dense(2, 4),
        ReLU(),
        Dense(4, 1),
        Sigmoid()
    ],
    loss = CrossEntropy(),
    optimizer = None
)

loader = DataLoader(X, y, batch=4)

# Train
epochs = 2000
lr = 0.1

print("Training XOR Neural Network...\n")

for epoch in range(1, epochs+1):
    losses = []
    for batch_x, batch_y in loader:
        out = model.forward(batch_x)
        loss_value = model.loss.forward(out, batch_y)
        grad = model.loss.backward()
        model.backward(grad, lr)
        losses.append(loss_value)

    if epoch == 1 or epoch % 100 == 0:
        print(f"Epoch {epoch}/{epochs} — Loss: {np.mean(losses):.6f}")

# Save weights
params = {}
index = 0
for layer in model.layers:
    if hasattr(layer, "params"):
        W, b = layer.params()
        params[f"W_{index}"] = W
        params[f"b_{index}"] = b
        index += 1

np.savez("weights.npz", **params)

print("\nTraining complete. Saved weights to weights.npz.")
