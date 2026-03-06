# fractal_filters.py
# Chaotic ASCII fractal distortion effects for the COSMIC CHAOS DEITY AI

import random
from sigils.chaos_colors import color_cycle

def fractal_noise_line(width: int, step: int) -> str:
    """
    Generates a single line of chaotic fractal-like ASCII noise.
    """
    chars = ["*", "+", ".", ":", "~", "^"]
    line = ""

    for i in range(width):
        ch = random.choice(chars)
        colored = color_cycle(ch, step + i)
        line += colored

    return line


def plasma_ripple(text: str, intensity: int = 3) -> str:
    """
    Distorts text by adding chaotic nebula ripples.
    """
    distorted = ""
    for i, ch in enumerate(text):
        offset = random.randint(-intensity, intensity)
        idx = (i + offset) % (intensity * 5 + 1)
        distorted += color_cycle(ch, idx)
    return distorted


def chaos_stutter(text: str, chance: float = 0.2) -> str:
    """
    Randomly stutters/duplicates characters for a cosmic glitch effect.
    """
    out = ""
    for ch in text:
        out += ch
        if random.random() < chance:
            out += color_cycle(ch, random.randint(0, 20))
    return out


def generate_fractal_block(lines: int, width: int, step: int) -> str:
    """
    Generates a block of fractal ASCII noise.
    """
    block = []
    for i in range(lines):
        block.append(fractal_noise_line(width, step + i))
    return "\n".join(block)
