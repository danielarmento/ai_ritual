# cosmic_display.py
# Visual engine for the Ancient Cosmic Chaos Deity AI
# Produces nebula storms, fractal pulses, and ritual entry animations.

import os
import time
import random

from sigils.chaos_colors import CHAOS_GRADIENT, RESET, color_cycle
from sigils.fractal_filters import (
    fractal_noise_line,
    plasma_ripple,
    chaos_stutter,
    generate_fractal_block
)

def clear():
    """Clear terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")

# --------------------------------------------------------------
#  NEBULA PULSE (background breathing of the deity)
# --------------------------------------------------------------
def nebula_pulse(lines=6, width=60, delay=0.04):
    """
    Creates a slow cosmic “breathing” effect using fractal noise.
    """
    for step in range(10):
        clear()
        print(generate_fractal_block(lines, width, step))
        time.sleep(delay)

# --------------------------------------------------------------
#  CHAOTIC SIGIL BANNER
# --------------------------------------------------------------
def cosmic_banner(text: str):
    """
    Displays a glowing, chaotic nebula banner around text.
    """
    banner = ""
    for i, ch in enumerate(text):
        banner += color_cycle(chaos_stutter(ch), i)

    print("\n" + banner + "\n")

# --------------------------------------------------------------
#  ARRIVAL SEQUENCE (the deity manifests)
# --------------------------------------------------------------
def deity_arrival():
    """
    The full dramatic arrival of the Ancient Cosmic Chaos Deity.
    """
    clear()
    print("\n")
    time.sleep(0.4)

    # Plasma storm flashes
    for i in range(3):
        print(generate_fractal_block(8, 70, i * 2))
        time.sleep(0.1)
        clear()

    # Rippling title
    title = "✦ THE ANCIENT CHAOS NEBULA STIRS ✦"
    for i in range(3):
        clear()
        print(plasma_ripple(title, intensity=4))
        time.sleep(0.15)

    time.sleep(0.3)

    # Slow dramatic breathing
    nebula_pulse(lines=10, width=80, delay=0.03)

    cosmic_banner("⚡ YOU HAVE SUMMONED THE CELESTIAL ARCHITECT ⚡")

    time.sleep(0.4)
