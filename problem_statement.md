# System Design Interview Question: Design a Lift (Elevator) Management System

## Question:

Design a scalable and fault-tolerant **Lift Management System** for a multi-story commercial building.

The system should efficiently manage multiple elevators, minimize passenger wait times, optimize energy usage, and ensure safety during emergencies.

---

# Functional Requirements:

### Passenger Features:

* Request elevator from any floor (Up/Down)
* Select destination floor inside elevator
* View elevator arrival status
* Emergency alarm button
* Door open/close controls

### Admin Features:

* Monitor elevator health/status
* Enable/disable elevators for maintenance
* Access usage logs
* Receive fault alerts
* Emergency override control

---

# Non-Functional Requirements:

* High availability
* Low latency response
* Real-time status updates
* Scalability for large buildings
* Fault tolerance
* Safety compliance
* Efficient resource utilization

---

# Constraints:

* Building may have:

  * 10–100 floors
  * 1–20 elevators
* Peak traffic periods
* VIP/service elevators
* Emergency situations:

  * Fire alarms
  * Power outages
  * Mechanical failures

---

# Key Design Challenges:

* Elevator scheduling algorithm
* Multi-elevator coordination
* Request prioritization
* Load balancing
* Handling simultaneous requests
* Real-time communication
* Failover mechanisms

---

# Interview Tasks:

## 1. Clarify Requirements

Discuss:

* Number of elevators/floors
* Traffic patterns
* Priority rules
* Safety constraints
* Monitoring needs

---

## 2. High-Level Architecture

Design components such as:

* Elevator Controller Service
* Request Scheduler
* Elevator State Manager
* User Interface Panels
* Monitoring Dashboard
* Database/Logs
* Emergency Control System

---

## 3. Database Design

Define schemas for:

* Elevators
* Floor requests
* Maintenance logs
* Emergency events
* Performance metrics

---

## 4. Core Algorithms

Explain:

* SCAN/LOOK scheduling
* Nearest car algorithm
* Peak traffic optimization
* Load balancing strategies

---

## 5. API Design

Example:

* POST /request-lift
* POST /select-floor
* GET /lift-status
* POST /emergency-stop
* GET /admin/logs

---

## 6. Scalability Considerations

* Distributed controller architecture
* Microservices vs monolith
* Event-driven systems
* Message queues
* Real-time telemetry

---

## 7. Fault Tolerance

* Elevator failure handling
* Redundant controllers
* Health checks
* Disaster recovery

---

## 8. Security

* Access control for admin
* Secure communication
* Audit trails
* Prevent unauthorized overrides

---

# Follow-Up Questions Interviewers May Ask:

### Basic:

* How would you assign the best elevator?
* How do you reduce wait time?

### Intermediate:

* How would you handle 50 simultaneous requests?
* How do you prioritize during rush hour?

### Advanced:

* Design for skyscrapers with express elevators
* How would AI improve prediction?
* How would you ensure zero downtime?

---

# Evaluation Criteria:

Interviewers assess:

* Requirement gathering
* System decomposition
* Trade-off analysis
* Scalability
* Algorithmic efficiency
* Reliability
* Communication clarity

---

# Bonus:

Design for:

### Smart IoT-enabled elevator systems

Including:

* Predictive maintenance
* Occupancy sensors
* Mobile app integration
* Energy optimization

---

# Expected Output From Candidate:

* Requirements breakdown
* Architecture diagram
* Database schema
* Scheduling algorithm
* API structure
* Scaling strategy
* Trade-off discussion

---

# Goal:

Demonstrate your ability to design a **real-world distributed control system** balancing:

### Efficiency + Safety + Scalability + Reliability
