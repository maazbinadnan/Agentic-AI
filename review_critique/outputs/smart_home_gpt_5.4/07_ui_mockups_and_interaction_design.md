# 07 UI Mockups and Interaction Design

## 1. Interaction Design Overview & Screen Architecture

This interaction design package translates the approved DigitalHome functional requirements and user stories into low-to-mid fidelity HTML/CSS mockups suitable for review. The prototype is web-based and focuses strictly on the functional scope defined in the source requirements: authentication, role-based access, environmental monitoring and control, security monitoring, power switching, administrative setup, system operations, home server support, and gateway-device communications.

### Design objectives
- Support simple web interactions for non-technical general users.
- Preserve privileged workflows for Master Users and DH Technicians.
- Make device status visible before action is taken.
- Show realistic edge cases including empty, offline, validation, and restricted states.
- Align every screen directly to a documented user story and functional requirement.

### Screen architecture
1. **Authentication & Access** (`auth_access_mockup.html`)
   - Login, logout, role-scoped navigation, unauthorized access handling.
2. **Environment Dashboard** (`environment_dashboard_mockup.html`)
   - General overview of supported home functions.
3. **Administration** (`admin_configuration_mockup.html`)
   - User account setup and default parameter configuration.
4. **System Operations & Server** (`system_operations_and_server_mockup.html`)
   - Start/stop operation, storage visibility, backup flow.
5. **Gateway Communications** (`gateway_communications_mockup.html`)
   - Server-to-gateway-to-device command and status path.
6. **Temperature Control** (`temperature_control_mockup.html`)
   - Thermostat reading and set point management.
7. **Humidity Control** (`humidity_control_mockup.html`)
   - Humidistat reading and set point management.
8. **Security Monitoring** (`security_monitoring_mockup.html`)
   - Entry point monitoring and alarm activation state.
9. **Appliance & Lighting Power** (`power_control_mockup.html`)
   - Power state visibility and on/off control.

All HTML mockups follow the required multi-state grid pattern and include:
- Primary/populated state
- Empty/unconfigured state
- Error/offline/restricted state

## 2. HTML Mockups to User Stories Mapping Table

| User Story | Functional Requirement(s) | Mockup File(s) | Coverage Summary |
|---|---|---|---|
| US-001 Access DigitalHome via Web Interface | FR-001, FR-011 | `auth_access_mockup.html` | Login, logout, authenticated landing access, restricted state |
| US-002 Monitor and Control Home Environment | FR-002 | `environment_dashboard_mockup.html` | Overview of supported home management areas and role-safe usage |
| US-003 Administer Users and Default Settings | FR-003, FR-011 | `admin_configuration_mockup.html` | Account creation, default settings, blocked unauthorized edits |
| US-004 Start or Stop DigitalHome Operation | FR-004, FR-011 | `system_operations_and_server_mockup.html` | Operational state toggling and protected admin control |
| US-005 Use Home Web Server Services | FR-005 | `system_operations_and_server_mockup.html` | Storage, account maintenance, and backup service views |
| US-006 Communicate with Home Devices Through Gateway | FR-006 | `gateway_communications_mockup.html` | Server-gateway-device path with active, idle, and offline states |
| US-007 Monitor and Set Temperature | FR-007 | `temperature_control_mockup.html` | Current reading, set point input, invalid submission state |
| US-008 Monitor and Set Humidity | FR-008 | `humidity_control_mockup.html` | Current humidity, set point input, offline/error handling |
| US-009 Monitor Entry Points and Trigger Alarm | FR-009 | `security_monitoring_mockup.html` | Contact state monitoring and breach-triggered alarm activation |
| US-010 Monitor and Switch Appliance or Lighting Power | FR-010 | `power_control_mockup.html` | On/off visibility and command failure handling |
| US-011 Enforce Role-Based Access | FR-011 | `auth_access_mockup.html`, `admin_configuration_mockup.html`, `system_operations_and_server_mockup.html`, `environment_dashboard_mockup.html` | Denied admin actions for general users and allowed privileged workflows |

## 3. Detailed Screen Specifications & Component Breakdowns

### 3.1 `auth_access_mockup.html`
**Mapped stories:** US-001, US-011  
**Primary components:**
- Product identity header
- Username and password fields
- Login and logout actions
- Role-aware navigation tiles
- Access-denied banner for restricted routes

**Interaction notes:**
- Successful login reveals only pages appropriate to the current role.
- Logout is presented as a clear session-ending action.
- Restricted state makes denial explicit rather than silently hiding failure.

### 3.2 `environment_dashboard_mockup.html`
**Mapped stories:** US-002, US-011  
**Primary components:**
- Home overview header
- Status cards for temperature, humidity, security, and power
- Summary feed of current conditions
- Empty setup state when no devices are configured
- Restricted admin attempt state

**Interaction notes:**
- This screen acts as the primary wayfinding layer for general users.
- High-level cards reduce cognitive load for users familiar only with basic web usage.

### 3.3 `admin_configuration_mockup.html`
**Mapped stories:** US-003, US-011  
**Primary components:**
- User account creation form
- Role selection control
- Default temperature/humidity settings form
- Existing accounts summary
- Permission-denied state

**Interaction notes:**
- Configuration actions are grouped into discrete sections to reduce accidental changes.
- Privilege messaging clarifies why an action is blocked.

### 3.4 `system_operations_and_server_mockup.html`
**Mapped stories:** US-004, US-005, US-011  
**Primary components:**
- Start/stop controls
- Backup action trigger
- Server services health list
- Stored records summary
- Stopped-state and backup-failure state

**Interaction notes:**
- Start/stop controls are intentionally prominent due to operational impact.
- Backup visibility reinforces trust in data persistence and prototype admin capability.

### 3.5 `gateway_communications_mockup.html`
**Mapped stories:** US-006  
**Primary components:**
- Server node
- Gateway node
- Simulated devices node
- Flow arrows to show transmission path
- Idle and offline warning states

**Interaction notes:**
- Since gateway communication is technical, the screen uses simple directional structure rather than dense diagnostics.
- Offline state highlights delivery failure without introducing unrequested engineering controls.

### 3.6 `temperature_control_mockup.html`
**Mapped stories:** US-007  
**Primary components:**
- Current temperature display
- Target set point field
- Save action
- Validation message for unsupported values

**Interaction notes:**
- Large current-reading emphasis supports quick environmental awareness.
- Validation state references the documented supported thermostat range.

### 3.7 `humidity_control_mockup.html`
**Mapped stories:** US-008  
**Primary components:**
- Current humidity display
- Target humidity field
- Save action
- Device offline error banner

**Interaction notes:**
- Similar structure to temperature management supports interaction consistency.
- Parallel design lowers learning effort for general users.

### 3.8 `security_monitoring_mockup.html`
**Mapped stories:** US-009  
**Primary components:**
- Entry point status cards
- Active/inactive monitoring states
- Alarm breach banner
- Alarm component status list
- Alert acknowledgment affordance

**Interaction notes:**
- Alarm state uses strong contrast and concise language for urgency.
- Breach flow reflects acceptance criteria: detect contact event first, then activate alarms.

### 3.9 `power_control_mockup.html`
**Mapped stories:** US-010  
**Primary components:**
- Device list with current power state
- On/off status pills
- No-device empty state
- Command failure state

**Interaction notes:**
- Simple device rows support rapid scanning.
- State chips make current on/off conditions clear at a glance.

## 4. Visual Hierarchy, WCAG 2.1 Accessibility, & UX Trade-offs

### Visual hierarchy
- Each mockup uses a strong top bar to identify feature and state.
- High-priority statuses are expressed with banners before detailed controls.
- Large numeric readings are used for thermostat and humidistat pages to foreground essential sensor information.
- Grouped cards and forms reduce fragmentation and help users understand task boundaries.

### Accessibility considerations
- Semantic text hierarchy is preserved with clear headings and labels.
- Color is paired with text messaging so meaning is not conveyed by color alone.
- Inputs are large enough for basic pointer interaction and keyboard focus styling can be added during implementation.
- Error banners use plain language and direct remediation cues.
- The responsive grid layout supports desktop review and narrow viewport adaptation.

### UX trade-offs
- The mockups are intentionally low-to-mid fidelity to emphasize structure and requirement traceability over visual styling.
- Technical gateway behavior is simplified into communication status blocks because the requirements define communication capability, not advanced diagnostics.
- Administrative pages avoid extra settings not supported by the current requirements set.
- Security interactions are focused on breach visibility and alarm activation rather than incident history or automation rules, which were not requested.

## Deliverables Saved
- `html/auth_access_mockup.html`
- `html/environment_dashboard_mockup.html`
- `html/admin_configuration_mockup.html`
- `html/system_operations_and_server_mockup.html`
- `html/gateway_communications_mockup.html`
- `html/temperature_control_mockup.html`
- `html/humidity_control_mockup.html`
- `html/security_monitoring_mockup.html`
- `html/power_control_mockup.html`
- `07_ui_mockups_and_interaction_design.md`

## Source Basis
This interaction design package was aligned against the existing project deliverables in the target output directory:
- `04_user_stories.md`
- `02_functional_requirements.md`

It also remains consistent with the raw DigitalHome SRS excerpt provided for this task.