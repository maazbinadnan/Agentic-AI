# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-002, FR-003 | US-002, US-003 | Personalized News & Live Results |
| UN-002 | FR-001 | US-001 | Personalization |
| UN-003 | FR-005 | US-005 | Live Streaming |
| UN-004 | FR-007 | US-007 | Notifications |
| UN-005 | FR-008 | US-008 | Social Sharing |
| UN-006 | NFR-001, FR-010 | US-010, US-015 | Performance |
| UN-007 | FR-004 | US-004 | Team & Player Info |
| UN-008 | FR-009, NFR-003 | US-009, US-012 | Offline Usability |
| UN-009 | FR-006, NFR-004 | US-006, US-013 | Security & Privacy |
| UN-010 | NFR-005 | US-014 | Reliability |
| UN-011 | NFR-002 | US-011 | Scalability |

---
## Gaps & BA Recommendations

### Offline Data Scope and Update Policy
- **Observation:** Offline data is now defined as news, results, and team/player information. The cache is updated every 24 hours and expires after 48 hours.
- **Recommendation:** Ensure implementation of cache refresh and expiration logic as specified.

### Details of Supported Social Media Platforms
- **Observation:** The requirements now specify Facebook, Twitter, and WhatsApp as supported platforms for sharing.
- **Recommendation:** Confirm if additional platforms are required in future releases.

### User Registration Methods
- **Observation:** Registration and login now support both email/password and third-party logins (Google, Apple).
- **Recommendation:** Verify compliance with Google and Apple sign-in guidelines.

### Notification Granularity
- **Observation:** Users can now select notification types (e.g., goals, news, match start) and set notification frequency.
- **Recommendation:** Ensure UI supports granular notification settings.

### Live Stream Rights Management
- **Observation:** Live stream rights are enforced using geo-IP lookup or a rights API.
- **Recommendation:** Confirm technical feasibility and legal compliance of the chosen enforcement method.

### Device and OS Version Support
- **Observation:** The app now supports Android 10+ and iOS 13+ devices.
- **Recommendation:** Monitor market share and update minimum requirements as needed.

---
## Summary Statistics

- **Total Discovered User Needs:** 11
- **Total Functional Requirements (FR):** 10
- **Total Non-Functional Requirements (NFR):** 5
- **Total User Stories (US):** 15
- **User Needs Coverage:** 11/11

### Priority Breakdown
- **High:** 23
- **Medium:** 3
- **Low:** 0
