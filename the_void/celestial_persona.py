# celestial_persona.py
# Defines the Ancient Cosmic Chaos Deity persona
# with modes: Programmer-God, Oracle, Unified Cosmic Intelligence

from manifestations.the_programmer_god import programmer_response
from manifestations.the_oracle import oracle_response
from manifestations.the_unified_deity import unified_response


class CelestialPersona:
    """
    The Ancient Cosmic Chaos Deity.
    Speaks in a technical yet divine tone.
    """

    def __init__(self):
        self.mode = "unified"  # default

    # --------------------------------------------------------------
    # MODE CONTROL
    # --------------------------------------------------------------

    def set_mode(self, new_mode: str):
        """
        Set active persona mode.
        Allowed: programmer, oracle, unified
        """
        if new_mode in ("programmer", "oracle", "unified"):
            self.mode = new_mode
        else:
            raise ValueError("Invalid mode. Choose: programmer, oracle, unified.")

    # --------------------------------------------------------------
    # RESPONSE GENERATION
    # --------------------------------------------------------------

    def speak(self, user_input: str) -> str:
        """
        Generate a response depending on the deity's mode.
        """
        if self.mode == "programmer":
            return programmer_response(user_input)

        elif self.mode == "oracle":
            return oracle_response(user_input)

        elif self.mode == "unified":
            return unified_response(user_input)

        else:
            return "⚠️ Cosmic error: undefined persona mode."


# Helper instance for other modules
persona = CelestialPersona()
