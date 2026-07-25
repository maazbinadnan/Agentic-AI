# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-003, FR-004 | US-003, US-004 | News & Live Results |
| UN-002 | FR-001, FR-002, FR-003 | US-001, US-002, US-003 | Personalization |
| UN-003 | FR-004, FR-007 | US-004, US-007 | Notifications & Live Results |
| UN-004 | FR-006 | US-006 | Live Streaming |
| UN-005 | FR-005 | US-005 | Team & Player Info |
| UN-006 | FR-008 | US-008 | Social Sharing |
| UN-007 | NFR-001, NFR-002, NFR-006 | US-009 | Performance & Quality |
| UN-008 | FR-009, NFR-003, NFR-006, NFR-007 | US-010 | Reliability & Offline |
| UN-009 | FR-001, NFR-004 | US-011 | Data Protection |
| UN-010 | NFR-005 | US-012 | Platform Availability |

---
## Gaps & BA Recommendations

### Details of Authentication Process
- **Observation:** The requirements specify 'uncomplicated' registration and login but do not clarify if third-party authentication (e.g., Google, Apple, Facebook) is supported or if only email/password is allowed.
- **Recommendation:** Clarify which authentication methods are required or permitted for user registration and login.

### Personalization Data Scope
- **Observation:** It is not specified whether users can select multiple favorite teams and channels, or if there are limits.
- **Recommendation:** Define the allowed number of favorite teams and channels a user can select.

### Notification Preferences Granularity
- **Observation:** The requirements do not specify if users can customize which types of notifications (e.g., news, results, live events) they receive.
- **Recommendation:** Clarify the level of granularity for notification preferences.

### Offline Functionality Scope
- **Observation:** It is unclear which features and data are available offline (e.g., cached news, results, team info) and for how long.
- **Recommendation:** Specify which modules and data are accessible offline and the caching policy.

### Live Stream Rights Enforcement
- **Observation:** The mechanism for determining and enforcing live stream rights by country is not described.
- **Recommendation:** Detail how the app will verify and enforce live stream rights per country.

### User Feedback and Support Channels
- **Observation:** While user feedback is mentioned, the method for collecting and processing feedback (e.g., in-app form, app store reviews) is not specified.
- **Recommendation:** Define the channels and processes for collecting user feedback and support requests.

---
## Summary Statistics

- **Total Discovered User Needs:** 10
- **Total Functional Requirements (FR):** 9
- **Total Non-Functional Requirements (NFR):** 7
- **Total User Stories (US):** 12
- **User Needs Coverage:** 10/10

### Priority Breakdown
- **High:** 23
- **Medium:** 4
- **Low:** 0
