# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003 | US-002, US-003 | News & Live Results |
| UN-002 | FR-001 | US-001 | Personalization |
| UN-003 | FR-006 | US-006 | Notifications |
| UN-004 | FR-005 | US-005 | Live Streams |
| UN-005 | FR-004 | US-004 | Team & Player Info |
| UN-006 | FR-007 | US-007 | Social Sharing |
| UN-007 | NFR-001, NFR-002 | US-009 | Performance |
| UN-008 | NFR-003, FR-009 | US-010 | Reliability & Offline |
| UN-009 | NFR-004 |  | Data Protection |
| UN-010 | FR-008 | US-008 | Authentication |
| UN-011 | NFR-005 |  | Platform Support |
| UN-012 | NFR-006 |  | Testing & Support |

---
## Gaps & BA Recommendations

### Details of Personalization Options
- **Observation:** The requirements specify that users can select favorite teams and sports channels, but do not clarify if users can change these preferences later or if there are limits to the number of favorites.
- **Recommendation:** Clarify whether users can update their preferences at any time and if there are any restrictions on the number of teams or channels that can be selected.

### Notification Preferences Granularity
- **Observation:** It is not specified whether users can customize which types of notifications they receive (e.g., only goals, only news, etc.).
- **Recommendation:** Define the level of granularity for notification preferences to ensure user control and avoid notification fatigue.

### Offline Functionality Scope
- **Observation:** The requirements state the app should be usable offline with cached content, but do not specify which features or data are available offline.
- **Recommendation:** Specify which modules and data (e.g., news, results, team info) are accessible offline and how often they are updated.

### Registration and Login Methods
- **Observation:** The requirements mention a simple registration and login process but do not specify supported authentication methods (e.g., email, social login, SSO).
- **Recommendation:** Clarify which authentication methods are supported and if there are any requirements for password complexity or two-factor authentication.

### Live Stream Rights Management
- **Observation:** The requirements state that live streams are only shown when rights are fulfilled in the user's country, but do not specify how the app determines user location or manages rights.
- **Recommendation:** Define the mechanism for determining user location (e.g., IP geolocation, device settings) and how rights management is enforced.

### Data Retention and User Deletion
- **Observation:** GDPR compliance is mentioned, but there are no details on data retention periods or user data deletion processes.
- **Recommendation:** Specify data retention policies and the process for users to request data deletion in compliance with GDPR.

---
## Summary Statistics

- **Total Discovered User Needs:** 12
- **Total Functional Requirements (FR):** 9
- **Total Non-Functional Requirements (NFR):** 6
- **Total User Stories (US):** 10
- **User Needs Coverage:** 12/12

### Priority Breakdown
- **High:** 17
- **Medium:** 5
- **Low:** 0
