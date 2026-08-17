# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a DigitalHome user, I want to log in to the system and see only the functions allowed for my role so that I can use the system securely and appropriately.

- **Source:** FR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Successful login for authorized user**
  - **Given:** A valid DigitalHome user account exists
  - **When:** The user submits correct login credentials
  - **Then:** The system grants access and displays the appropriate role-based interface
- **Scenario: Invalid login attempt**
  - **Given:** The login page is available
  - **When:** The user submits invalid credentials
  - **Then:** The system denies access and displays an authentication error message

### US-002
**User Story:** As a General User, I want to see the current status of my home devices and connectivity in one dashboard so that I can quickly understand the condition of the home.

- **Source:** FR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Dashboard with active devices**
  - **Given:** The system has configured simulated devices
  - **When:** The user opens the home status dashboard
  - **Then:** The system displays current temperature, humidity, security, power, and connectivity status values
- **Scenario: Dashboard when devices are unavailable**
  - **Given:** One or more simulated devices or the gateway are unavailable
  - **When:** The user refreshes the dashboard
  - **Then:** The system marks the affected items as unavailable and does not show stale control confirmation as current status

### US-003
**User Story:** As a General User, I want to adjust thermostat set points from the web interface so that I can maintain a comfortable temperature in the home.

- **Source:** FR-003
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Valid temperature set point update**
  - **Given:** A thermostat is configured and reachable
  - **When:** The user submits a valid temperature set point
  - **Then:** The system stores the new set point and displays it as the active target temperature
- **Scenario: Invalid temperature set point**
  - **Given:** A thermostat is configured
  - **When:** The user submits a set point outside the supported range
  - **Then:** The system rejects the value and displays a validation message

### US-004
**User Story:** As a General User, I want to adjust humidity set points from the web interface so that I can maintain comfortable humidity levels in the home.

- **Source:** FR-004
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Valid humidity set point update**
  - **Given:** A humidistat is configured and reachable
  - **When:** The user submits a valid humidity set point
  - **Then:** The system stores the new set point and displays it as the active target humidity
- **Scenario: Humidity device unavailable**
  - **Given:** A humidistat is unavailable or not configured
  - **When:** The user opens humidity controls
  - **Then:** The system indicates that humidity control cannot be performed

### US-005
**User Story:** As a General User, I want to see security sensor status and alarm state so that I can detect a possible breach in the home.

- **Source:** FR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Breach detected on monitored entry**
  - **Given:** A magnetic contact is active for a monitored door or window
  - **When:** The contact indicates a breach condition
  - **Then:** The system displays the breach and shows the associated alarm as active
- **Scenario: No breach present**
  - **Given:** All monitored contacts are secure
  - **When:** The user views the security panel
  - **Then:** The system displays each monitored contact as normal and the alarm as inactive

### US-006
**User Story:** As a General User, I want to turn appliances or lighting units on or off remotely so that I can manage convenience, safety, and energy use.

- **Source:** FR-006
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Change appliance power state successfully**
  - **Given:** A power switch is configured and reachable
  - **When:** The user sends a command to change the device state
  - **Then:** The system updates and displays the new power state for that appliance or light
- **Scenario: Power control unavailable**
  - **Given:** A power switch is offline or unavailable
  - **When:** The user attempts to change the state
  - **Then:** The system does not apply the change and displays an availability error

### US-007
**User Story:** As a Master User, I want to manage user accounts and default settings so that the household system remains correctly configured.

- **Source:** FR-007
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Create a new user account**
  - **Given:** The Master User is logged in with administrative rights
  - **When:** The user submits valid new account details
  - **Then:** The system creates the account and makes it available for future login
- **Scenario: Unauthorized user attempts administration**
  - **Given:** A General User is logged in
  - **When:** The General User attempts to access account or default settings management
  - **Then:** The system denies access to the administrative function

### US-008
**User Story:** As a DH Technician, I want to start, stop, and maintain the configured DigitalHome system so that I can support setup, maintenance, and troubleshooting.

- **Source:** FR-008
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Start system operation**
  - **Given:** The DH Technician is authenticated and the system is stopped
  - **When:** The technician issues a start command
  - **Then:** The system enters the running state and displays that operational state in the administrative interface
- **Scenario: Stop system operation**
  - **Given:** The DH Technician is authenticated and the system is running
  - **When:** The technician issues a stop command
  - **Then:** The system enters the stopped state and prevents normal control actions that require active operation

### US-009
**User Story:** As a Master User or DH Technician, I want system data to be stored and backed up so that configuration and operational information can be retained for continued use and recovery.

- **Source:** FR-009
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Backup completes successfully**
  - **Given:** The user has administrative rights and data exists in the home system
  - **When:** A backup is initiated
  - **Then:** The system records that backup support has completed and preserves user accounts, plans, and home operational data
- **Scenario: Backup failure occurs**
  - **Given:** A backup destination or service is unavailable
  - **When:** A backup is initiated
  - **Then:** The system reports the failure and leaves existing committed data unchanged
