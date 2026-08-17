# 3. Non-Functional Requirements

### NFR-001  
- **Requirement:** The system shall provide a browser-based user interface that supports common web interactions for non-technical users and renders core pages responsively on modern web-ready devices at widths from 320 px upward.
- **Source:** UN-001, UN-002, UN-003

### NFR-002  
- **Requirement:** The system shall enforce role-based access control such that General Users can access monitoring and control features only, while Master Users and DH Technicians can additionally access configuration, account management, and system operation functions.
- **Source:** UN-001, UN-006, UN-007

### NFR-003  
- **Requirement:** The system shall display updated simulated device and sensor status to the user within 5 seconds of a page refresh or control request under normal prototype operating conditions.
- **Source:** UN-002, UN-003, UN-004, UN-005

### NFR-004  
- **Requirement:** The system shall validate user-entered control values against configured device constraints and shall reject invalid entries with a clear error message without applying the change.
- **Source:** UN-003, UN-006

### NFR-005  
- **Requirement:** The system shall persist user account data, plans, and operational data and shall support backup execution without loss of previously committed records during normal operation.
- **Source:** UN-008

### NFR-006  
- **Requirement:** The system shall operate in a realistic simulated environment that models the behavior and constraints of an actual home, including simulated sensors, controllers, and device state transitions.
- **Source:** UN-002, UN-003, UN-004, UN-005, UN-007

### NFR-007  
- **Requirement:** The system shall use widely accepted, available hardware, software technologies, and communication standards where feasible to support cost-conscious prototype delivery and maintainability.
- **Source:** UN-007, UN-008

### NFR-008  
- **Requirement:** The system shall indicate communication or service unavailability when the home server, gateway, or simulated devices cannot be reached, and shall prevent control actions that require unavailable components.
- **Source:** UN-002, UN-003, UN-004, UN-005, UN-007

### NFR-009  
- **Requirement:** The prototype software and supporting configuration shall be deliverable within a 12-month project window by a five-engineer team using the prescribed organizational development process.
- **Source:** UN-007
