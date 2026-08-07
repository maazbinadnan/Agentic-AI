# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, FR-003, FR-009, NFR-001, NFR-002, NFR-004 | US-001, US-003, US-009 | Startup Performance & Core Access |
| UN-002 | FR-002, FR-003 | US-002, US-003 | Personalization |
| UN-003 | FR-004, NFR-002, NFR-008 | US-004 | Live Match Tracking |
| UN-004 | FR-005, NFR-004 | US-005 | Football Coverage & Discovery |
| UN-005 | FR-006 | US-006 | Stream Access & Rights Compliance |
| UN-006 | FR-002, FR-007 | US-002, US-007 | Notifications |
| UN-007 | FR-001 | US-001 | Onboarding & Authentication |
| UN-008 | FR-008 | US-008 | Social Sharing |
| UN-009 | FR-009, NFR-003, NFR-007, NFR-008 | US-009 | Offline Reliability |
| UN-010 | FR-006, NFR-005, NFR-006, NFR-007 | US-006 | Privacy & Compliance |

---
## Gaps & BA Recommendations

### Authentication Method Not Specified
- **Observation:** The brief requires uncomplicated registration and login, but does not define whether email/password, social login, passwordless authentication, or guest mode are required.
- **Recommendation:** Confirm approved authentication methods and whether unregistered users may browse non-personalized content.

### Real-Time Update SLA Is Undefined
- **Observation:** The app must provide real-time live ticker data, but the acceptable refresh frequency and end-to-end latency are not specified.
- **Recommendation:** Define measurable SLAs for live score and event update intervals and acceptable delays during peak traffic.

### Offline Functional Scope Needs Clarification
- **Observation:** The app is required to remain usable offline, but the mandatory offline dataset is not fully defined.
- **Recommendation:** Confirm which screens and data types must be cached, cache retention duration, and stale-data labeling rules.

### Rights Validation Logic Requires Detail
- **Observation:** Stream links must comply with country-specific transmission rights, but the method used to determine the user’s country is not stated.
- **Recommendation:** Define the source of geo-eligibility and any fallback behavior when location cannot be verified.

### Notification Taxonomy Is Incomplete
- **Observation:** Notifications are mentioned for news and results, but granular event types and delivery urgency are not described.
- **Recommendation:** Specify supported triggers such as goals, kickoff, full-time, lineup release, breaking news, and stream-start alerts.

### Search Capability Is Implied but Not Explicit
- **Observation:** Comprehensive coverage of competitions, teams, and players suggests a need for search or guided discovery, but this is not directly stated.
- **Recommendation:** Decide whether search, filters, and browse hierarchies are required in MVP.

---
## Summary Statistics

- **Total Discovered User Needs:** 10
- **Total Functional Requirements (FR):** 9
- **Total Non-Functional Requirements (NFR):** 8
- **Total User Stories (US):** 9
- **User Needs Coverage:** 10/10

### Priority Breakdown
- **High:** 20
- **Medium:** 6
- **Low:** 0
