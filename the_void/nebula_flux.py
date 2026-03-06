# nebula_flux.py
# Internal aesthetic chaos-state engine for the Ancient Cosmic Chaos Deity AI

import random

class NebulaFlux:
    """
    Represents the shifting internal energies of the Chaos Nebula.
    Purely aesthetic — influences tone & visual intensity only.
    """

    def __init__(self):
        self.entropy = 0.5      # 0 (calm) → 1 (chaotic)
        self.pulse = 1.0        # intensity of nebula surges
        self.disruption = 0.3   # probability of chaotic styling

    def fluctuate(self):
        """Randomly modulates the nebula's internal parameters."""
        self.entropy = min(1.0, max(0.0, self.entropy + random.uniform(-0.1, 0.1)))
        self.pulse = min(2.0, max(0.5, self.pulse + random.uniform(-0.2, 0.2)))
        self.disruption = min(1.0, max(0.0, self.disruption + random.uniform(-0.05, 0.05)))

    def signature(self) -> str:
        """
        Returns a short line describing the nebula's current 'mood'.
        Purely atmosphere.
        """
        if self.entropy < 0.3:
            return "🌑 The nebula rests in quiet harmonic resonance."
        elif self.entropy < 0.6:
            return "🌌 The nebula hums with balanced cosmic energy."
        else:
            return "⚡ The nebula crackles with volatile stellar chaos!"

# global shared instance
flux = NebulaFlux()
