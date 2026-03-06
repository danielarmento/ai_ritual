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

    def params(self): return [self.W, self.b]


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


class Softmax:
    def forward(self, x):
        e = np.exp(x - np.max(x, axis=1, keepdims=True))
        self.out = e / np.sum(e, axis=1, keepdims=True)
        return self.out

    def backward(self, grad, lr):
        return grad


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
# Optimizer
# ============================================================

class Adam:
    def __init__(self, b1=0.9, b2=0.999, eps=1e-8):
        self.m = {}
        self.v = {}
        self.b1 = b1
        self.b2 = b2
        self.eps = eps
        self.t = 0

    def update(self, params, grads, lr):
        self.t += 1
        for i, (p, g) in enumerate(zip(params, grads)):
            if i not in self.m:
                self.m[i] = np.zeros_like(g)
                self.v[i] = np.zeros_like(g)

            self.m[i] = self.b1*self.m[i] + (1-self.b1)*g
            self.v[i] = self.b2*self.v[i] + (1-self.b2)*(g**2)

            m_hat = self.m[i] / (1 - self.b1**self.t)
            v_hat = self.v[i] / (1 - self.b2**self.t)

            p -= lr * m_hat / (np.sqrt(v_hat) + self.eps)


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
    def __init__(self, layers, loss, optimizer):
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

    def train(self, loader, epochs=1000, lr=0.1):
        for epoch in range(1, epochs+1):
            losses = []
            for batch_x, batch_y in loader:
                out = self.forward(batch_x)
                loss_value = self.loss.forward(out, batch_y)
                grad = self.loss.backward()
                self.backward(grad, lr)
                losses.append(loss_value)

            if epoch % 100 == 0 or epoch == 1:
                print(f"Epoch {epoch}/{epochs} — Loss: {np.mean(losses):.6f}")

    def predict(self, x):
        return self.forward(x)
