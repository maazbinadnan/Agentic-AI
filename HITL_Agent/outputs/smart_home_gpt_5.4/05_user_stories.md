# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As an authenticated user, I want to sign in with my username and password so that I can securely access DigitalHome functions.

- **Source:** FR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Successful login with valid credentials**
  - **Given:** the user is on the DigitalHome login page and has a valid username and password
  - **When:** the user submits the correct credentials
  - **Then:** the system shall authenticate the user and grant access to DigitalHome functions permitted for that user role
- **Scenario: Failed login with invalid credentials**
  - **Given:** the user is on the DigitalHome login page
  - **When:** the user submits an invalid username or password
  - **Then:** the system shall deny access and keep protected DigitalHome functions unavailable

### US-002
**User Story:** As a DigitalHome user, I want the system to enforce my role permissions so that I can access only the functions appropriate to my responsibilities.

- **Source:** FR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: General User accesses permitted monitoring and control functions**
  - **Given:** a General User is authenticated in the system
  - **When:** the user opens monitoring or control pages
  - **Then:** the system shall allow access to home monitoring and control functions
- **Scenario: General User attempts to access restricted administrative functions**
  - **Given:** a General User is authenticated in the system
  - **When:** the user attempts to access account management, configuration, or system start or stop functions
  - **Then:** the system shall deny access to those restricted functions

### US-003
**User Story:** As an authenticated user, I want to log out of the web interface so that my access to protected DigitalHome functions is terminated.

- **Source:** FR-003
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Successful logout**
  - **Given:** an authenticated user is using the DigitalHome web interface
  - **When:** the user selects the logout action
  - **Then:** the system shall end the session and prevent further access to protected functions
- **Scenario: Access attempt after logout**
  - **Given:** a user has logged out from the DigitalHome web interface
  - **When:** the user attempts to open a protected page without signing in again
  - **Then:** the system shall require authentication before granting access

### US-004
**User Story:** As an authenticated user, I want the home web server to store my plans, data, accounts, and backups so that DigitalHome information is available for ongoing use and recovery.

- **Source:** FR-004
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Web server supports interaction and data storage**
  - **Given:** the DigitalHome home web server is operational
  - **When:** an authenticated user interacts with devices or saves plans and account data
  - **Then:** the system shall store the relevant plans, operational data, and user account records on the home web server
- **Scenario: Backup support is available for stored DigitalHome information**
  - **Given:** user account information, user plans, and home database records exist on the home web server
  - **When:** backup support is invoked by the system
  - **Then:** the system shall create backup data for those stored records

### US-005
**User Story:** As a DigitalHome user, I want the system to communicate with home devices through the gateway so that web-based monitoring and control can reach sensors and controllers in the home.

- **Source:** FR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Successful communication through gateway and RF link**
  - **Given:** the home web server, gateway, and simulated DigitalHome devices are connected and available
  - **When:** the system sends or receives device data
  - **Then:** the gateway shall exchange communications between the web server and the simulated sensors and controllers
- **Scenario: Broadband connectivity is unavailable**
  - **Given:** the DigitalHome system depends on broadband Internet connectivity for remote communication
  - **When:** the broadband connection is unavailable
  - **Then:** the system shall be unable to complete remote communication with the affected devices or users

### US-006
**User Story:** As a General User, I want to view the current status of my home environment and device states so that I can understand current conditions in my home.

- **Source:** FR-006
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: View current monitored home status**
  - **Given:** a General User is authenticated in the web interface
  - **When:** the user opens the home monitoring page
  - **Then:** the system shall display current temperature, humidity, door and window contact states, alarm status, and appliance or lighting power states
- **Scenario: Some monitored device data is unavailable**
  - **Given:** a General User is authenticated and one or more monitored devices have no current status available
  - **When:** the user opens the home monitoring page
  - **Then:** the system shall display the available status information and indicate unavailable monitored data where applicable

### US-007
**User Story:** As a General User, I want to monitor temperature and set a thermostat target so that the system can regulate home temperature toward my preferred level.

- **Source:** FR-007
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: View current temperature and update thermostat set point**
  - **Given:** a thermostat is available in the simulated home and a General User is authenticated
  - **When:** the user views the thermostat and submits a temperature set point within the supported sensing range
  - **Then:** the system shall display the current temperature, store the requested set point, and switch heating or cooling outputs on or off as needed to regulate toward that set point
- **Scenario: Temperature reading falls outside supported sensing range**
  - **Given:** the thermostat produces a simulated reading outside 14°F to 104°F (-10°C to 40°C)
  - **When:** the system receives the out-of-range reading
  - **Then:** the system shall not use that reading as a valid thermostat reading for normal regulation

### US-008
**User Story:** As a General User, I want to monitor humidity and set a humidistat target so that the system can regulate home humidity toward my preferred level.

- **Source:** FR-008
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: View current humidity and update humidistat set point**
  - **Given:** a humidistat is available in the simulated home and a General User is authenticated
  - **When:** the user views the humidistat and submits a humidity set point
  - **Then:** the system shall display the current humidity, store the requested set point, and switch humidifier or dehumidifier outputs as needed to regulate toward that set point
- **Scenario: Humidity control device is unavailable**
  - **Given:** a humidistat reading is available but the related humidifier or dehumidifier control output is unavailable
  - **When:** the user submits a humidity set point
  - **Then:** the system shall retain the requested set point and indicate that active humidity regulation cannot be completed until the control output is available

### US-009
**User Story:** As a General User, I want to monitor and change appliance or lighting power states so that I can manage energy use and household convenience.

- **Source:** FR-009
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: View and change a power switch state**
  - **Given:** a programmable power switch for a supported appliance or lighting unit is available and a General User is authenticated
  - **When:** the user views the current state and sends an on or off command
  - **Then:** the system shall display the current state and change the power switch state to the requested on or off state
- **Scenario: Command targets an unavailable power switch**
  - **Given:** a programmable power switch is not currently reachable in the simulated environment
  - **When:** the user sends an on or off command
  - **Then:** the system shall not report a successful state change unless the switch state is actually updated

### US-010
**User Story:** As a General User, I want to see whether doors and windows are in a normal or breach state so that I can monitor entry security in my home.

- **Source:** FR-010
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Display normal and breach states from active contact sensors**
  - **Given:** active magnetic contact sensors are configured for doors or windows
  - **When:** the system receives sensor states
  - **Then:** the system shall display whether each active contact is in a normal closed state or an entry breach state
- **Scenario: Contact sensor is inactive**
  - **Given:** a door or window has a magnetic contact sensor that is not active
  - **When:** the system evaluates entry status for that sensor
  - **Then:** the system shall not treat that inactive sensor as an active breach source

### US-011
**User Story:** As a General User, I want security alarms to activate when a breach is detected so that I am informed of a possible security issue.

- **Source:** FR-011
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Activate sound and light alarm on detected breach**
  - **Given:** an active magnetic contact sensor is being monitored and the related alarm capability is configured
  - **When:** the system detects a security breach from that sensor
  - **Then:** the system shall activate the configured sound alarm and light alarm and display the resulting alarm state in the web interface
- **Scenario: No breach is detected**
  - **Given:** active magnetic contact sensors are being monitored and no breach event has occurred
  - **When:** the system evaluates alarm conditions
  - **Then:** the system shall not activate the breach alarm state

### US-012
**User Story:** As a General User, I want to create and maintain monthly plans for supported devices so that my home behavior can be scheduled over time.

- **Source:** FR-012
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Create or update a monthly plan**
  - **Given:** a General User is authenticated and supported environmental or power-managed devices exist
  - **When:** the user creates or updates a monthly plan
  - **Then:** the system shall store the monthly plan for later viewing and execution
- **Scenario: View an existing monthly plan**
  - **Given:** a stored monthly plan exists for the authenticated user
  - **When:** the user opens the monthly planning view
  - **Then:** the system shall display the saved monthly plan details

### US-013
**User Story:** As a General User, I want to create and maintain daily presets for supported devices so that recurring daily settings can be applied automatically.

- **Source:** FR-013
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Create or update a daily preset**
  - **Given:** a General User is authenticated and schedulable thermostat, humidistat, or power-switch devices exist
  - **When:** the user creates or updates a daily preset with planned set points or power states
  - **Then:** the system shall store the daily preset for later viewing and execution
- **Scenario: View an existing daily preset**
  - **Given:** a stored daily preset exists for the authenticated user
  - **When:** the user opens the daily preset view
  - **Then:** the system shall display the saved daily preset details

### US-014
**User Story:** As a General User, I want the system to execute saved plans and presets automatically so that scheduled home settings take effect at the planned times.

- **Source:** FR-014
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Apply scheduled settings at the planned time**
  - **Given:** stored monthly plans or daily presets exist for supported devices
  - **When:** a planned execution time is reached
  - **Then:** the system shall apply the scheduled thermostat set point, humidistat set point, or power state to the targeted device
- **Scenario: Scheduled target device is unavailable at execution time**
  - **Given:** a stored plan or preset is due for execution and the targeted device is unavailable
  - **When:** the execution time is reached
  - **Then:** the system shall not falsely indicate that the scheduled device change was successfully applied

### US-015
**User Story:** As a General User, I want to review historical reports of home operations so that I can understand trends, extremes, and downtime events.

- **Source:** FR-015
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: View historical report data**
  - **Given:** historical operational data exists for supported monitored or controlled devices
  - **When:** the user requests a historical report through the web interface
  - **Then:** the system shall provide report results that include averages, minimum values, maximum values, and downtime logs
- **Scenario: Request a report when no historical data exists for the selected scope**
  - **Given:** no historical operational data exists for the selected report scope
  - **When:** the user requests the historical report
  - **Then:** the system shall indicate that no report data is available for that request

### US-016
**User Story:** As a Master User or DH Technician, I want to manage DigitalHome user accounts so that authorized household users can access the system appropriately.

- **Source:** FR-016
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Create or update a user account**
  - **Given:** a Master User or DH Technician is authenticated in the web interface
  - **When:** the user creates or updates a DigitalHome user account
  - **Then:** the system shall save the account information and make the maintained account available according to its assigned role
- **Scenario: Unauthorized user attempts account management**
  - **Given:** a General User is authenticated in the web interface
  - **When:** the user attempts to create or modify a DigitalHome user account
  - **Then:** the system shall deny the account-management action

### US-017
**User Story:** As a Master User or DH Technician, I want to configure system default parameters so that DigitalHome behavior can be adjusted for household needs.

- **Source:** FR-017
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Update system default parameters**
  - **Given:** a Master User or DH Technician is authenticated in the web interface
  - **When:** the user submits changes to system default parameters
  - **Then:** the system shall save the updated parameter settings
- **Scenario: Unauthorized user attempts parameter configuration**
  - **Given:** a General User is authenticated in the web interface
  - **When:** the user attempts to change system default parameters
  - **Then:** the system shall deny the configuration action

### US-018
**User Story:** As a Master User or DH Technician, I want to start or stop DigitalHome system operation so that I can control availability during maintenance or administrative activities.

- **Source:** FR-018
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Authorized user starts or stops system operation**
  - **Given:** a Master User or DH Technician is authenticated in the web interface
  - **When:** the user submits a start or stop operation command
  - **Then:** the system shall change DigitalHome system operation to the requested state
- **Scenario: Unauthorized user attempts to start or stop the system**
  - **Given:** a General User is authenticated in the web interface
  - **When:** the user attempts to start or stop DigitalHome system operation
  - **Then:** the system shall deny the requested action

### US-019
**User Story:** As an authorized user, I want the system to back up account, plan, and home database information so that DigitalHome data can be preserved for later recovery.

- **Source:** FR-019
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Successful backup of DigitalHome data**
  - **Given:** user account information, user plans, and home database records exist in the system
  - **When:** the system performs a backup
  - **Then:** the system shall preserve backup copies of those records for later recovery
- **Scenario: Backup is attempted when some source data is missing**
  - **Given:** one or more expected data categories are absent from the current system state
  - **When:** the system performs a backup
  - **Then:** the system shall back up the available data without inventing missing records

### US-020
**User Story:** As a DigitalHome user, I want all supported functions to operate against realistic simulated home devices and conditions so that the prototype can be used without physical hardware.

- **Source:** FR-020
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Use monitoring and control features in the simulated environment**
  - **Given:** the DigitalHome prototype is running in its simulated environment
  - **When:** users perform monitoring, control, planning, reporting, account-management, or backup actions
  - **Then:** the system shall execute those functions using simulated sensors, controllers, and home conditions
- **Scenario: Physical household hardware is not present**
  - **Given:** no actual physical home hardware is connected to the prototype
  - **When:** the system is used for supported DigitalHome functions
  - **Then:** the system shall continue to operate using the simulated environment rather than requiring physical devices

### US-021
**User Story:** As a DigitalHome user, I want remote access to depend on broadband Internet availability so that I can understand when remote communication is possible.

- **Source:** FR-021
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Remote access with broadband Internet available**
  - **Given:** broadband Internet service is available to the home web server and gateway
  - **When:** an authenticated user accesses the DigitalHome web interface remotely
  - **Then:** the system shall support remote communication between the user, home web server, and gateway
- **Scenario: Remote access without broadband Internet available**
  - **Given:** broadband Internet service is unavailable
  - **When:** an authenticated user attempts remote access to the DigitalHome web interface
  - **Then:** the system shall not be able to provide the expected remote communication path
