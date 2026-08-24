## Business Analysis & Requirements Specification

### 5. Requirements & Story Traceability Matrix

| User Need ID | Derived Requirement IDs | Mapped User Story IDs | Primary Domain Area |
|--------------|-------------------------|-----------------------|---------------------|
| UN-001 | FR-001, NFR-001, NFR-002 | US-001 | Platform / Startup UX |
| UN-002 | FR-002 | US-002 | News |
| UN-003 | FR-003, NFR-003 | US-003 | Live Ticker |
| UN-004 | FR-004 | US-004 | Competition Coverage |
| UN-005 | FR-005 | US-005 | Team & Player Data |
| UN-006 | FR-006, NFR-007 | US-006 | Live Streaming |
| UN-007 | FR-007 | US-007 | Authentication |
| UN-008 | FR-002, FR-008, NFR-002 | US-002, US-008 | Personalization |
| UN-009 | FR-008, FR-009 | US-008, US-009 | Notifications |
| UN-010 | FR-010 | US-010 | Social Sharing |
| UN-011 | FR-011, NFR-004 | US-011 | Offline Reliability |
| UN-012 | NFR-005 | NFR-only / no user story required | Scalability |
| UN-013 | NFR-006 | NFR-only / no user story required | Privacy / Compliance |
| UN-014 | FR-012, NFR-008 | US-012 | Operations / Improvement |

### 6. Gaps & BA Recommendations

- **Offline Scope Ambiguity:** The source states that the app remains usable offline, but it does not specify which content must be available without connectivity. Stakeholders should define the minimum offline-capable feature set, such as cached news, saved team pages, or last known scores.
- **Peak-Load KPI Assumption:** The revised scalability requirement now includes measurable service-level indicators to satisfy testability, but the source document did not supply exact thresholds for response time or error rate. Stakeholders should confirm or replace the assumed p95 response time and error-rate targets.
- **Live Ticker Latency Assumption:** The revised live ticker latency requirement now includes a measurable UI update target to satisfy testability, but the source document did not specify the exact threshold. Stakeholders should validate the 5-second assumption against business expectations and data-provider capabilities.
- **Authentication Details Missing:** Registration and login are required, but account fields, supported identity methods, password rules, account recovery, and session behavior are not specified.
- **Notification Rules Missing:** The source mentions notifications for news and results, but trigger events, delivery timing, quiet hours, notification channels, and opt-in granularity are undefined.
- **Broadcast Rights Logic Incomplete:** The source mentions country-based rights compliance, but the method for determining user country, handling travel/roaming, and behavior on VPN or ambiguous geolocation is unspecified.
- **Preferred Sports Channels Model Undefined:** The source states that users can select preferred sports channels, but available channel lists, source integrations, and filtering logic are not defined.
- **Module Configuration Scope Unclear:** The source refers to additional modules that users can configure and connect to the interface, but module types, constraints, and personalization boundaries are not specified.
- **Compliance Detail Gap:** GDPR compliance is required, but the lawful basis, consent model, retention periods, data subject rights handling, and data processor responsibilities are not stated.
- **Testing and Support Process Scope:** The source references a thorough testing and support process, but acceptance test coverage, defect severity thresholds, support channels, and post-release SLA expectations are unspecified.
- **Feedback Mechanism Detail Gap:** The revision defines feedback as an in-app submission and review capability for clarity, but the source did not explicitly confirm whether app-store reviews must also be ingested or whether review access is in-app, back-office, or operational reporting.
- **HTML Mockups Request Outside Source Scope:** The user requested HTML mockups, but the source document does not provide enough UI layout detail, branding, navigation structure, or content hierarchy to produce evidence-based mockups without introducing assumptions. A separate wireframing brief is recommended.

### 7. Summary Statistics

- **Total Discovered User Needs:** 14
- **Total Functional Requirements (FR):** 12
- **Total Non-Functional Requirements (NFR):** 8
- **Total User Stories (US):** 12
- **Priority Breakdown:**
  - Must Have: 8
  - Should Have: 3
  - Could Have: 1
  - Won't Have: 0
- **User Needs Coverage:** 14 / 14
