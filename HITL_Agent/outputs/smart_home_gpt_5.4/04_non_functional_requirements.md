# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall present updated values for monitored temperature, humidity, contact sensor status, and appliance power state on the web interface within 2 seconds of receiving a new device or simulated device status update.
- **Source:** UN-001
- **Priority:** High

### NFR-002
- **Requirement:** The system shall refresh dashboard data for active monitoring sessions at least once every 5 seconds while a user is viewing the web interface.
- **Source:** UN-001
- **Priority:** High

### NFR-003
- **Requirement:** The system shall complete login, page load, and readiness for basic user interaction within 3 seconds for 95% of requests under normal prototype operating conditions.
- **Source:** UN-001, UN-005
- **Priority:** High

### NFR-004
- **Requirement:** The system shall sample and process thermostat readings at a minimum rate of 1 Hz for each active thermostat in the simulated environment.
- **Source:** UN-001, UN-002
- **Priority:** High

### NFR-005
- **Requirement:** The system shall support thermostat sensing and reporting only within the specified operating range of 14°F to 104°F (-10°C to 40°C), and shall reject or flag any simulated reading outside that range as invalid.
- **Source:** UN-001, UN-002
- **Priority:** High

### NFR-006
- **Requirement:** The system shall sample and process humidistat readings at a minimum rate of 1 Hz for each active humidistat in the simulated environment.
- **Source:** UN-001, UN-002
- **Priority:** High

### NFR-007
- **Requirement:** The system shall apply any user-requested thermostat, humidistat, or power-switch control command within 2 seconds of request submission for 95% of commands under normal prototype operating conditions.
- **Source:** UN-002
- **Priority:** High

### NFR-008
- **Requirement:** The system shall transmit and receive gateway-to-device wireless communications over a simulated indoor RF range of up to 1000 feet without loss of functional connectivity in the modeled environment.
- **Source:** UN-001, UN-002
- **Priority:** High

### NFR-009
- **Requirement:** The system shall support at least 4 schedule periods per day for each schedulable thermostat, humidistat, and programmable power switch within daily presets and monthly planning functions.
- **Source:** UN-003
- **Priority:** Medium

### NFR-010
- **Requirement:** The system shall save or update a daily preset or monthly planner entry within 2 seconds of user submission for 95% of requests.
- **Source:** UN-003
- **Priority:** Medium

### NFR-011
- **Requirement:** The system shall generate historical reports containing averages, minimums, maximums, and downtime logs for a selected date range within 5 seconds for 95% of report requests covering up to 31 days of data.
- **Source:** UN-004
- **Priority:** Medium

### NFR-012
- **Requirement:** The system shall retain historical monitoring, event, and downtime data for at least 90 days in the prototype data store to support historical reporting.
- **Source:** UN-004, UN-009
- **Priority:** Medium

### NFR-013
- **Requirement:** The system shall require successful username-and-password authentication before granting access to any monitoring, control, planning, reporting, or configuration function.
- **Source:** UN-005
- **Priority:** High

### NFR-014
- **Requirement:** The system shall enforce role-based authorization such that General Users can access monitoring, control, planning, and reporting functions only, while Master Users and DH Technicians shall additionally be permitted to manage user accounts, change system parameters, and start or stop system operation.
- **Source:** UN-005, UN-006, UN-007, UN-008
- **Priority:** High

### NFR-015
- **Requirement:** The system shall encrypt all authenticated web sessions and all transmitted credentials using TLS 1.2 or higher.
- **Source:** UN-005
- **Priority:** High

### NFR-016
- **Requirement:** The system shall automatically terminate an authenticated session after 15 minutes of user inactivity.
- **Source:** UN-005
- **Priority:** Medium

### NFR-017
- **Requirement:** The system shall record each successful and failed login attempt, logout event, account-management action, configuration change, and system start or stop event with user identifier and timestamp.
- **Source:** UN-005, UN-006, UN-007, UN-008
- **Priority:** Medium

### NFR-018
- **Requirement:** The system shall present web interface workflows for login, monitoring, control, planning, and reporting that can be completed using standard browser interactions without requiring technical product knowledge beyond basic web usage.
- **Source:** UN-001, UN-003, UN-004, UN-005
- **Priority:** Medium

### NFR-019
- **Requirement:** The system shall restrict account creation, account modification, default-parameter changes, and other configuration actions to Master Users and DH Technicians only.
- **Source:** UN-006, UN-007
- **Priority:** High

### NFR-020
- **Requirement:** The system shall make administrator-requested configuration changes effective within 5 seconds of successful submission for 95% of requests.
- **Source:** UN-006, UN-007
- **Priority:** Medium

### NFR-021
- **Requirement:** The system shall permit only Master Users and DH Technicians to start or stop DigitalHome system operation, and shall complete the requested state transition within 10 seconds for 95% of requests.
- **Source:** UN-008
- **Priority:** Medium

### NFR-022
- **Requirement:** The system shall perform an automated backup of user account information, user plans, and the home database at least once every 24 hours.
- **Source:** UN-009
- **Priority:** High

### NFR-023
- **Requirement:** The system shall restore the most recent successful backup of user account information, user plans, and the home database within 4 hours of a recovery request.
- **Source:** UN-009
- **Priority:** Medium

### NFR-024
- **Requirement:** The system shall achieve at least 99.0% availability over each 30-day period excluding planned maintenance windows not exceeding 4 hours per month.
- **Source:** UN-001, UN-002, UN-009
- **Priority:** Medium

### NFR-025
- **Requirement:** The system shall detect an active door or window contact sensor breach and activate the associated sound and light alarm indication within 2 seconds of the triggering event while the security monitoring function is active.
- **Source:** UN-001, UN-002
- **Priority:** High

### NFR-026
- **Requirement:** The system shall enter a fail-safe state on loss of communication between the gateway and a monitored security sensor for more than 10 seconds by marking the sensor status as unavailable and logging the communication failure event.
- **Source:** UN-001, UN-009
- **Priority:** High

### NFR-027
- **Requirement:** The system shall preserve the last confirmed appliance power state across server or application restart and, if the prior state cannot be verified during recovery, shall reset the affected programmable power switch to OFF by default.
- **Source:** UN-002, UN-009
- **Priority:** High

### NFR-028
- **Requirement:** The system shall support programmable power switches only for simulated small-appliance and lighting loads up to 120 volts and 15 amperes per switch.
- **Source:** UN-002
- **Priority:** Medium

### NFR-029
- **Requirement:** The system shall execute all thermostat, humidistat, contact sensor, alarm, and programmable power switch behaviors in a simulated environment that adheres to realistic home physical properties and device constraints, with no dependency on actual installed household hardware.
- **Source:** UN-001, UN-002, UN-009
- **Priority:** High

### NFR-030
- **Requirement:** The system shall achieve a mean time between service-affecting failures of at least 720 operating hours in the prototype test environment.
- **Source:** UN-009
- **Priority:** Medium