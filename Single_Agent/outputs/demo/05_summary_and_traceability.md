# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, NFR-001, NFR-006 | US-001 | Access & Onboarding |
| UN-002 | FR-002, FR-003, FR-007 | US-002, US-003, US-007 | Personalization |
| UN-003 | FR-003, NFR-003, NFR-006 | US-003 | News Delivery |
| UN-004 | FR-004, NFR-002, NFR-003 | US-004 | Live Ticker |
| UN-005 | FR-005, NFR-006 | US-005 | Football Discovery |
| UN-006 | FR-006, NFR-007 | US-006 | Streaming & Rights Compliance |
| UN-007 | FR-007, NFR-003 | US-007 | Notifications |
| UN-008 | FR-008 | US-008 | Social Sharing |
| UN-009 | FR-009, NFR-004, NFR-008, NFR-009 | US-009 | Offline Reliability |
| UN-010 | FR-010, NFR-005, NFR-008 | US-010 | Privacy & Compliance |

---
## Gaps & BA Recommendations

### Authentication Scope Unclear
- **Observation:** The source requires uncomplicated registration and login at startup, but does not define guest access, password reset, social sign-in, or verification requirements.
- **Recommendation:** Confirm the authentication model, supported credential methods, recovery flows, and whether unauthenticated browsing is allowed.

### Offline Feature Boundaries Not Specified
- **Observation:** The app must remain usable offline, but the exact set of supported offline screens and cached content rules are not defined.
- **Recommendation:** Define offline-capable features, cache retention duration, stale-data labeling, and synchronization behavior after reconnect.

### Notification Rules Need Refinement
- **Observation:** Notifications are described broadly for current events, news, and results, but event triggers and user controls are not detailed.
- **Recommendation:** Specify notification categories, trigger events, quiet-hour behavior, rate limits, and permission education screens.

### Streaming Integration Ambiguity
- **Observation:** Live stream links are required, but the exact user experience is unclear, including whether streams open in-app or via external providers.
- **Recommendation:** Confirm provider integration boundaries, launch behavior, rights-verification source, and region-resolution method.

### GDPR Operational Controls Incomplete
- **Observation:** GDPR compliance is stated, but no explicit requirements are given for consent records, retention, deletion, export, or user rights handling.
- **Recommendation:** Add dedicated compliance stories and requirements for privacy notice access, consent capture, account deletion, and data subject request fulfillment.

### Coverage Scope Requires Commercial Validation
- **Observation:** The phrase “all leagues and competitions” may exceed practical content licensing and data provider coverage.
- **Recommendation:** Replace this with a governed catalog of supported competitions and define a process for content expansion.

---
## Summary Statistics

- **Total Discovered User Needs:** 10
- **Total Functional Requirements (FR):** 10
- **Total Non-Functional Requirements (NFR):** 9
- **Total User Stories (US):** 10
- **User Needs Coverage:** 10/10

### Priority Breakdown
- **High:** 21
- **Medium:** 8
- **Low:** 0