# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall become fully loaded and ready for user interaction within 2 seconds of app startup under normal supported device and network conditions.
- **Source:** UN-001
- **Priority:** High

### NFR-002
- **Requirement:** The system shall support at least 100,000 concurrent users on peak match days without material degradation of response times for news retrieval, live score retrieval, and notification delivery.
- **Source:** UN-003, UN-001
- **Priority:** High

### NFR-003
- **Requirement:** The system shall continue to provide access to cached news, preferences, team details, and last known live data during temporary connectivity loss, and shall clearly indicate offline or degraded states to the user.
- **Source:** UN-009
- **Priority:** High

### NFR-004
- **Requirement:** The system shall present a mobile-first user interface for Android and iOS that enables users to access core news, live ticker, and navigation features in no more than 3 interactions from the home screen.
- **Source:** UN-001, UN-004
- **Priority:** Medium

### NFR-005
- **Requirement:** The system shall process personal data in compliance with GDPR, including lawful consent capture where required, privacy notice availability, and mechanisms supporting data access, correction, and deletion requests.
- **Source:** UN-010
- **Priority:** High

### NFR-006
- **Requirement:** The system shall protect account and personal data in transit and at rest using industry-standard encryption and authenticated access controls.
- **Source:** UN-010
- **Priority:** High

### NFR-007
- **Requirement:** The system shall monitor application health, log failures, and support pre-release testing and post-release issue resolution processes to detect and resolve malfunctions early.
- **Source:** UN-009, UN-010
- **Priority:** Medium

### NFR-008
- **Requirement:** The system shall maintain stable interface structures and module interoperability even when external live data sources update or return delayed responses.
- **Source:** UN-003, UN-009
- **Priority:** Medium
