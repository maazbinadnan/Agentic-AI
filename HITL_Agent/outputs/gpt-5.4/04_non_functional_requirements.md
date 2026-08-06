# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall load and be fully ready for user interaction within 2 seconds of app startup on supported Android and iOS devices under normal operating conditions.
- **Source:** UN-011
- **Priority:** High

### NFR-002
- **Requirement:** The system shall support up to 100,000 concurrent users during peak match-day periods without performance loss that prevents users from accessing core features, including authentication, news viewing, live ticker updates, notifications, and deep-link access to eligible live streams.
- **Source:** UN-013
- **Priority:** High

### NFR-003
- **Requirement:** The system shall retrieve and display live ticker data in real time from the external API and shall continuously refresh current match data while network connectivity is available.
- **Source:** UN-004
- **Priority:** High

### NFR-004
- **Requirement:** The system shall remain usable under limited network coverage and shall continue to provide offline access to previously loaded content and saved user preferences during temporary loss of connectivity.
- **Source:** UN-012
- **Priority:** High

### NFR-005
- **Requirement:** The system shall maintain a consistent user interface and stable operation of fixed app modules even when external server data or updates are received.
- **Source:** UN-004, UN-011
- **Priority:** Medium

### NFR-006
- **Requirement:** The system shall provide a user interface that enables users to access core information and functions directly with uncomplicated startup registration and login flows.
- **Source:** UN-001, UN-011
- **Priority:** High

### NFR-007
- **Requirement:** The system shall display live stream links only when a live broadcast has begun and when the relevant transmission rights are valid for the user’s country.
- **Source:** UN-007, UN-008
- **Priority:** High

### NFR-008
- **Requirement:** The system shall process all personal data in compliance with GDPR across registration, login, personalization, notifications, and ongoing app usage.
- **Source:** UN-014
- **Priority:** High

### NFR-009
- **Requirement:** The system shall send notifications about news and results only to users who have explicitly opted in to receive such notifications.
- **Source:** UN-009, UN-014
- **Priority:** High

### NFR-010
- **Requirement:** The system shall preserve the availability of detailed team and player information for user access at any time, subject to network availability or cached offline data where applicable.
- **Source:** UN-006, UN-012
- **Priority:** Medium

### NFR-011
- **Requirement:** The system shall undergo thorough pre-release testing and issue resolution activities to detect and correct malfunctions before production release.
- **Source:** UN-013
- **Priority:** Medium

### NFR-012
- **Requirement:** The system shall support continuous post-release evaluation of user feedback and app reviews to inform ongoing functional and service quality improvements.
- **Source:** UN-015
- **Priority:** Low
