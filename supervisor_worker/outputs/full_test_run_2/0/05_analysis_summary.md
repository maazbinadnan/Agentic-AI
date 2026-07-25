# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003, FR-009 | US-002, US-003, US-009 | Content & Live Data |
| UN-002 | FR-001 | US-001 | Personalization |
| UN-003 | FR-004 | US-004 | Notifications |
| UN-004 | FR-005 | US-005 | Live Streaming |
| UN-005 | FR-006 | US-006 | Team & Player Info |
| UN-006 | FR-007 | US-007 | Social Sharing |
| UN-007 | FR-008 | US-008 | Authentication |
| UN-008 | NFR-001 |  | Performance |
| UN-009 | NFR-002 |  | Reliability |
| UN-010 | NFR-005 |  | Compliance |
| UN-011 | NFR-003, NFR-006, NFR-007 |  | Scalability & Quality |
| UN-012 | NFR-004 |  | Platform Support |

---
## Gaps & BA Recommendations

### Offline Data Scope
- **Observation:** The requirements specify offline usability but do not clarify which features or data are available offline (e.g., cached news, live ticker, team info).
- **Recommendation:** Clarify with stakeholders which modules and data should be accessible offline and how often offline data should be refreshed.

### Personalization Data Storage
- **Observation:** It is unclear whether user preferences (favorite teams, channels) are stored locally, in the cloud, or both.
- **Recommendation:** Specify the storage mechanism for personalization data and whether it syncs across devices.

### Notification Preferences Granularity
- **Observation:** The level of granularity for notification preferences (e.g., news only, results only, all events) is not defined.
- **Recommendation:** Define the types and granularity of notifications users can enable or disable.

### Social Media Integration Scope
- **Observation:** The specific social media platforms supported for sharing are not listed.
- **Recommendation:** Confirm which social media platforms (e.g., Facebook, Twitter, WhatsApp) should be integrated for sharing.

### User Registration Methods
- **Observation:** The requirements do not specify if third-party authentication (e.g., Google, Apple, Facebook) is supported.
- **Recommendation:** Clarify if social login or email/password registration is required, or both.

### Live Stream Provider Integration
- **Observation:** The process for updating or managing live stream provider links (e.g., DAZN, Sky Sport) is not described.
- **Recommendation:** Define how live stream links are sourced, updated, and managed in the app.

### GDPR User Rights Management
- **Observation:** While GDPR compliance is required, there is no detail on user rights management (e.g., data export, deletion requests).
- **Recommendation:** Specify which GDPR user rights (access, rectification, erasure, etc.) must be supported in the app.

---
## Summary Statistics

- **Total Discovered User Needs:** 12
- **Total Functional Requirements (FR):** 9
- **Total Non-Functional Requirements (NFR):** 7
- **Total User Stories (US):** 9
- **User Needs Coverage:** 12/12

### Priority Breakdown
- **High:** 20
- **Medium:** 4
- **Low:** 0
