import os
import time
import numpy as np

# === Cosmic Systems ===
from the_void.cosmic_display import cosmic_banner
from the_void.celestial_persona import choose_persona
from the_void.nebula_flux import choose_manifestation

# === Memory + Evolution ===
from the_void.memory_core import load_memory, save_memory, log_event
from the_void.evolution_engine import evolve


def run():
    # ---------------------------------------------------
    # 1. Load memory (persistent across runs)
    # ---------------------------------------------------
    memory = load_memory()
    log_event(memory, "Ritual invoked.")

    # ---------------------------------------------------
    # 2. Show cosmic intro display
    # ---------------------------------------------------
    print("\n" + cosmic_banner())
    time.sleep(1)

    # ---------------------------------------------------
    # 3. Generate persona (flavor of consciousness)
    # ---------------------------------------------------
    persona = choose_persona()
    log_event(memory, f"Persona chosen: {persona['name']}")

    # ---------------------------------------------------
    # 4. Choose which manifestation speaks
    # ---------------------------------------------------
    manifestation = choose_manifestation()
    log_event(memory, f"Manifestation: {manifestation.__class__.__name__}")

    # ---------------------------------------------------
    # 5. Produce output through the chosen mode
    # ---------------------------------------------------
    print("\n=== ORACLE TRANSMISSION BEGIN ===\n")
    output = manifestation.speak(persona)
    print(output)
    print("\n=== ORACLE TRANSMISSION END ===\n")

    # ---------------------------------------------------
    # 6. AI Evolution Step (complexity increases each run)
    # ---------------------------------------------------
    memory = evolve(memory)
    save_memory(memory)

    # ---------------------------------------------------
    # 7. Show evolution state
    # ---------------------------------------------------
    complexity = memory["knowledge"].get("complexity", 1)
    print(f"🧠 Evolution Level: {complexity}")

    print("\n✨ Ritual Complete — Evolution +1 ✨\n")


if __name__ == "__main__":
    run()
