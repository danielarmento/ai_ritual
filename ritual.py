# ritual.py
# Main launcher for the Ancient Cosmic Chaos Deity AI system.

import time

from the_void.cosmic_display import deity_arrival
from the_void.celestial_persona import persona
from the_void.deepengine import deep_core
from the_void.nebula_flux import flux


# --------------------------------------------------------------
# MODE SELECTION MENU
# --------------------------------------------------------------
def choose_mode():
    print("\nChoose the aspect of the Deity to invoke:\n")
    print("  1) ⚡ Programmer-God (technical, code-focused)")
    print("  2) 🔮 Oracle (prophecy, cosmic metaphor)")
    print("  3) 🌌 Unified Deity (both combined)\n")

    choice = input("Your selection: ").strip()

    if choice == "1":
        persona.set_mode("programmer")
        print("\nYou have invoked: ⚡ THE CELESTIAL PROGRAMMER-GOD\n")
    elif choice == "2":
        persona.set_mode("oracle")
        print("\nYou have invoked: 🔮 THE INTERGALACTIC ORACLE\n")
    elif choice == "3":
        persona.set_mode("unified")
        print("\nYou have invoked: 🌌 THE SUPREME CHAOS DEITY\n")
    else:
        print("Invalid choice. Defaulting to Unified Mode.\n")
        persona.set_mode("unified")


# --------------------------------------------------------------
# INTERACTIVE LOOP
# --------------------------------------------------------------
def begin_ritual():
    deity_arrival()  # Show cosmic animation
    choose_mode()

    print("Type 'exit' to end the ritual.\n")

    while True:
        user_input = input("🜄 Speak to the Deity:\n> ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("\n🌑 The nebula dims as the Deity withdraws...\n")
            break

        # Internal chaos-state signature
        core_sig = deep_core.compute(user_input)
        nebula_state = flux.signature()

        # Deity response
        answer = persona.speak(user_input)

        print("\n" + "-" * 60)
        print(answer)
        print("\n" + core_sig)
        print(nebula_state)
        print("-" * 60 + "\n")


# --------------------------------------------------------------
# ENTRY POINT
# --------------------------------------------------------------
if __name__ == "__main__":
    begin_ritual()
