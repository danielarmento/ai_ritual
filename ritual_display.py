#!/usr/bin/env python3
import time
import os
import sys

# Clear screen function
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# Frames for the animation
frames = [
"""
🌱 Growing roots...
""",
"""
🌿 Unfolding leaves...
""",
"""
🔥 Awakening inner fire...
""",
"""
💨 Breathing with the wind...
""",
"""
🌙 Gathering night energy...
""",
"""
✨ Aligning the inner pathways...
"""
]

# How long the animation should run (seconds)
DURATION = 6  # Change this if you want longer or shorter animation
FRAME_DELAY = 0.5

def main():
    start = time.time()

    while time.time() - start < DURATION:
        for frame in frames:
            clear()
            print(frame)
            sys.stdout.flush()
            time.sleep(FRAME_DELAY)

    # Final message after animation ends cleanly
    clear()
    print("✨ Ritual complete — initiating neural training... ✨")
    time.sleep(1)

if __name__ == "__main__":
    main()
