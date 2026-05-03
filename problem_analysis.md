# lift management system 

## building 
number of stories (n) = 5;
idle lift - lift[0] -> goes back to the ground floor 

## inputs
Request the lift (outside) --> call
select destination (inside) --> destination

## operational functions 
open door (open)
close door (close)
sound alarm (alarm)
call emergency contact (emergency)

## Queues -> manages the ques of the pending stops for the lift 
Ascending queue
descending queue
pending descending queue
pending ascending queue

## basic logic of the lifts operations 
1. call the lift 
2. lift comes to the call zone 
3. you enter inside the lift
4. press the destination
5. lift goes to the destination 


## steps break down 
1. call the lift 

    if numerous calls comes into the system at the same time 
    check if the the call is above or below the lift 
    if above :
        prioritize the ascending case
    else: 
        prioritize descending scenario 


    if the zone of the lift reaches n || if the zone is a the greates value in the ascending queue 
        shift the scenario to descending 
    else if the zone is at 0 || if the zone is at the smallest value in descending queue
        shift the scenario to ascending  
    else 
        return idle() 


    function idle(){

        return lift[0]
    }

    if the lift move 


    (a)check if the lift is in the ascending loop (0-n)
        if yes:(ascending scenario)
            Check if the call is greater that the current floor 
                if yes
                    (b)check the zone if is in the queue 
                        if yes 
                            ignore the zone 
                        else 
                            add the zone in the acsending queue and sort the queue in the ascending order 
                else 
                    store the order in the pending up array 
                        check the zone if is in the queue 
                            if yes 
                                ignore the zone 
                            else 
                                add the zone in the acsending queue and sort the queue in the ascending order 
        else: (Descending scenario)
            Check if the call is smaller that the current floor 
                if yes
                    (b)check the zone if is in the queue 
                        if yes 
                            ignore the zone 
                        else 
                            add the zone in the descending queue and sort the queue in the descending order 
                else 
                    store the order in the pending down array 
                        check the zone if is in the queue 
                            if yes 
                                ignore the zone 
                            else 
                                add the zone in the descending queue and sort the queue in the descending order 


2. lift comes to the call zone
## arrays
lift current possition - current
lift next position - next
current direction - up/down - used to choose the algorithm to use either up or down 
capacity - max limit 

lift is at current position x
checks the next position and moves to the next position y in a delay (3 sec for now)
lift open doors 
user enters next position 
lift uses the algorithm to queue the request 

lift goes to the next position in the queue 
lift oopen doors

        

# Understanding 
we will need 2 algorithms for a start 
1. To manage the queuing of the requests from the users 
2. Manages how the lift operates with the queues 

3. in later stages we can optimize for the alarms and contacting emergency 


# arrarys involved with the lift
current lift possition lift[]  
next lift position lift_next[]


# arrarys involved with the calls
Ascending calls calls_up[]
Descending calls calls_down[]



# arrarys involved with the destinations
Descending cycle descending_queue[]
Ascending cycle ascending_queue[]

pending destination case pending_queue (when a person is going to floor 9 but we are descending we just store the value in the pending array before we change the cycle to avoid any loss of data and making them re enter the floor)
 