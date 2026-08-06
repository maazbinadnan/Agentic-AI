# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall load and be fully ready for authenticated user interaction within a maximum of two seconds after application start under normal supported-device and network conditions, excluding first-time installation, operating-system cold-start variance, and external provider outages.
- **Source:** UN-002
- **Priority:** High

### NFR-002
- **Requirement:** The system shall provide smooth mobile interaction by completing primary in-app navigation actions, including opening news, live ticker, team/player information, notifications, and sharing screens, within one second at the 95th percentile on supported Android and iOS devices under normal operating conditions.
- **Source:** UN-002, UN-003, UN-004, UN-005, UN-007, UN-008
- **Priority:** High

### NFR-003
- **Requirement:** The system shall retrieve and display live ticker score and match-event updates in the user interface within five seconds at the 95th percentile after successful receipt of data from the external live-data API during live matches.
- **Source:** UN-004
- **Priority:** High

### NFR-004
- **Requirement:** The system shall support up to 100,000 simultaneous users on high-traffic match days without performance loss, maintaining 95th-percentile backend response times of no more than one second for core read operations including news, live ticker, team/player information, and notification-related data retrieval.
- **Source:** UN-010
- **Priority:** High

### NFR-005
- **Requirement:** The system shall maintain at least 99.5% monthly availability for authenticated core services and shall avoid planned downtime during live match windows for covered European leagues and competitions.
- **Source:** UN-004, UN-010
- **Priority:** High

### NFR-006
- **Requirement:** The system shall remain usable during limited or lost connectivity by presenting previously loaded cached content in read-only mode within two seconds, clearly indicating offline or stale status for live data, and preventing server-dependent changes such as favorite-team or notification-preference updates while offline.
- **Source:** UN-009
- **Priority:** High

### NFR-007
- **Requirement:** The system shall support both Android and iOS mobile platforms by passing 100% of release-blocking functional, startup-performance, and compatibility smoke tests on the supported operating-system versions and device classes defined for each production release.
- **Source:** UN-002
- **Priority:** High

### NFR-008
- **Requirement:** The system shall require a valid authenticated session for 100% of protected app features, including news, live ticker, team/player information, personalization, notifications, sharing, and stream-link access, with only registration, login, password recovery, and privacy/legal information accessible without authentication.
- **Source:** UN-001, UN-011
- **Priority:** High

### NFR-009
- **Requirement:** The system shall protect personal data and authentication data by encrypting data in transit using TLS 1.2 or higher and by storing credentials, tokens, and personal data only in platform-secure storage or encrypted application storage on supported Android and iOS devices.
- **Source:** UN-001, UN-011
- **Priority:** High

### NFR-010
- **Requirement:** The system shall process all personal data in compliance with GDPR by supporting lawful processing, data minimization, privacy notices, consent capture where required, withdrawal of consent, and data-subject access, export, rectification, and erasure workflows within legally required response timeframes.
- **Source:** UN-011
- **Priority:** High

### NFR-011
- **Requirement:** The system shall display live broadcast deep links only when the broadcast has begun and rights metadata confirms that the relevant provider link is authorized for the user’s country, and the system shall not host, retransmit, or embed live video streams.
- **Source:** UN-006
- **Priority:** High

### NFR-012
- **Requirement:** The system shall send football news, result, and match-event notifications only after the user has explicitly enabled notifications and granted operating-system notification permission, and the system shall stop sending such notifications within five minutes after notification permission or in-app notification preference withdrawal is detected.
- **Source:** UN-007, UN-011
- **Priority:** High

### NFR-013
- **Requirement:** The system shall meet WCAG 2.2 AA applicable mobile accessibility criteria for core user journeys, including screen-reader support for interactive elements, text scaling up to 200% without loss of core functionality, and minimum text/background contrast of 4.5:1 for standard text.
- **Source:** UN-002
- **Priority:** Medium

### NFR-014
- **Requirement:** The system shall complete pre-release testing with zero open critical or high-severity defects across functional, performance, peak-load, limited-connectivity, Android/iOS compatibility, security, privacy, and GDPR compliance test suites before production release.
- **Source:** UN-010, UN-011, UN-012
- **Priority:** High

### NFR-015
- **Requirement:** The system shall support continuous improvement by collecting user feedback, app-review insights, and production defect reports, triaging them at least weekly, and triaging critical production defects within one business day of detection.
- **Source:** UN-012
- **Priority:** Medium

### NFR-016
- **Requirement:** The system shall maintain user-interface and module stability when external server data changes by tolerating additive API fields without application failure and by displaying a controlled error or fallback state within two seconds when required external data is unavailable or invalid.
- **Source:** UN-004, UN-009, UN-010
- **Priority:** Medium

### NFR-017
- **Requirement:** The system shall protect user privacy during social sharing by using native Android and iOS sharing mechanisms and by excluding authentication tokens, account identifiers, notification preferences, and other personal data from 100% of shared news or match-report payloads.
- **Source:** UN-008, UN-011
- **Priority:** Medium
