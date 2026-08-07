## Business Analysis & Requirements Specification

### 5. Requirements & Story Traceability Matrix

| User Need ID | Derived Requirement IDs | Mapped User Story IDs | Primary Domain Area |
|--------------|-------------------------|-----------------------|---------------------|
| UN-001 | FR-003, FR-009, NFR-005, NFR-009 | US-003, US-009 | Content Access |
| UN-002 | FR-001 | US-001 | Authentication |
| UN-003 | FR-002, FR-003, FR-007 | US-002, US-003, US-007 | Personalization |
| UN-004 | FR-004, NFR-002 | US-004 | Live Ticker |
| UN-005 | FR-005 | US-005 | Football Information |
| UN-006 | FR-006, NFR-007 | US-006 | Streaming Links |
| UN-007 | FR-007 | US-007 | Notifications |
| UN-008 | FR-008 | US-008 | Social Sharing |
| UN-009 | FR-009, FR-010, NFR-001, NFR-003, NFR-004, NFR-009 | US-009, US-010 | UX & Resilience |
| UN-010 | NFR-003 |  | Scalability |
| UN-011 | FR-001, NFR-006 | US-001 | Privacy & Compliance |
| UN-012 | FR-011, NFR-008 | US-011 | Operations & Improvement |

### 6. Gaps & BA Recommendations

- **Rights Validation Logic:** The brief states that live stream links must only be shown where transmission rights are fulfilled in the user’s country, but it does not define the authoritative rights source, refresh frequency, or fallback behavior when rights status is unknown.
- **Authentication Details:** Registration and login are required, but the document does not specify allowed identity methods, password rules, account recovery, or whether guest access is permitted.
- **Notification Rules:** The brief confirms notifications for current events, news, or results, but does not define notification triggers, delivery channels, quiet hours, or user-level notification granularity.
- **Offline Scope:** The app must remain usable offline, but the brief does not specify which exact screens, data sets, or cached content must remain available without connectivity.
- **External API Dependency:** Live data comes from an external server, but no service-level expectations, API error handling rules, retry behavior, or data ownership responsibilities are specified.
- **Supported Social Platforms:** Social sharing is requested, but supported platforms and device OS-level sharing expectations are not specified.
- **Content Coverage Boundaries:** The brief mentions extensive coverage of all national and international leagues and competitions, but does not specify content providers, competition list boundaries, or regional exclusions.
- **Live Ticker Latency Assumption:** A measurable target of 5 seconds from external API receipt to display has been introduced to make NFR-002 testable; stakeholders should confirm whether this threshold is acceptable for production.
- **Peak-Load Performance Assumption:** Measurable thresholds for startup time, request response time, and error rate have been introduced to make NFR-003 testable; stakeholders should validate these as formal non-functional acceptance criteria.
- **External Update Consistency Scope:** The source text requires consistent UI and module behaviour despite external server updates, but does not specify how compatibility is maintained when external API contracts change; governance of versioning and backward compatibility should be agreed with the API provider.
- **HTML Mockups Scope Decision:** HTML mockups were explicitly requested and are treated as in scope for this revision. Because the source text lacks branding, visual design system, and detailed navigation specifications, any mockups should be labelled as low-fidelity assumption-based wireframes rather than final UI design.

### 7. Summary Statistics

- **Total Discovered User Needs:** 12
- **Total Functional Requirements (FR):** 11
- **Total Non-Functional Requirements (NFR):** 9
- **Total User Stories (US):** 11
- **Priority Breakdown:**
  - Must Have: 8
  - Should Have: 2
  - Could Have: 1
  - Won't Have: 0
- **User Needs Coverage:** 12 / 12