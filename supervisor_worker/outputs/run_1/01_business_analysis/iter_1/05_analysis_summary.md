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
| UN-007 | NFR-001, NFR-002 | US-009, US-014 | Performance |
| UN-008 | NFR-003, FR-009, FR-010, FR-011 | US-010, US-011 | Reliability & Offline |
| UN-009 | NFR-004, FR-012 | US-012 | Data Protection |
| UN-010 | FR-008 | US-008 | Authentication |
| UN-011 | NFR-005 | US-013 | Platform Support |
| UN-012 | NFR-006 | US-015 | Testing & Support |

---
## Gaps & BA Recommendations

### Personalization Flexibility and Limits
- **Observation:** The requirements now specify that users can update their favorite teams and channels at any time, with explicit limits (10 teams, 5 channels).
- **Recommendation:** Confirm with stakeholders if these limits are appropriate and if users should be able to reorder or group favorites.

### Notification Preferences Granularity
- **Observation:** Notification types (goals, news, match start/end) are now selectable by users. However, the full list of notification types and default settings are not defined.
- **Recommendation:** Define the complete set of notification types and default notification settings for new users.

### Offline Functionality Scope
- **Observation:** Offline access is specified for news, results, and team/player info, with indication of offline status and last update time. Other modules (e.g., live streams, sharing) are not addressed.
- **Recommendation:** Clarify which additional features, if any, should be available offline and how often offline data is refreshed.

### Registration and Login Methods
- **Observation:** Supported authentication methods are now specified (email/password, Google, Apple, Facebook). Password complexity and two-factor authentication are not addressed.
- **Recommendation:** Define password complexity requirements and whether two-factor authentication is required or optional.

### Live Stream Rights Management
- **Observation:** User location for rights management is determined by IP geolocation. Handling of VPNs, proxies, or manual location override is not specified.
- **Recommendation:** Clarify how the system should handle users attempting to bypass location restrictions (e.g., via VPN) and whether manual override is permitted.

### Data Retention and User Deletion
- **Observation:** GDPR compliance now includes user-initiated data deletion. Data retention periods and backup deletion are not detailed.
- **Recommendation:** Specify data retention periods for inactive accounts and how deleted data is removed from backups in compliance with GDPR.

---
## Summary Statistics

- **Total Discovered User Needs:** 12
- **Total Functional Requirements (FR):** 12
- **Total Non-Functional Requirements (NFR):** 6
- **Total User Stories (US):** 15
- **User Needs Coverage:** 12/12

### Priority Breakdown
- **High:** 22
- **Medium:** 5
- **Low:** 0
