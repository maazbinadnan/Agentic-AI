# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003 | US-002 | News & Live Results |
| UN-002 | FR-001 | US-001 | Personalization |
| UN-003 | FR-006 | US-003 | Notifications |
| UN-004 | FR-005 | US-004 | Live Streaming |
| UN-005 | FR-004 | US-005 | Team & Player Info |
| UN-006 | FR-007 | US-006 | Social Sharing |
| UN-007 | NFR-001 | US-007 | Performance |
| UN-008 | FR-009, NFR-003 | US-008 | Reliability & Offline |
| UN-009 | NFR-004 | US-009 | Security & Compliance |
| UN-010 | NFR-002, NFR-005, NFR-006 |  | Scalability & Quality |
| UN-011 | FR-010 | US-011 | Platform Support |
| UN-012 | FR-008 | US-010 | Authentication |

---
## Gaps & BA Recommendations

### Offline Data Scope
- **Observation:** The requirements specify offline usability but do not clarify which features or data are available offline (e.g., live ticker, notifications, or only cached news/results).
- **Recommendation:** Clarify with stakeholders which modules and data types must be accessible offline and how often offline data should be refreshed.

### Personalization Data Storage
- **Observation:** It is not specified whether user preferences (favorite teams, channels) are stored locally, in the cloud, or both.
- **Recommendation:** Confirm with stakeholders where and how personalization data should be stored and synchronized across devices.

### Registration and Login Methods
- **Observation:** The requirements mention uncomplicated registration and login but do not specify supported methods (e.g., email, social login, SSO).
- **Recommendation:** Define which authentication methods are required for MVP and future releases.

### Notification Preferences Granularity
- **Observation:** It is unclear if users can configure notification types (e.g., only goals, only news, all events) or if notifications are all-or-nothing.
- **Recommendation:** Clarify the level of granularity required for notification preferences.

### Live Stream Rights Management
- **Observation:** The mechanism for determining and enforcing live stream rights by country is not detailed.
- **Recommendation:** Specify how the app will check and enforce transmission rights for live streams per user location.

### User Feedback Channels
- **Observation:** Continuous evaluation of user feedback is mentioned, but the channels (in-app, app store, email) are not specified.
- **Recommendation:** Define which feedback channels will be monitored and how feedback will be collected and processed.

---
## Summary Statistics

- **Total Discovered User Needs:** 12
- **Total Functional Requirements (FR):** 10
- **Total Non-Functional Requirements (NFR):** 6
- **Total User Stories (US):** 11
- **User Needs Coverage:** 12/12

### Priority Breakdown
- **High:** 22
- **Medium:** 6
- **Low:** 0
