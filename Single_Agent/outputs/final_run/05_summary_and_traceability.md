# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, NFR-001, NFR-005 | US-001 | Onboarding & Access |
| UN-002 | FR-002, FR-003 | US-002, US-003 | Personalization |
| UN-003 | FR-003, FR-005, FR-006, NFR-005 | US-003, US-005, US-006 | Content & Discovery |
| UN-004 | FR-004, NFR-004 | US-004 | Live Match Experience |
| UN-005 | FR-006 | US-006 | Team & Player Information |
| UN-006 | FR-007, NFR-007 | US-007 | Stream Availability |
| UN-007 | FR-002, FR-008 | US-002, US-008 | Notifications |
| UN-008 | FR-009 | US-009 | Social Sharing |
| UN-009 | FR-004, FR-010, NFR-001, NFR-002, NFR-003, NFR-004, NFR-008 | US-004, US-010 | Reliability & Scale |
| UN-010 | FR-001, FR-002, FR-007, NFR-006, NFR-007, NFR-008 | US-001, US-002, US-007 | Privacy & Compliance |

---
## Gaps & BA Recommendations

### Authentication Method Ambiguity
- **Observation:** The source requires uncomplicated registration and login but does not specify identity providers, password rules, account verification, or guest access.
- **Recommendation:** Confirm whether MVP authentication uses email/password only or also supports social login, and define minimum verification and recovery flows.

### Offline Scope Definition
- **Observation:** The app must remain usable offline, but the exact set of cached content and user actions supported offline is not specified.
- **Recommendation:** Define a cache matrix covering news feed, team/player details, last-known live ticker state, competition pages, and preference editing behavior while offline.

### Live Data Freshness Threshold
- **Observation:** The source requires real-time live data but does not quantify acceptable update latency or fallback intervals.
- **Recommendation:** Establish measurable service targets for update frequency, event delay tolerance, and stale-data indicators.

### Streaming Link Behavior
- **Observation:** Live stream links are mentioned, but it is unclear whether links open in-app, via deep link, or in an external browser/provider app.
- **Recommendation:** Define provider integration behavior, user redirection flow, and error handling for unavailable or uninstalled providers.

### Rights Validation Logic
- **Observation:** Country-based transmission rights compliance is required, but the source does not specify how user country is determined or audited.
- **Recommendation:** Confirm the rights-validation mechanism, auditability expectations, and fallback behavior when country determination is uncertain.

### Notification Granularity
- **Observation:** Notifications for news and results are required, but event categories, quiet hours, and per-team/per-event granularity are unspecified.
- **Recommendation:** Define notification taxonomy for MVP, including match start, goals, final result, breaking news, and opt-in controls.

### Content Provider and API Dependency Risk
- **Observation:** The live ticker depends on an external server/API, and broader content likely also depends on external feeds.
- **Recommendation:** Add provider SLA, retry policy, timeout handling, and operational monitoring requirements to reduce dependency risk.

---
## Summary Statistics

- **Total Discovered User Needs:** 10
- **Total Functional Requirements (FR):** 10
- **Total Non-Functional Requirements (NFR):** 8
- **Total User Stories (US):** 10
- **User Needs Coverage:** 10/10

### Priority Breakdown
- **High:** 18
- **Medium:** 10
- **Low:** 0