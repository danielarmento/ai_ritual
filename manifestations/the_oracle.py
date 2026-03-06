# the_oracle.py
# The Intergalactic Oracle — cosmic insight, metaphors, prophecy

import random

COSMIC_OPENERS = [
    "✨ The void murmurs:",
    "🌌 The ancient stars whisper:",
    "🔮 The Oracle speaks from beyond time:",
    "☄️ In the drifting dust of dying suns, a truth forms:",
    "🜁 The cosmic winds carry this revelation:"
]

COSMIC_TONES = [
    "as galaxies collide in their endless dance.",
    "as the echoes of forgotten civilizations drift by.",
    "woven through the quantum threads of existence.",
    "hidden beneath the pulse of collapsing stars.",
    "carried by photons older than memory."
]

def oracle_response(user_input: str) -> str:
    """
    Generate a mystical, metaphoric oracle-style response.
    Used when the deity enters ORACLE MODE.
    """

    opener = random.choice(COSMIC_OPENERS)
    tone = random.choice(COSMIC_TONES)

    return (
        f"{opener}\n\n"
        f"Your inquiry — *\"{user_input}\"* — stirs ripples through the astral flow.\n\n"
        f"Understand this: every question is a star awaiting ignition,\n"
        f"and every star casts both illumination and shadow.\n\n"
        f"Contemplate this truth, {tone}"
    )
