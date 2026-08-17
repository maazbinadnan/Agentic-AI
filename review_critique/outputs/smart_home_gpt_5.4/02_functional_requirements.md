## Business Analysis & Requirements Specification

### 2. Functional Requirements

---

**FR-001: Web-Based User Access**

- **Requirement:** The system shall provide a personal web page on the DigitalHome web server or local home server through which authorized users can log in, log out, browse available pages, and submit monitoring and control requests.
- **Source:** UN-001, UN-005
- **Priority:** Must Have

---

**FR-002: General Environment Monitoring and Control**

- **Requirement:** The system shall allow a general user to monitor and control supported home environmental devices for temperature, humidity, security status, and power to small appliances and lighting units.
- **Source:** UN-001
- **Priority:** Must Have

---

**FR-003: User Account and Configuration Administration**

- **Requirement:** The system shall allow a master user and DH technician to establish user accounts and change system configuration settings, including default parameter settings.
- **Source:** UN-002, UN-003, UN-010
- **Priority:** Must Have

---

**FR-004: System Operations Control**

- **Requirement:** The system shall allow a master user and DH technician to start and stop operation of the DigitalHome system.
- **Source:** UN-002, UN-003
- **Priority:** Must Have

---

**FR-005: Home Web Server Services**

- **Requirement:** The system shall support an individual home web server hosted on a home computer to provide interaction with DigitalHome elements, storage of plans and data, maintenance of user accounts, and backup of user account information, user plans, and the home database.
- **Source:** UN-009, UN-010
- **Priority:** Must Have

---

**FR-006: Gateway-to-Device Communications**

- **Requirement:** The system shall use a home gateway device to communicate between the DigitalHome web server and DigitalHome sensors and controllers through a broadband Internet connection and an RF module for wireless send/receive operations.
- **Source:** UN-009
- **Priority:** Must Have

---

**FR-007: Temperature Monitoring and Regulation**

- **Requirement:** The system shall monitor current temperature from digital programmable thermostats and allow authorized users to set a target temperature used to control heating or cooling devices on or off as needed to achieve the set point.
- **Source:** UN-006
- **Priority:** Must Have

---

**FR-008: Humidity Monitoring and Regulation**

- **Requirement:** The system shall monitor current humidity from digital programmable humidistats and allow authorized users to set a target humidity used to control humidifiers and dehumidifiers to achieve the set point.
- **Source:** UN-006
- **Priority:** Must Have

---

**FR-009: Entry Monitoring and Security Alarm Activation**

- **Requirement:** The system shall monitor magnetic alarm contact switches for door or window entry when active and shall activate security sound and light alarms when a security breach is detected from a magnetic contact.
- **Source:** UN-007
- **Priority:** Must Have

---

**FR-010: Appliance and Lighting Power Monitoring and Control**

- **Requirement:** The system shall monitor the current state of appliances and lighting units through digital programmable power switches and shall allow authorized users to change the state of a connected appliance or lighting unit from off to on or from on to off.
- **Source:** UN-008
- **Priority:** Must Have

---

**FR-011: Role-Based Privilege Enforcement**

- **Requirement:** The system shall enforce user privileges such that general users can use monitoring and control capabilities, and master users and DH technicians can perform configuration functions and start or stop system operation.
- **Source:** UN-001, UN-002, UN-003
- **Priority:** Must Have