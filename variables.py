
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

