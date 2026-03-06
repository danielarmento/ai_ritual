# chaos_colors.py
# CHAOS-NEBULA color palette (violet plasma storm)

RESET = "\033[0m"

# Nebula core colors
NEBULA_VIOLET = "\033[38;5;135m"     # bright violet
NEBULA_MAGENTA = "\033[38;5;201m"    # cosmic pink
NEBULA_WHITE = "\033[38;5;255m"      # white lightning

# For pulses and strobing effects
PULSE_1 = "\033[38;5;207m"
PULSE_2 = "\033[38;5;171m"
PULSE_3 = "\033[38;5;99m"

# Gradient sequence used for animations
CHAOS_GRADIENT = [
    NEBULA_VIOLET,
    NEBULA_MAGENTA,
    PULSE_1,
    PULSE_2,
    PULSE_3,
    NEBULA_WHITE,
]

def color_cycle(text: str, index: int) -> str:
    """
    Return text wrapped in a shifting cosmic nebula color.
    Used for animated fractal effects.
    """
    color = CHAOS_GRADIENT[index % len(CHAOS_GRADIENT)]
    return f"{color}{text}{RESET}"
