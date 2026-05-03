import time
import pyttsx3

engine = pyttsx3.init()

current_floor = 0
target_floor = 3

while current_floor < target_floor:
    current_floor += 1
    time.sleep(3)
    engine.say(f"Floor {current_floor}")
    engine.runAndWait()
    print("Lift at floor:", current_floor)

time.sleep(3)
engine.say(f"Doors Opening")
engine.runAndWait()
print("Doors Opening")

time.sleep(3)
engine.say(f"Doors Closing")
engine.runAndWait()
print("Doors Closing")
