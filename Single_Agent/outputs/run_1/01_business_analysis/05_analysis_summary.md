# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003 | US-002 | Personalized News & Live Results |
| UN-002 | FR-001, FR-002, FR-003 | US-001, US-002 | Personalization |
| UN-003 | FR-007 | US-005 | Notifications |
| UN-004 | FR-005 | US-004 | Live Streams |
| UN-005 | FR-004 | US-003 | Team & Player Info |
| UN-006 | FR-006 | US-006 | Social Sharing |
| UN-007 | NFR-001 | US-007 | Performance |
| UN-008 | NFR-002 | US-008 | Reliability & Offline |
| UN-009 | NFR-004 | US-009 | Security & Compliance |
| UN-010 | NFR-003 | US-010 | Scalability |
| UN-011 | FR-008 | US-011 | Authentication |
| UN-012 | NFR-005 |  | Quality Assurance |
| UN-013 | NFR-006 |  | Continuous Improvement |

---
## Gaps & BA Recommendations

### Offline Functionality Scope
- **Observation:** The requirements specify offline usability but do not detail which features (e.g., news, live ticker, team info) are available offline or how data is cached and updated.
- **Recommendation:** Clarify which modules and data are accessible offline and define cache update policies and user experience during offline periods.

### Notification Preferences Granularity
- **Observation:** It is unclear if users can customize notification types (e.g., only goals, only news, only match start/end) or if all notifications are bundled.
- **Recommendation:** Specify the level of granularity for notification preferences to ensure user control and avoid notification fatigue.

### Social Media Integration Scope
- **Observation:** The requirements mention sharing via social media but do not specify which platforms are supported or if deep linking is required.
- **Recommendation:** Define the list of supported social media platforms and whether native app integration or web sharing is required.

### User Registration Methods
- **Observation:** The registration process is described as uncomplicated but does not specify supported methods (e.g., email, phone, social login).
- **Recommendation:** Clarify which registration and login methods are supported to ensure alignment with user expectations and compliance.

### Live Stream Rights Management
- **Observation:** The mechanism for determining and enforcing transmission rights for live streams per country is not detailed.
- **Recommendation:** Specify how the app verifies and enforces country-specific transmission rights for live stream links.

### Data Retention and Deletion Policy
- **Observation:** GDPR compliance is required, but there is no detail on data retention periods, user data deletion, or data access requests.
- **Recommendation:** Define data retention, deletion, and user data access policies to ensure full GDPR compliance.

---
## Summary Statistics

- **Total Discovered User Needs:** 13
- **Total Functional Requirements (FR):** 8
- **Total Non-Functional Requirements (NFR):** 6
- **Total User Stories (US):** 11
- **User Needs Coverage:** 13/13

### Priority Breakdown
- **High:** 18
- **Medium:** 6
- **Low:** 0
