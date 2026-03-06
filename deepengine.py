import numpy as np

# ============================================================
# Layers
# ============================================================

class Dense:
    def __init__(self, inp, out):
        self.W = np.random.randn(inp, out) * np.sqrt(2/inp)
        self.b = np.zeros((1, out))

    def forward(self, x):
        self.x = x
        return x @ self.W + self.b

    def backward(self, grad, lr):
        dW = self.x.T @ grad
        db = grad.sum(0, keepdims=True)
        dx = grad @ self.W.T

        self.W -= lr * dW
        self.b -= lr * db
        return dx

    def params(self): 
        return [self.W, self.b]


class ReLU:
    def forward(self, x):
        self.mask = x > 0
        return x * self.mask

    def backward(self, grad, lr):
        return grad * self.mask


class Sigmoid:
    def forward(self, x):
        self.out = 1/(1+np.exp(-x))
        return self.out

    def backward(self, grad, lr):
        return grad * self.out * (1 - self.out)


# ============================================================
# Loss functions
# ============================================================

class CrossEntropy:
    def forward(self, pred, actual):
        pred = np.clip(pred, 1e-9, 1 - 1e-9)
        self.pred = pred
        self.actual = actual
        return -np.mean(actual*np.log(pred))

    def backward(self):
        pred = np.clip(self.pred, 1e-9, 1 - 1e-9)
        return (pred - self.actual) / self.actual.shape[0]


# ============================================================
# DataLoader
# ============================================================

class DataLoader:
    def __init__(self, x, y, batch=32):
        self.x = x
        self.y = y
        self.batch = batch

    def __iter__(self):
        idx = np.arange(len(self.x))
        np.random.shuffle(idx)
        for start in range(0, len(self.x), self.batch):
            end = start + self.batch
            b = idx[start:end]
            yield self.x[b], self.y[b]


# ============================================================
# Model
# ============================================================

class Model:
    def __init__(self, layers, loss, optimizer=None):
        self.layers = layers
        self.loss = loss
        self.opt = optimizer

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, grad, lr):
        for layer in reversed(self.layers):
            grad = layer.backward(grad, lr)
        return grad

    def predict(self, x):
        return self.forward(x)
