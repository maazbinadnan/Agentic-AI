# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, NFR-005 | US-001 | Content & Information Access |
| UN-002 | FR-002, FR-006 | US-002, US-006 | Personalization & Notifications |
| UN-003 | FR-003 | US-003 | Live Ticker |
| UN-004 | FR-004 | US-004 | Live Streams |
| UN-005 | FR-005 | US-005 | Authentication |
| UN-006 | FR-007 | US-007 | Social Sharing |
| UN-007 | FR-008, NFR-001, NFR-002, NFR-003 | US-008 | Performance & Reliability |
| UN-008 | NFR-004 | US-009 | Privacy & Compliance |

---
## Gaps & BA Recommendations

### Authentication method details are unspecified
- **Observation:** The input states that registration and login should be uncomplicated and available at startup, but does not define supported authentication methods, mandatory registration fields, password rules, or account recovery behavior.
- **Recommendation:** Confirm whether authentication will use email/password only, social login, phone verification, guest access, and password reset capabilities.

### Offline behavior scope is ambiguous
- **Observation:** The input says the app remains usable offline, but does not specify which content must be cached locally, how long cached data remains valid, or which functions are expected to degrade gracefully. The current requirement has been limited to the interface, locally stored user configuration, and content previously loaded on the device.
- **Recommendation:** Define the minimum offline feature set, caching rules, content freshness expectations, and user messaging for stale or unavailable live data.

### Real-time update frequency requires stakeholder confirmation
- **Observation:** The live ticker is described as real time and continuously updated, but the source does not provide a numeric latency threshold. The requirement has therefore been rewritten without a numeric SLA.
- **Recommendation:** Confirm a stakeholder-approved service level for live match update latency if measurable performance targets are required.

### Transmission rights validation mechanism is unspecified
- **Observation:** The app must show live stream links only where rights are fulfilled in the country, but the source of rights data and the method for determining user country are not described.
- **Recommendation:** Clarify how geo-eligibility will be determined, which rights source is authoritative, and how the app should behave when rights data is unavailable or inconclusive.

### Notification event types and delivery rules need refinement
- **Observation:** Notifications are mentioned for news or results of favorite teams, but the exact event triggers, quiet hours, batching rules, and user opt-in granularity are not specified.
- **Recommendation:** Define notification categories, trigger conditions, timing expectations, opt-in levels, and platform-specific delivery constraints.

### Supported social media channels are not listed
- **Observation:** The app should support sharing via social media directly from the app, but no specific platforms or content formatting requirements are provided.
- **Recommendation:** Identify whether native OS sharing is sufficient or whether direct integrations with named social platforms are required.

### League and competition coverage boundaries are undefined
- **Observation:** The input references extensive national and international coverage, but does not identify mandatory leagues, competitions, data providers, or depth of coverage.
- **Recommendation:** Prioritize the initial list of leagues and competitions for MVP and define any phased expansion plan.

### GDPR compliance controls are high level only
- **Observation:** GDPR compliance is required, but the input does not specify consent management, privacy notice presentation, data retention, deletion requests, or data subject rights workflows. Current acceptance criteria therefore only cover observable in-app behaviors directly supported by the source context.
- **Recommendation:** Document detailed privacy requirements, lawful bases for processing, consent flows, retention periods, and user rights handling procedures.

---
## Summary Statistics

- **Total Discovered User Needs:** 8
- **Total Functional Requirements (FR):** 8
- **Total Non-Functional Requirements (NFR):** 5
- **Total User Stories (US):** 9
- **User Needs Coverage:** 8/8

### Priority Breakdown
- **High:** 17
- **Medium:** 5
- **Low:** 0
