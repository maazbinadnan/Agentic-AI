# 2. Functional Requirements

### FR-001
- **Requirement:** The system shall authenticate users through a web interface using a valid username and password before permitting access to DigitalHome monitoring, control, planning, reporting, or administration functions.
- **Source Need:** UN-005
- **Priority:** High

### FR-002
- **Requirement:** The system shall provide role-based access control such that General Users can monitor and control home environmental and power-management functions, while Master Users and DH Technicians can additionally configure system parameters, maintain user accounts, and start or stop system operation.
- **Source Need:** UN-005, UN-006, UN-007, UN-008
- **Priority:** High

### FR-003
- **Requirement:** The system shall allow authenticated users to log out from the web interface and shall terminate access to protected functions after logout.
- **Source Need:** UN-005
- **Priority:** Medium

### FR-004
- **Requirement:** The system shall provide a home web server that supports user interaction with DigitalHome devices, stores DigitalHome plans and operational data, maintains user account records, and provides backup support for user account information, user plans, and the home database.
- **Source Need:** UN-001, UN-003, UN-004, UN-005, UN-009
- **Priority:** High

### FR-005
- **Requirement:** The system shall communicate between the web server and DigitalHome sensors and controllers through a home gateway that connects to a broadband Internet connection and exchanges wireless RF messages with DigitalHome devices over an indoor transmission range of up to 1000 feet.
- **Source Need:** UN-001, UN-002, UN-009
- **Priority:** High

### FR-006
- **Requirement:** The system shall present authenticated General Users with current monitored home status information through the web interface, including current temperature readings, current humidity readings, door and window contact states, alarm status, and appliance or lighting power states.
- **Source Need:** UN-001
- **Priority:** High

### FR-007
- **Requirement:** The system shall support digital programmable thermostats by receiving current temperature readings, displaying the readings to users, accepting a user-entered temperature set point, and switching connected heating or cooling control outputs on or off as needed to regulate the enclosed space toward the set point within the thermostat sensing range of 14°F to 104°F (-10°C to 40°C).
- **Source Need:** UN-001, UN-002
- **Priority:** High

### FR-008
- **Requirement:** The system shall support digital programmable humidistats by receiving current humidity readings, displaying the readings to users, accepting a user-entered humidity set point, and switching humidifier or dehumidifier control outputs as needed to regulate the enclosed space toward the set point.
- **Source Need:** UN-001, UN-002
- **Priority:** High

### FR-009
- **Requirement:** The system shall support digital programmable power switches by monitoring and displaying the current on/off state of each connected small appliance or lighting unit and by allowing authorized users to issue commands that change the power switch state from off to on or from on to off.
- **Source Need:** UN-001, UN-002
- **Priority:** High

### FR-010
- **Requirement:** The system shall support magnetic alarm contact switches for doors and windows and shall detect and display whether each active contact sensor indicates a normal closed state or an entry breach state.
- **Source Need:** UN-001
- **Priority:** High

### FR-011
- **Requirement:** The system shall activate configured security sound alarms and light alarms when it detects a security breach from an active magnetic contact switch and shall display the resulting alarm state through the web interface.
- **Source Need:** UN-001, UN-002
- **Priority:** High

### FR-012
- **Requirement:** The system shall allow General Users to create, view, update, and store monthly plans that define scheduled DigitalHome behavior for supported environmental and power-managed devices.
- **Source Need:** UN-003, UN-009
- **Priority:** High

### FR-013
- **Requirement:** The system shall allow General Users to create, view, update, and store daily presets or schedules that specify planned thermostat set points, humidistat set points, and power switch states for supported devices.
- **Source Need:** UN-003, UN-009
- **Priority:** High

### FR-014
- **Requirement:** The system shall execute stored monthly plans and daily presets by applying the scheduled set points or power states to the targeted supported devices at the planned times.
- **Source Need:** UN-003
- **Priority:** High

### FR-015
- **Requirement:** The system shall store historical operational data for supported monitored and controlled devices and shall provide historical reports through the web interface that include averages, minimum values, maximum values, and downtime logs.
- **Source Need:** UN-004, UN-009
- **Priority:** High

### FR-016
- **Requirement:** The system shall allow Master Users and DH Technicians to create, view, update, and maintain DigitalHome user accounts through the web interface.
- **Source Need:** UN-006, UN-007
- **Priority:** High

### FR-017
- **Requirement:** The system shall allow Master Users and DH Technicians to configure and update system default parameters through the web interface.
- **Source Need:** UN-006, UN-007
- **Priority:** High

### FR-018
- **Requirement:** The system shall allow Master Users and DH Technicians to start and stop DigitalHome system operation through the web interface.
- **Source Need:** UN-007, UN-008
- **Priority:** Medium

### FR-019
- **Requirement:** The system shall perform backup of user account information, user plans, and the home database so that stored DigitalHome configuration and usage information can be preserved for later recovery.
- **Source Need:** UN-009
- **Priority:** Medium

### FR-020
- **Requirement:** The system shall operate all monitoring, control, planning, reporting, account-management, and backup functions against simulated sensors, controllers, and home conditions that represent the behavior and constraints of an actual home environment.
- **Source Need:** UN-001, UN-002, UN-003, UN-004, UN-007, UN-009
- **Priority:** Medium

### FR-021
- **Requirement:** The system shall require broadband Internet service availability for remote communication between the home web server, gateway, and authenticated users accessing the DigitalHome web interface.
- **Source Need:** UN-001, UN-002, UN-005
- **Priority:** Medium