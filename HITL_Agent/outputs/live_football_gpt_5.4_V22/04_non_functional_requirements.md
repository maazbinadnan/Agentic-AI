# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall be fully loaded and ready for authenticated user interaction within 2 seconds of application startup on supported Android and iOS devices under normal operating conditions.
- **Source:** UN-001
- **Priority:** High

### NFR-002
- **Requirement:** The system shall support at least 100,000 concurrent users during peak match-day periods without loss of availability of core features including login, news retrieval, live ticker access, personalization, and notification event processing.
- **Source:** UN-002
- **Priority:** High

### NFR-003
- **Requirement:** The system shall display newly received live ticker updates in the mobile user interface within 2 seconds of successful receipt from the external live-data API.
- **Source:** UN-003
- **Priority:** High

### NFR-004
- **Requirement:** The system shall maintain an end-to-end service availability of at least 99.5% per calendar month for core end-user functions excluding planned maintenance windows announced at least 24 hours in advance.
- **Source:** UN-002, UN-003
- **Priority:** High

### NFR-005
- **Requirement:** The system shall preserve offline usability by allowing users to access the most recently cached news, stories, and scores for at least 24 hours after network loss.
- **Source:** UN-004
- **Priority:** High

### NFR-006
- **Requirement:** The system shall automatically detect restoration of network connectivity and refresh stale live content within 30 seconds without requiring the user to restart the application.
- **Source:** UN-004, UN-003
- **Priority:** Medium

### NFR-007
- **Requirement:** The system shall ensure that 95% of standard screen transitions initiated by the user complete within 1 second on supported Android and iOS devices under normal operating conditions.
- **Source:** UN-001, UN-005
- **Priority:** Medium

### NFR-008
- **Requirement:** The system shall use secure transport encryption with TLS 1.2 or higher for all communications between the mobile application and external APIs, authentication services, notification services, and backend endpoints.
- **Source:** UN-006
- **Priority:** High

### NFR-009
- **Requirement:** The system shall encrypt personal data stored on backend systems and any authentication tokens stored on the mobile device using platform-approved cryptographic mechanisms.
- **Source:** UN-006, UN-007
- **Priority:** High

### NFR-010
- **Requirement:** The system shall require successful user authentication before access to any application features is granted at startup.
- **Source:** UN-007
- **Priority:** High

### NFR-011
- **Requirement:** The system shall process personal data in compliance with GDPR, including providing users with clear privacy information, consent controls where required, and mechanisms to request access, correction, and deletion of their personal data.
- **Source:** UN-006
- **Priority:** High

### NFR-012
- **Requirement:** The system shall restrict display of live-stream deep links to countries and contexts in which transmission rights are valid, based on rights-availability data applied at the time the link is presented.
- **Source:** UN-008
- **Priority:** High

### NFR-013
- **Requirement:** The system shall not embed or stream live video content internally and shall present live-stream access only as external deep links to licensed third-party providers.
- **Source:** UN-008
- **Priority:** Medium

### NFR-014
- **Requirement:** The system shall ensure that all fixed user interface modules remain functionally consistent and visually intact after external server-side content or data updates.
- **Source:** UN-005
- **Priority:** Medium

### NFR-015
- **Requirement:** The system shall deliver push notifications for enabled favorite-team news and result events to the notification service within 5 seconds of the triggering event being received by the application backend.
- **Source:** UN-009
- **Priority:** Medium

### NFR-016
- **Requirement:** The system shall ensure that notification preferences are opt-in, user-configurable, and changeable at any time from within the application.
- **Source:** UN-009, UN-006
- **Priority:** High

### NFR-017
- **Requirement:** The system shall support installation and operation on both Android and iOS platforms through platform-standard distribution channels.
- **Source:** UN-010
- **Priority:** High

### NFR-018
- **Requirement:** The system shall provide social sharing through platform-standard sharing mechanisms without exposing unpublished personal data beyond the content explicitly selected by the user for sharing.
- **Source:** UN-011, UN-006
- **Priority:** Medium

### NFR-019
- **Requirement:** The system shall tolerate temporary external live-data API unavailability by continuing to display the most recently retrieved match data together with a visible indication that live updates are temporarily unavailable.
- **Source:** UN-003, UN-004
- **Priority:** High

### NFR-020
- **Requirement:** The system shall log application errors, failed API calls, and critical service interruptions with timestamps and diagnostic context sufficient to support fault analysis and resolution.
- **Source:** UN-012
- **Priority:** Medium

### NFR-021
- **Requirement:** The system shall support daily automated backup of user account data, favorites, and notification preferences, and shall enable restoration of backed-up data within 4 hours of a production recovery event.
- **Source:** UN-006, UN-012
- **Priority:** Medium

### NFR-022
- **Requirement:** The system shall achieve a mean time to restore core service functionality of no more than 4 hours after a Sev-1 production incident.
- **Source:** UN-012
- **Priority:** Medium

### NFR-023
- **Requirement:** The system shall be designed so that no single backend service failure causes complete loss of all core end-user functionality.
- **Source:** UN-002, UN-012
- **Priority:** Medium

### NFR-024
- **Requirement:** The system shall retain audit records of authentication events, consent changes, and personal-data management actions for at least 12 months for security and compliance purposes.
- **Source:** UN-006, UN-007
- **Priority:** Medium

### NFR-025
- **Requirement:** The system shall collect, store, and process only the minimum personal data necessary to provide account access, personalization, and notification features.
- **Source:** UN-006
- **Priority:** High

### NFR-026
- **Requirement:** The system shall ensure that 99% of successful login requests complete within 5 seconds under normal operating conditions.
- **Source:** UN-007, UN-001
- **Priority:** High

### NFR-027
- **Requirement:** The system shall display cached content when bandwidth is limited or connectivity is intermittent, with the user interface remaining responsive to user input within 2 seconds for cached-content views.
- **Source:** UN-004, UN-005
- **Priority:** High

### NFR-028
- **Requirement:** The system shall validate all data received from external APIs before presentation in the user interface to prevent malformed or unauthorized content from being rendered to users.
- **Source:** UN-003, UN-006
- **Priority:** High
