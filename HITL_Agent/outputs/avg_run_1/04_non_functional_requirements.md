# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall be fully loaded and ready for user interaction within a maximum of 2 seconds after application startup on supported Android and iOS devices under normal operating conditions.
- **Source:** UN-001
- **Priority:** High

### NFR-002
- **Requirement:** The system shall provide authentication screens and complete the transition from startup to an authenticated, usable app state through an uncomplicated mobile flow optimized for direct access at app launch.
- **Source:** UN-002
- **Priority:** Medium

### NFR-003
- **Requirement:** The system shall retrieve and display live ticker updates for in-progress matches with minimal practical delay supported by the external live-data API and current mobile network conditions.
- **Source:** UN-005
- **Priority:** High

### NFR-004
- **Requirement:** The system shall support at least 100,000 concurrent users during peak match-day demand without performance loss in core app functions.
- **Source:** UN-003, UN-004, UN-005, UN-006, UN-009
- **Priority:** High

### NFR-005
- **Requirement:** The system shall remain usable under limited network coverage by degrading gracefully, preserving access to previously cached content, and informing users when live or other network-dependent functions are unavailable.
- **Source:** UN-011
- **Priority:** High

### NFR-006
- **Requirement:** The system shall support offline usage for previously cached content when network connectivity is temporarily unavailable.
- **Source:** UN-011
- **Priority:** High

### NFR-007
- **Requirement:** The system shall ensure that live stream links are displayed only when the relevant transmission rights are valid for the user's country.
- **Source:** UN-007
- **Priority:** High

### NFR-008
- **Requirement:** The system shall present live stream access as deep-links to authorized external providers and shall not host or play live video streams directly within the app.
- **Source:** UN-007
- **Priority:** Medium

### NFR-009
- **Requirement:** The system shall keep the user interface and integrated modules consistent and operational even when external server-side content updates occur.
- **Source:** UN-003, UN-008, UN-011
- **Priority:** Medium

### NFR-010
- **Requirement:** The system shall process all personal data in compliance with GDPR requirements applicable to registration, login, personalization, notifications, and ongoing app usage.
- **Source:** UN-012
- **Priority:** High

### NFR-011
- **Requirement:** The system shall protect personal data by applying data-handling controls consistent with GDPR obligations, including lawful processing, data minimization, and privacy-compliant user data management.
- **Source:** UN-012
- **Priority:** High

### NFR-012
- **Requirement:** The system shall deliver push notifications for enabled favorite-team live score updates and news in a timely manner after the triggering event is received by the platform notification service.
- **Source:** UN-009
- **Priority:** Medium

### NFR-013
- **Requirement:** The system shall provide a direct and readily understandable user interface that allows users to access core football information and app modules without unnecessary navigation complexity.
- **Source:** UN-003, UN-004, UN-006, UN-008
- **Priority:** Medium
