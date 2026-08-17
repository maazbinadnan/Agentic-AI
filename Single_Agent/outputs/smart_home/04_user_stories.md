# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a General User, I want to monitor and control the temperature, humidity, and power state of devices so that I can manage my home environment remotely.
- **Source:** FR-001
- **Priority:** High
**Acceptance Criteria:**
- **Scenario: Monitor and control devices**
  - **Given:** I am logged in and viewing the dashboard
  - **When:** I select a device and adjust its settings
  - **Then:** The device state updates and the new value is displayed
- **Scenario: Device offline**
  - **Given:** I am logged in and a device is offline
  - **When:** I attempt to control the device
  - **Then:** An error message is displayed

### US-002
**User Story:** As any user, I want to securely log in and out of the system so that my account and home data are protected.
- **Source:** FR-002
- **Priority:** High
**Acceptance Criteria:**
- **Scenario: Successful login**
  - **Given:** I am on the login page
  - **When:** I enter valid credentials
  - **Then:** I am granted access to the system
- **Scenario: Failed login**
  - **Given:** I am on the login page
  - **When:** I enter invalid credentials
  - **Then:** An error message is displayed

### US-003
**User Story:** As any user, I want to receive feedback and error messages when device actions fail or the system is offline so that I am aware of system status.
- **Source:** FR-003
- **Priority:** High
**Acceptance Criteria:**
- **Scenario: Device action fails**
  - **Given:** I am controlling a device
  - **When:** The action fails
  - **Then:** An error message is displayed
- **Scenario: System offline**
  - **Given:** The system is offline
  - **When:** I attempt any action
  - **Then:** A system offline message is displayed

### US-004
**User Story:** As a Master User or DH Technician, I want to manage user accounts so that I can control who has access to the system.
- **Source:** FR-004
- **Priority:** Medium
**Acceptance Criteria:**
- **Scenario: Add user**
  - **Given:** I am logged in as a Master User or Technician
  - **When:** I add a new user
  - **Then:** The user appears in the user list
- **Scenario: Remove user**
  - **Given:** I am logged in as a Master User or Technician
  - **When:** I remove a user
  - **Then:** The user is deleted from the system

### US-005
**User Story:** As a Master User or DH Technician, I want to configure system parameters so that the system operates according to my preferences.
- **Source:** FR-005
- **Priority:** Medium
**Acceptance Criteria:**
- **Scenario: Change parameter**
  - **Given:** I am logged in as a Master User or Technician
  - **When:** I change a system parameter
  - **Then:** The new parameter value is saved and applied

### US-006
**User Story:** As a Master User or DH Technician, I want to back up and restore user and system data so that I can prevent data loss.
- **Source:** FR-006
- **Priority:** Medium
**Acceptance Criteria:**
- **Scenario: Backup data**
  - **Given:** I am logged in as a Master User or Technician
  - **When:** I initiate a backup
  - **Then:** The system confirms the backup is complete
- **Scenario: Restore data**
  - **Given:** I am logged in as a Master User or Technician
  - **When:** I initiate a restore
  - **Then:** The system restores data and confirms success
