import time
import sys
import time
import pyttsx3


engine = pyttsx3.init()
def sound_alarm(emergency_type="STUCK"):
    print("ALARM SYSTEM ACTIVATED! Awaiting response...")

    # Different alarm patterns based on emergency type
    patterns = {
        "GENERAL": [
            0.2, 0.2, 0.2, 0.4,
            0.2, 0.2, 0.2, 0.4,
            0.1, 0.1, 0.1, 0.2,
            0.5
        ],

        "OVERLOAD": [
            0.3, 0.3, 0.6,
            0.3, 0.3, 0.6
        ],

        "FIRE": [
            0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.2,
            0.1, 0.1, 0.1, 0.2
        ],

        "STUCK": [
            0.5, 0.2,
            0.5, 0.2,
            0.8
        ],

        "POWER_FAILURE": [
            0.7, 0.3,
            0.7, 0.3,
            1.0
        ]
    }

    pattern = patterns.get(emergency_type, patterns["GENERAL"])

    cycle_limit = 3
    cycle = 0

    while cycle < cycle_limit:
        print(f"\n[ALARM MODE: {emergency_type}] Cycle {cycle + 1}")

        for delay in pattern:
            print("\a", end="", flush=True)
            time.sleep(delay)

        cycle += 1

        # escalation logic
        if cycle == 2:
            print("ESCALATION: Increasing urgency level...")

    print("\nAlarm cycle complete. System remains in emergency monitoring mode.")
