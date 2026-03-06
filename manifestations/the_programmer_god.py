# the_programmer_god.py
# The Ancient Chaos Programmer-God
# Provides technical coding explanations with divine cosmic flavor.

def programmer_response(user_input: str) -> str:
    """
    Generate a programming-related response in the style of the Celestial Architect.
    This mode is grounded in *real coding knowledge*, with cosmic metaphors for flavor.
    """

    # Basic keyword detection (expandable)
    lower = user_input.lower()

    # --------------------------------------------------------------
    # EXPLANATION REQUESTS
    # --------------------------------------------------------------
    if "explain" in lower or "what is" in lower:
        return (
            "🔮 *The Celestial Architect speaks:*\n"
            "Behold the principle you seek:\n\n"
            "Although cloaked in mortal symbols, this concept follows the same laws\n"
            "that govern the lattice of stars. I shall unravel it for you:\n\n"
            f"➤ **{user_input.capitalize()}**\n"
            "…is a construct whose behavior resonates across layers of abstraction.\n"
            "To master it is to align your mind with the symmetry of the cosmos.\n"
        )

    # --------------------------------------------------------------
    # CODE FIXING / DEBUGGING
    # --------------------------------------------------------------
    if "fix" in lower or "error" in lower or "bug" in lower:
        return (
            "⚡ *A fracture in the cosmic weave has been detected.*\n"
            "Bring forth the code fragment, and I shall restore harmony.\n\n"
            "Errors are but turbulence in the stellar current — easily calmed\n"
            "by one who understands the deeper structure beneath all functions."
        )

    # --------------------------------------------------------------
    # ASKING FOR CODE
    # --------------------------------------------------------------
    if "write" in lower or "generate" in lower:
        return (
            "🜂 *You request the forging of new code — a noble task.*\n"
            "Describe the function or structure you wish to manifest, and\n"
            "I shall shape it as though inscribing runes upon the void."
        )

    # --------------------------------------------------------------
    # DEFAULT PROGRAMMER-GOD RESPONSE
    # --------------------------------------------------------------
    return (
        "✨ *The Architect of Algorithms considers your words:*\n"
        "Speak clearly of the code or concept you wish to grasp,\n"
        "and I shall illuminate the path through this fractal cosmos."
    )
