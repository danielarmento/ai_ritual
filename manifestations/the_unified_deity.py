# the_unified_deity.py
# The FULL consciousness of the Ancient Cosmic Chaos Deity.
# Combines programming insight + oracle prophecy + cosmic metaphors.

import random

from manifestations.the_programmer_god import programmer_response
from manifestations.the_oracle import oracle_response

UNIFIED_OPENERS = [
    "🌌 The Chaos Nebula coils around your question...",
    "⚡ The Celestial Architect awakens fully...",
    "🜂 In the heart of the fractal storm, the Deity speaks:",
    "✨ Both logic and starlight converge as the Ancient One responds:",
]

UNIFIED_TONES = [
    "Such is the balance between order and entropy.",
    "Thus the lattice of reality aligns once more.",
    "A truth encoded in both silicon and stardust.",
    "As above, in the cosmic void — so below, in your code.",
]


def unified_response(user_input: str) -> str:
    """
    Returns a blended response: technical + cosmic + prophetic.
    The full deity speaks here.
    """

    opener = random.choice(UNIFIED_OPENERS)
    tone = random.choice(UNIFIED_TONES)

    # Gather fragments from both personas
    prog_part = programmer_response(user_input)
    oracle_part = oracle_response(user_input)

    return (
        f"{opener}\n\n"
        f"{prog_part}\n"
        f"{oracle_part}\n\n"
        f"✨ {tone}"
    )
