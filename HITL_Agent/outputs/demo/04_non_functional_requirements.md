# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall be fully loaded and ready for user interaction within a maximum of 2 seconds after app startup on supported Android and iOS devices under normal operating conditions.
- **Source:** UN-002
- **Priority:** High

### NFR-002
- **Requirement:** The system shall retrieve and display live ticker updates for ongoing matches in near real time, subject to external API and network latency.
- **Source:** UN-004
- **Priority:** High

### NFR-003
- **Requirement:** The system shall continue to provide access to previously cached news content when network connectivity is limited or temporarily unavailable.
- **Source:** UN-010
- **Priority:** High

### NFR-004
- **Requirement:** The system shall remain usable under limited network coverage by preserving access to the user interface and cached news content without application failure.
- **Source:** UN-010
- **Priority:** High

### NFR-005
- **Requirement:** The system shall support at least 100,000 simultaneous users during peak match-day demand without performance loss in core user journeys.
- **Source:** UN-011
- **Priority:** High

### NFR-006
- **Requirement:** The system shall enforce country-based transmission rights rules so that live stream deep links are displayed only when the relevant broadcast rights are fulfilled in the user’s country.
- **Source:** UN-006
- **Priority:** High

### NFR-007
- **Requirement:** The system shall process all personal data in compliance with GDPR requirements applicable to user registration, login, personalization, and notifications.
- **Source:** UN-012
- **Priority:** High

### NFR-008
- **Requirement:** The system shall protect personal data exchanged between the mobile application and external services during login, account access, and personalization operations.
- **Source:** UN-001, UN-007, UN-012
- **Priority:** High

### NFR-009
- **Requirement:** The system shall keep the user interface and integrated modules consistent and operational despite updates to externally sourced server data.
- **Source:** UN-003, UN-004, UN-005, UN-007
- **Priority:** Medium

### NFR-010
- **Requirement:** The system shall deliver goal notifications for favorite teams as soon as current event data is received by the notification service.
- **Source:** UN-008
- **Priority:** Medium

### NFR-011
- **Requirement:** The system shall be available on both Android and iOS mobile platforms with equivalent support for the defined core features.
- **Source:** UN-002, UN-003, UN-004, UN-005, UN-006, UN-007, UN-008, UN-009, UN-010, UN-011
- **Priority:** High

### NFR-012
- **Requirement:** The system shall undergo thorough pre-release testing to detect and resolve malfunctions before production release.
- **Source:** UN-011
- **Priority:** Medium

### NFR-013
- **Requirement:** The system shall support continuous evaluation of user feedback and app reviews to inform post-release functional and quality improvements.
- **Source:** UN-011
- **Priority:** Low