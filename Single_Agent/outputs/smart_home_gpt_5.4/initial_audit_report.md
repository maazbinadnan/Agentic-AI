# Initial Elicitation & Scope Audit

## Source Overview
The provided DigitalHome (DH) requirements describe a prototype smart home management system intended for business validation rather than a full commercial release. The system is constrained to a simulated environment and focuses on web-based monitoring and control of home environmental and security devices.

## In-Scope Capabilities
- Web-based access to the DH system through a personal web page on a DH web server or local home server.
- Monitoring and control of:
  - Temperature via digital programmable thermostats
  - Humidity via digital programmable humidistats
  - Security via magnetic alarm contact switches and alarms
  - Power to small appliances and lighting units via digital programmable power switches
- Home web server support for:
  - Device interaction and control
  - Storage of plans and data
  - User account establishment and maintenance
  - Backup of user accounts, plans, and home database
- Gateway-based communication between server and simulated devices.
- Role-based access for General User, Master User, and DH Technician.
- System operation controls for privileged roles, including start/stop and configuration.

## Explicit User Roles
### General User
- Monitors and controls the home environment.
- Uses common web functionality such as login, logout, browsing, and submission of requests.

### Master User
- Has General User capabilities.
- Can change system configuration.
- Can add user accounts and change default parameter settings.
- Has the same rights as the DH Technician.

### DH Technician
- Sets up and maintains DH configuration.
- Has advanced rights to establish accounts, set parameters, and start/stop system operation.

## Core Domain Entities
- User account
- Home web server
- Local home server
- Wireless gateway device
- Thermostat
- Humidistat
- Magnetic contact sensor
- Security sound/light alarm
- Power switch
- Appliance or lighting unit
- Home plans and operational data
- Backup dataset
- Simulated sensor/controller instance

## Architectural & Operational Constraints
- Prototype must be completed within 12 months.
- Team size is five engineers plus management support.
- Development must follow the company-defined process.
- Use widely accepted and available technologies and standards where possible.
- Minimize system element costs and document cost comparisons in the final project report.
- All testing and operation for the prototype occur in a realistic simulated environment; no physical home deployment is included.
- ISP/broadband connectivity is assumed for operation.
- Gateway supports wireless communication with indoor range up to 1000 feet.

## Implicit Requirements Identified
- Authentication and session management are required because users log in and have differentiated rights.
- Authorization and role-based access control are required because General Users, Master Users, and Technicians have different permissions.
- A dashboard or status page is required to support environmental and security monitoring.
- Device state visibility is required for all controllable/observable devices.
- Validation rules are required for setpoint and command inputs.
- Error and degraded-state handling is required for gateway, server, and simulated device communication failures.
- Administrative tooling is required for account management, parameter management, and system operation control.
- Data persistence is required for plans, account information, and backups.
- Auditability would be beneficial for privileged changes, though not explicitly stated.

## Out-of-Scope / Not Explicitly Supported
- Real physical devices and actual home deployment.
- Mobile-native applications.
- Advanced entertainment and communications features mentioned in the vision statement but excluded from prototype scope.
- Detailed automation rules, scheduling, or scene management.
- Third-party smart-home ecosystem integrations.
- Detailed alert notification channels such as SMS or email.

## Key Gaps / Ambiguities
### 1. Authentication Detail
- The roles imply login and authorization, but password policy, session timeout, recovery, and account lockout behavior are unspecified.

### 2. Security Workflow Detail
- The requirements mention monitoring entry and activating alarms on a security breach, but do not define arming modes, bypass behavior, alarm reset, or event history requirements.

### 3. Device Configuration Model
- The document does not specify whether users can name devices, assign rooms/zones, or remove failed devices.

### 4. Environmental Control Logic
- Thermostat and humidistat setpoint control are described, but polling frequency, tolerance bands, and conflict resolution are unspecified.

### 5. Backup Characteristics
- Backup is required, but backup schedules, restore process, retention, and failure handling are not specified.

### 6. Lighting Treatment
- Lighting units are named in scope, but no distinct lighting controller behavior is given; they are assumed to be controlled through digital programmable power switches.

### 7. Operational Monitoring
- Start/stop operation is explicitly available to Technician/Master User, but the operational states and consequences for active controls during shutdown are not specified.

## BA Recommendations
- Treat authentication, authorization, and role-based permissions as mandatory foundational capabilities for the prototype.
- Consolidate lighting control under power switch management unless stakeholders specify distinct lighting semantics.
- Represent devices in a room/zone-oriented dashboard to simplify monitoring and control for non-technical users.
- Include visible connectivity and simulation status indicators to support prototype evaluation.
- Add explicit administrative screens for users, defaults, backups, and system operation status.
- Capture all identified ambiguities as stakeholder questions before implementation begins.

## Proposed Deliverable Structure
- `01_user_needs.md`: high-level consolidated user needs.
- `02_functional_requirements.md`: formal, testable system behaviors.
- `03_non_functional_requirements.md`: measurable quality and constraint requirements.
- `04_user_stories.md`: developer-ready user stories and Gherkin acceptance criteria.
- `05_summary_and_traceability.md`: full traceability, gaps, and metrics.
- `html/*.html`: responsive standalone UI mockups for major screens.
- `07_ui_mockups_and_interaction_design.md`: mapping of stories to screens and design decisions.
- `INDEX.md`: executive summary and manifest.
