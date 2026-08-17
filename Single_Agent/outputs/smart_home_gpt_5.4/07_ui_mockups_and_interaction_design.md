# 7. UI Mockups & Interaction Design

## HTML Mockup-to-User Story Mapping

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `login.html` | US-001 | Login form, role-aware access messaging, invalid credentials error, server unavailable state |
| `dashboard.html` | US-002 | Home dashboard cards, device status summary, connectivity indicator, empty configuration state, gateway offline state |
| `environment_control.html` | US-003, US-004 | Thermostat panel, humidistat panel, setpoint inputs, validation messaging, unavailable-device handling |
| `security_power.html` | US-005, US-006 | Security contact list, alarm state, breach alert, appliance/light power controls, unavailable control state |
| `admin_console.html` | US-007, US-008, US-009 | User account administration, default settings summary, start/stop controls, operational state, backup initiation and error state |

## Screen Layout Specifications

### 1. Login Screen
- Primary layout uses a centered credential card inside a mobile-style responsive frame.
- Key components: username field, password field, sign-in action, role-aware helper text.
- Alternative states show authentication failure and server unavailability.

### 2. Dashboard Screen
- Summary-first design with high-visibility metric cards for temperature, humidity, security, and active loads.
- Secondary detail list presents individual devices and system operational state.
- Empty and offline states preserve the same spatial structure for continuity and reduced cognitive load.

### 3. Environment Control Screen
- Two vertically stacked control sections separate thermostat and humidistat interactions.
- Each section combines current reading, target value, and update action.
- Error states are shown inline near the affected control to support rapid correction.

### 4. Security & Power Screen
- Security and power are grouped because both require quick operational decisions from the resident.
- The security section emphasizes exception visibility through prominent breach alerts and state pills.
- Power controls use direct action buttons rather than hidden menus to simplify switching tasks.

### 5. Admin Console Screen
- Administrative functions are segmented into system operation, user accounts, and backup/defaults.
- This grouping aligns with technician and master-user mental models for setup and maintenance.
- Restricted and failure states are explicitly visualized to demonstrate access control and operational resilience.

## UI/UX Trade-offs

### Simplicity vs. Technical Detail
- The prototype prioritizes clear resident-facing controls over highly detailed diagnostic telemetry.
- Technician needs are handled through a separate admin console rather than exposing all technical detail on end-user screens.

### Unified Dashboard vs. Deep Navigation
- A unified dashboard was chosen to satisfy the requirement for easy monitoring of multiple home conditions.
- This reduces navigation overhead for General Users, while specialized actions remain on dedicated screens.

### Direct Manipulation vs. Safety Friction
- Environmental and power controls are presented as direct actions for usability.
- Safety and correctness are balanced through visible validation, disabled controls in offline states, and role-based restrictions.

### Prototype Realism vs. Scope Control
- The interfaces surface connectivity, simulation, and degraded-state information to support proof-of-concept evaluation.
- More advanced commercial behaviors such as automation scheduling, event history, and multistep provisioning were intentionally excluded to stay within prototype scope.

## Interaction Design Notes
- All HTML mockups are standalone responsive pages.
- Each file includes mandatory multi-state subcases: populated, empty/unconfigured, and error/offline/restricted.
- Layouts use a repeatable responsive grid pattern to enable side-by-side comparison of normal and edge-case flows during stakeholder review.
