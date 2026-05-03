import time
import sys
import time
import pyttsx3

engine = pyttsx3.init()

#variable definition and initialization 

max_floor : int = 10
min_floor : int = 0

current_floor : int
next_floor : int

direction : int #1 is up and 0 is down -  like binary representation of direction x-when idle and M when under maintenance

overload_status : int
capacity : int
current_load : int
door_status : int #1 is open and 0 is closed - like binary representation of door status
is_moving : int #1 is moving and 0 is stationary - like binary representation of movement status only when door closed

call_up : list[int] #list of floors where up button is pressed
call_down : list[int] #list of floors where down button is pressed

ascending_queue : list[int] #list of floors to stop at while going up
descending_queue : list[int] #list of floors to stop at while going down

pending_up : list[int] #list of floors where up button is pressed while going down
pending_down : list[int] #list of floors where down button is pressed while going up

trip_history : list[tuple]  #list of tuples (floor, direction) representing the history of trips made by the lift  
error_logs : list[str]  #list of strings representing error messages logged during operation
maintenance_logs : list[str]  #list of strings representing maintenance activities performed on the lift
request_times : list[tuple]

alarm_status : bool #1 is on and 0 is off - like binary representation of alarm status  ///DONE///

emergency_triggered : int #1 is triggered and 0 is not triggered - like binary representation of emergency status ///DONE///
emergency_contacted : int #contact information for emergency situations ///DONE///
emergency_contacts : list[tuple[str, str]]   # ///DONE///

maintenance_mode : bool #True if the lift is in maintenance mode, False otherwise    ///DONE///
fault_code  : int #integer representing the current fault code of the lift, if any   ///DONE///

vip_mode : bool #True if the lift is in VIP mode, False otherwise     /////LLATER STAGES//////

is_on : bool #True if the lift is powered on, False otherwise  ///DONE///

choice : int #variable to store user choice in the menu ///DONE///


# Function to initialize the lift
def initialize_lift():
    is_on = False

    while True:
        print("...... Lift Management System ......")
        print("1. Power On Lift")
        print("2. Power Off Lift")
        print("3. View lift status")
        print("4. Maintenance Mode")
        print("5. Exit")
        
        print("===================================")
        choice = input("Enter your choice: ")
        print("===================================")

        if choice == '1':
            is_on = True
            print("===================================")
            print("Lift powered on successfully.")
            print(f"Lift status: {'On' if is_on else 'Off'}")
            print("===================================")
        elif choice == '2':
            is_on = False
            print("===================================")
            print("Lift powered off successfully.")
            print(f"Lift status: {'On' if is_on else 'Off'}")
            print("===================================")
        elif choice == '3':
            print("===================================")
            print(f"Lift Status: {'On' if is_on else 'Off'}")
            print("===================================")
        elif choice == '4':
            maintenance()
        elif choice == '5':
            print("===================================")
            print("Exiting Lift Management System.")
            print("===================================")
            break
        else:
            print("Invalid choice. Please try again.")

def maintenance():
    maintenance_mode = True

    while True:
        print("Checking maintenance status...")
        #Check lift status and perform necessary maintenance tasks
        print("Which maintenance tasks would you like to perform?")
        print("1. Check lift Status")
        print("2. View maintenance logs")
        print("3. View trip history")    
        print("4. View error logs")
        print("5. Fault messages")
        print("6. Perform routine maintenance")
        print("7. View request times")
        print("8. Manage emergency contacts")
        print("9. Full system diagnostics")
        print("10. Manage VIP mode settings")
        print("11. Exit maintenance mode")

        print("===================================")
        choice = input("Enter your choice: ")
        print("===================================")


        if choice == '1':
            print("===================================")
            print("Checking lift status...")
            print("===================================")
            # Code to check lift status
        elif choice == '2':
            print("===================================")
            print("Viewing maintenance logs...")
            print("===================================")
            # Code to view maintenance logs
        elif choice == '3':
            print("===================================")
            print("Viewing trip history...")
            print("===================================")
            # Code to view trip history
        elif choice == '4':
            print("===================================")
            print("Viewing error logs...")
            print("===================================")
            # Code to view error logs
        elif choice == '5':
            print("===================================")
            print("Viewing fault messages...")
            for i in range(9):
                handle_fault(i)
            print("===================================")
            # Code to view fault messages
        elif choice == '6':
            print("===================================")
            print("Performing routine maintenance...")
            print("===================================")
            # Code to perform routine maintenance
        elif choice == '7':
            print("===================================")
            print("Viewing request times...")
            print("===================================")
            # Code to view request times
        elif choice == '8':
            print("===================================")
            print("Managing emergency contacts...")
            print("===================================")
            # Code to manage emergency contacts
        elif choice == '9':
            print("===================================")
            print("Performing full system diagnostics...")
            print("===================================")
            # Code to perform full system diagnostics
        elif choice == '10':
            print("===================================")
            print("Managing VIP mode settings...")
            print("===================================")
            # Code to manage VIP mode settings        
        elif choice == '11':
            print("===================================")
            print("Exiting maintenance mode...")
            print("===================================")
            break
        else:
            print("Invalid choice. Please try again.")



    # Code to perform maintenance tasks
    print("==========================================================")
    print("Maintenance tasks completed. Exiting maintenance mode.")    
    print("==========================================================")

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

def menu():
    while True:
        print("...... Lift Management System ......")
        print("1. POWER")
        print("2. MAINTENANCE")
        print("3. EMERGENCY")
        print("4. VIP MODE")
        print("5. Exit")
        
        print("===================================")
        choice = input("Enter your choice: ")
        print("===================================")

        if choice == '1':
            is_on = True
            print("===================================")
            initialize_lift()
            print("===================================")
        elif choice == '2':
            is_on = False
            print("===================================")
            maintenance()
            print("===================================")
        elif choice == '3':
            print("===================================")
            handle_emergency()
            print("===================================")
        elif choice == '4':
            print("===================================")
            print("VIP mode is currently under development. Please check back later.")
            #handle_vip_mode()
            print("===================================")
        elif choice == '5':
            print("===================================")
            print("Exiting Lift Management System.")
            print("===================================")
            break
        else:
            print("Invalid choice. Please try again.")

menu()



