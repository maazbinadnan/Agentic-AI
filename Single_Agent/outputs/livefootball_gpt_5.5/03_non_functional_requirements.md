# 3. Non-Functional Requirements

### NFR-001
- **Requirement:** The system shall complete cold-start loading and render the first usable screen within 2 seconds on supported Android and iOS devices under normal network conditions.
- **Source:** UN-001
- **Priority:** High

### NFR-002
- **Requirement:** The system shall maintain smooth interaction performance with no more than 100 milliseconds average UI response latency for common navigation and preference actions on supported devices.
- **Source:** UN-001
- **Priority:** High

### NFR-003
- **Requirement:** The system shall support at least 100,000 simultaneous users on match days without material degradation of login, news, live ticker, and notification services.
- **Source:** UN-013
- **Priority:** High

### NFR-004
- **Requirement:** The system shall maintain 99.5% monthly availability for core services excluding planned maintenance windows.
- **Source:** UN-013
- **Priority:** High

### NFR-005
- **Requirement:** The system shall remain navigable and shall provide access to cached favorites, recent news, recent scores, and saved profiles when network connectivity is unavailable.
- **Source:** UN-011
- **Priority:** High

### NFR-006
- **Requirement:** The system shall detect network loss within 5 seconds and display a clear offline or reconnecting status without terminating the user session.
- **Source:** UN-011
- **Priority:** High

### NFR-007
- **Requirement:** The system shall process personal data in compliance with GDPR, including lawful basis, transparency, consent management where required, data minimization, retention controls, and user rights handling.
- **Source:** UN-012
- **Priority:** High

### NFR-008
- **Requirement:** The system shall encrypt personal data in transit using TLS 1.2 or higher and shall encrypt sensitive personal data at rest using industry-standard encryption.
- **Source:** UN-012
- **Priority:** High

### NFR-009
- **Requirement:** The system shall validate and sanitize all external API responses before rendering them in the user interface to preserve module consistency and prevent malformed content from disrupting the app.
- **Source:** UN-005, UN-013
- **Priority:** High

### NFR-010
- **Requirement:** The system shall refresh active live ticker data at least every 10 seconds where supported by the external data provider and connectivity conditions.
- **Source:** UN-005
- **Priority:** High

### NFR-011
- **Requirement:** The system shall meet WCAG 2.1 AA-aligned mobile accessibility expectations for color contrast, text scaling, focus order, and screen-reader labels on core screens.
- **Source:** UN-001, UN-012
- **Priority:** Medium

### NFR-012
- **Requirement:** The system shall log client and service errors in a privacy-preserving manner and shall make diagnostic information available to support teams for pre-release testing and post-release issue resolution.
- **Source:** UN-013, UN-012
- **Priority:** Medium
