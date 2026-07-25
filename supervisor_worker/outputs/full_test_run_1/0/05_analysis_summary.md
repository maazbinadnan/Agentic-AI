# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003 | US-002, US-003 | Personalized News & Live Results |
| UN-002 | FR-001 | US-001 | Personalization |
| UN-003 | FR-005 | US-005 | Live Streaming |
| UN-004 | FR-007 | US-007 | Notifications |
| UN-005 | FR-008 | US-008 | Social Sharing |
| UN-006 | NFR-001 |  | Performance |
| UN-007 | FR-004 | US-004 | Team & Player Info |
| UN-008 | FR-009, NFR-003 | US-009 | Offline Usability |
| UN-009 | FR-006, NFR-004 | US-006 | Security & Privacy |
| UN-010 | NFR-005 |  | Reliability |
| UN-011 | NFR-002 |  | Scalability |

---
## Gaps & BA Recommendations

### Details of Supported Social Media Platforms
- **Observation:** The requirements specify sharing news and reports via social media, but do not list which platforms are supported.
- **Recommendation:** Clarify which social media platforms (e.g., Facebook, Twitter, WhatsApp) should be integrated for sharing.

### Offline Data Scope and Update Policy
- **Observation:** It is unclear which data is available offline and how often offline content is updated or expired.
- **Recommendation:** Define the scope of offline data (e.g., news, results, team info) and the policy for cache refresh and expiration.

### User Registration Methods
- **Observation:** The registration process is described as 'uncomplicated' but does not specify if third-party logins (e.g., Google, Apple) are supported.
- **Recommendation:** Specify if social login or email/password registration is required, and if both are supported.

### Notification Granularity
- **Observation:** The requirements mention notifications for news and results but do not specify if users can select notification types or frequency.
- **Recommendation:** Clarify if users can customize notification types (e.g., only goals, only news) and set notification frequency.

### Live Stream Rights Management
- **Observation:** The mechanism for determining if live stream rights are fulfilled in a user's country is not described.
- **Recommendation:** Define how the app checks and enforces live stream rights by country (e.g., via API, geo-IP lookup).

### Device and OS Version Support
- **Observation:** The requirements do not specify the minimum supported Android and iOS versions or device types.
- **Recommendation:** Specify the minimum OS versions and device requirements for app compatibility.

---
## Summary Statistics

- **Total Discovered User Needs:** 11
- **Total Functional Requirements (FR):** 9
- **Total Non-Functional Requirements (NFR):** 5
- **Total User Stories (US):** 9
- **User Needs Coverage:** 11/11

### Priority Breakdown
- **High:** 20
- **Medium:** 3
- **Low:** 0
