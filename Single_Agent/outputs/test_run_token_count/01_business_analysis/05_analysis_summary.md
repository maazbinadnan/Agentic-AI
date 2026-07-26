# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003 | US-002, US-003 | News & Live Results |
| UN-002 | FR-001, FR-010 | US-001, US-010 | Personalization |
| UN-003 | FR-004 | US-004 | Notifications |
| UN-004 | FR-005 | US-005 | Live Streams |
| UN-005 | FR-006 | US-006 | Team & Player Info |
| UN-006 | FR-007 | US-007 | Social Sharing |
| UN-007 | FR-009, NFR-001, NFR-002 | US-009 | Performance & Interface |
| UN-008 | NFR-003 |  | Reliability & Offline |
| UN-009 | NFR-004 |  | Data Protection |
| UN-010 | FR-008 | US-008 | Authentication |
| UN-011 | NFR-005 |  | Platform Availability |
| UN-012 | NFR-006 |  | Testing & Support |
| UN-013 | NFR-007 |  | Continuous Improvement |

---
## Gaps & BA Recommendations

### Live Stream Rights Verification
- **Observation:** The process for verifying transmission rights for live streams in each country is not specified.
- **Recommendation:** Clarify how the app will determine if live stream rights are fulfilled for a user's location (e.g., via IP geolocation, provider API, or user input).

### Offline Data Scope
- **Observation:** It is unclear which data and features are available offline and how long cached data is retained.
- **Recommendation:** Specify which modules (e.g., news, live ticker, team info) are accessible offline and define cache expiration policies.

### User Registration Methods
- **Observation:** The supported registration and login methods (e.g., email, social login, SSO) are not detailed.
- **Recommendation:** Define which authentication methods are supported for registration and login.

### Notification Preferences Granularity
- **Observation:** The level of granularity for notification preferences (e.g., per team, per event type) is not described.
- **Recommendation:** Clarify if users can customize notification types and for which teams or events.

### User Feedback Mechanism
- **Observation:** The mechanism for collecting and evaluating user feedback and app reviews is not specified.
- **Recommendation:** Describe how users can submit feedback (e.g., in-app form, app store reviews) and how it will be processed.

### Social Media Integration Scope
- **Observation:** The specific social media platforms supported for sharing are not listed.
- **Recommendation:** List the social media platforms (e.g., Facebook, Twitter, WhatsApp) that will be integrated for sharing.

---
## Summary Statistics

- **Total Discovered User Needs:** 13
- **Total Functional Requirements (FR):** 10
- **Total Non-Functional Requirements (NFR):** 7
- **Total User Stories (US):** 10
- **User Needs Coverage:** 13/13

### Priority Breakdown
- **High:** 21
- **Medium:** 5
- **Low:** 1
