# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, NFR-001, NFR-002 | US-001 | Access & Role-Based Use |
| UN-002 | FR-002, NFR-001, NFR-003, NFR-006, NFR-008 | US-002 | Monitoring Dashboard |
| UN-003 | FR-003, FR-004, NFR-001, NFR-003, NFR-004, NFR-008 | US-003, US-004 | Environmental Control |
| UN-004 | FR-005, NFR-003, NFR-006, NFR-008 | US-005 | Security Monitoring |
| UN-005 | FR-006, NFR-003, NFR-006, NFR-008 | US-006 | Appliance & Lighting Control |
| UN-006 | FR-001, FR-007, FR-009, NFR-002, NFR-004 | US-001, US-007, US-009 | Household Administration |
| UN-007 | FR-001, FR-007, FR-008, FR-009, NFR-002, NFR-006, NFR-007, NFR-009 | US-001, US-007, US-008, US-009 | Technical Administration |
| UN-008 | FR-009, NFR-005, NFR-007 | US-009 | Data Storage & Backup |

---
## Gaps & BA Recommendations

### Authentication & Session Policy
- **Observation:** The source material implies web login and role separation, but does not define password rules, account recovery, session timeout, or lockout behavior.
- **Recommendation:** Confirm minimum credential policy, session expiration, and whether password reset is required in the prototype.

### Security Operation Detail
- **Observation:** Contact switches and alarms are specified, but arming modes, alarm acknowledgement, reset behavior, and event history are not defined.
- **Recommendation:** Clarify whether the prototype needs arm/disarm workflows, breach timestamps, or alarm reset controls.

### Device Inventory & Naming
- **Observation:** The source material identifies device categories but does not define how devices are labeled, grouped, or assigned to rooms.
- **Recommendation:** Introduce a simple room/zone and device naming model to improve dashboard usability and test realism.

### Backup & Restore Scope
- **Observation:** Backup support is required, but restore capability, frequency, retention, and status reporting detail are absent.
- **Recommendation:** Confirm whether manual backup alone is sufficient for the prototype or whether restore and scheduling are also needed.

### Lighting Control Semantics
- **Observation:** Lighting units are in project scope, but no specialized dimming or scheduling functions are described.
- **Recommendation:** Treat lighting as binary on/off power-switch-controlled devices unless stakeholders request richer control behavior.

### Operational State Model
- **Observation:** Technicians can start and stop system operation, but the defined system states and the effect on active sessions and queued commands are unspecified.
- **Recommendation:** Define at least Running, Stopped, and Degraded states for prototype clarity and testing.

---
## Summary Statistics

- **Total Discovered User Needs:** 8
- **Total Functional Requirements (FR):** 9
- **Total Non-Functional Requirements (NFR):** 9
- **Total User Stories (US):** 9
- **User Needs Coverage:** 8/8

### Priority Breakdown
- **High:** 5
- **Medium:** 4
- **Low:** 0
