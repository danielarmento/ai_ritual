import time
import os
import numpy as np
from deepengine import Model, Dense, ReLU, Sigmoid
from ritual_display import ritual_animation
from demo import xor_demo

# ----------------------------------------------------
# Load XOR-trained neural network
# ----------------------------------------------------

def load_model():
    # Model structure must match train.py
    model = Model(
        layers=[
            Dense(2, 4),
            ReLU(),
            Dense(4, 1),
            Sigmoid()
        ],
        loss=None,
        optimizer=None
    )

    if os.path.exists("weights.npz"):
        data = np.load("weights.npz", allow_pickle=True)
        weights = data["weights"]

        # First layer
        model.layers[0].W = weights.item().get("dense1_W")
        model.layers[0].b = weights.item().get("dense1_b")

        # Second layer
        model.layers[2].W = weights.item().get("dense2_W")
        model.layers[2].b = weights.item().get("dense2_b")

        print("\n[✓] Loaded saved neural network weights.\n")
    else:
        print("\n[!] No weights found — run train.py first.\n")

    return model

# ----------------------------------------------------
# Ritual runtime display
# ----------------------------------------------------

def run():
    os.system("clear")
    print("🌙 Starting Ritual AI...\n")
    time.sleep(1)

    ritual_animation()    # animated display
    model = load_model()  # load neural network

    print("Performing XOR demo:\n")
    xor_demo(model)

    print("\n✨ Ritual Complete.\n")

if __name__ == "__main__":
    run()
