import time, os, itertools

frames = [
    "🌱 Growing roots...",
    "🌿 Unfolding leaves...",
    "🌾 Reaching toward the sun...",
    "🔥 Awakening inner fire...",
    "🌙 Breathing with the night..."
]

for f in itertools.cycle(frames):
    os.system("clear")
    print("\n" * 5)
    print(f.center(80))
    print("\n" * 2)
    time.sleep(1)
