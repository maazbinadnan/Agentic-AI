## Business Analysis & Requirements Specification

### 4. Agile User Stories & Backlog

---

**US-001: Access DigitalHome via Web Interface**

- **User Story:** As a general user, I want to access DigitalHome through a web interface so that I can monitor and control my home remotely.
- **Source:** UN-001, UN-005, FR-001
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Successful login and page access
    - **Given** a registered user account exists
    - **When** the user navigates to the DigitalHome web page and submits valid login credentials
    - **Then** the system grants access to the available DigitalHome pages for that user role
  - **Scenario 2:** Logout from the system
    - **Given** the user is logged into DigitalHome
    - **When** the user selects logout
    - **Then** the system ends the session and returns the user to a logged-out state

---

**US-002: Monitor and Control Home Environment**

- **User Story:** As a general user, I want to monitor and control supported home devices so that I can manage the environment in my home.
- **Source:** UN-001, FR-002
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** View supported home management functions
    - **Given** the user is authenticated as a general user
    - **When** the user opens the home management page
    - **Then** the system displays available monitoring and control functions for temperature, humidity, security, appliances, and lighting within the prototype scope
  - **Scenario 2:** Reject unauthorized administration action
    - **Given** the user is authenticated as a general user
    - **When** the user attempts to access a configuration or system operation function reserved for higher-privilege roles
    - **Then** the system denies the action

---

**US-003: Administer Users and Default Settings**

- **User Story:** As a master user or DH technician, I want to manage user accounts and configuration settings so that the system is correctly configured for home operation.
- **Source:** UN-002, UN-003, UN-010, FR-003
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Create or update configuration information
    - **Given** the user is authenticated with master user or technician privileges
    - **When** the user submits a new user account or updated default parameter settings
    - **Then** the system saves the requested configuration change
  - **Scenario 2:** Block unauthorized configuration changes
    - **Given** the user is authenticated as a general user
    - **When** the user attempts to create a user account or change default parameter settings
    - **Then** the system denies the request

---

**US-004: Start or Stop DigitalHome Operation**

- **User Story:** As a master user or DH technician, I want to start or stop the DigitalHome system so that I can control system operation during setup, maintenance, or administration.
- **Source:** UN-002, UN-003, FR-004
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Start system operation
    - **Given** the user is authenticated as a master user or DH technician and the system is stopped
    - **When** the user issues a start command
    - **Then** the system enters an operational state
  - **Scenario 2:** Stop system operation
    - **Given** the user is authenticated as a master user or DH technician and the system is operational
    - **When** the user issues a stop command
    - **Then** the system enters a stopped state

---

**US-005: Use Home Web Server Services**

- **User Story:** As an administrator, I want the home web server to host DigitalHome services so that users and administrators can interact with devices, data, accounts, and backups.
- **Source:** UN-009, UN-010, FR-005
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Store and maintain home information
    - **Given** the home web server is operational
    - **When** an authorized user or administrator stores plans, data, or account information
    - **Then** the system persists the information on the home web server
  - **Scenario 2:** Perform backup
    - **Given** account information, user plans, and home database records exist
    - **When** an authorized administrator initiates backup functionality
    - **Then** the system creates a backup of those records

---

**US-006: Communicate with Home Devices Through Gateway**

- **User Story:** As a system operator, I want the server to communicate with home devices through the gateway so that commands and status data can move between the user interface and device layer.
- **Source:** UN-009, FR-006
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Send device command through gateway
    - **Given** the gateway is connected to broadband and paired with simulated devices
    - **When** the server sends a supported control command
    - **Then** the gateway transmits the command to the target device through the RF module
  - **Scenario 2:** Receive device status through gateway
    - **Given** a simulated device produces status information
    - **When** the gateway receives the wireless transmission
    - **Then** the server receives the device status for presentation or processing

---

**US-007: Monitor and Set Temperature**

- **User Story:** As a general user, I want to view current temperature and set a desired temperature so that heating or cooling can regulate my home to the target value.
- **Source:** UN-006, FR-007
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** View current temperature
    - **Given** a thermostat is available in the system
    - **When** the user opens the temperature page
    - **Then** the system displays the current temperature reading reported by the thermostat
  - **Scenario 2:** Set target temperature
    - **Given** the user is authorized to control temperature
    - **When** the user submits a new temperature set point within the supported range
    - **Then** the system stores the set point and uses it to control heating or cooling devices on or off as needed

---

**US-008: Monitor and Set Humidity**

- **User Story:** As a general user, I want to view current humidity and set a desired humidity so that humidification equipment can regulate my home to the target value.
- **Source:** UN-006, FR-008
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** View current humidity
    - **Given** a humidistat is available in the system
    - **When** the user opens the humidity page
    - **Then** the system displays the current humidity reading reported by the humidistat
  - **Scenario 2:** Set target humidity
    - **Given** the user is authorized to control humidity
    - **When** the user submits a new humidity set point
    - **Then** the system stores the set point and uses it to control humidifiers and dehumidifiers

---

**US-009: Monitor Entry Points and Trigger Alarm**

- **User Story:** As a general user, I want the system to monitor doors and windows and trigger alarms on breaches so that I can be alerted to possible intrusions.
- **Source:** UN-007, FR-009
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Detect entry through active magnetic contact
    - **Given** a magnetic alarm contact switch is active on a door or window
    - **When** the contact indicates entry
    - **Then** the system records a security breach condition
  - **Scenario 2:** Activate sound and light alarms
    - **Given** a security breach condition has been detected from a magnetic contact
    - **When** alarm activation rules are applied
    - **Then** the system activates the configured security sound and light alarms

---

**US-010: Monitor and Switch Appliance or Lighting Power**

- **User Story:** As a general user, I want to view and change the power state of appliances and lighting so that I can manage energy use and household convenience.
- **Source:** UN-008, FR-010
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** View current power state
    - **Given** a programmable power switch is connected to an appliance or lighting unit
    - **When** the user opens the power control page
    - **Then** the system displays whether the connected item is currently on or off
  - **Scenario 2:** Change power state
    - **Given** the user is authorized to control the connected item
    - **When** the user issues an on or off command
    - **Then** the system changes the state of the appliance or lighting unit accordingly

---

**US-011: Enforce Role-Based Access**

- **User Story:** As a system owner, I want user capabilities to be restricted by role so that only authorized users can perform configuration and operational administration actions.
- **Source:** UN-001, UN-002, UN-003, FR-011
- **Priority:** Must Have
- **Acceptance Criteria:**
  - **Scenario 1:** Permit authorized privileged action
    - **Given** the user is authenticated as a master user or DH technician
    - **When** the user attempts a permitted configuration or system operation action
    - **Then** the system allows the action according to the role’s privileges
  - **Scenario 2:** Deny unauthorized privileged action
    - **Given** the user is authenticated as a general user
    - **When** the user attempts a privileged configuration or system operation action
    - **Then** the system denies the action