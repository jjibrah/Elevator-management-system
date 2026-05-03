from alarms import sound_alarm
from variables import *


def handle_fault(fault_code):
    fault_messages = {
        0: "No fault detected.",
        1: "Overload detected. Reduce passenger load.",
        2: "Door obstruction or door jam detected.",
        3: "Power failure detected.",
        4: "Lift stuck between floors.",
        5: "Emergency alarm activated.",
        6: "Maintenance mode active.",
        7: "Motor malfunction detected.",
        8: "Sensor failure detected."
    }

    if fault_code in fault_messages:
        print(f"\nFault Code [{fault_code}]: {fault_messages[fault_code]}")
    else:
        print(f"\nFault Code [{fault_code}]: Unknown fault detected. Immediate inspection required.")

def handle_emergency():
    emergency_triggered = True
    emergency_contacted = False

    emergency_contacts = {
        "Fire Department": "911",
        "Medical Emergency": "999",
        "Building Security": "+254700000000",
        "Lift Maintenance Team": "+254711111111"
    }
    while True:
        print("Emergency situation detected!")
        print("1. Contact emergency services")
        print("2. View emergency contact information")
        print("3. Sound alarm")
        print("4. Exit emergency mode")

        print("===================================")
        choice = input("Enter your choice: ")
        print("===================================")

        if choice == '1':
            print("Contacting emergency services...")
            print(f"{list(emergency_contacts.keys())[0]}: {list(emergency_contacts.values())[0]}")
            print("===============================================")

            emergency_contacted = True
            break
        elif choice == '2':
            print("===================================")
            print("Emergency contact information:")
            for contact, number in emergency_contacts.items():
                print(f"{contact}: {number}")
            print("===================================")
        elif choice == '3':
            alarm_status = True
            while True:
                print("Sounding alarm... press 'q' then Enter to stop.")
                sound_alarm()  # Function to sound the alarm
                user_input = input()
                if user_input.lower() == 'q':
                    alarm_status = False
                    print("Alarm stopped.")
                    break

        elif choice == '4':
            print("Exiting emergency mode...")
            break
        else:
            print("Invalid choice. Please try again.")


    # Code to contact emergency services and provide necessary information
