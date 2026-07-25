# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, FR-006 | US-001, US-012 | Football Content & Live Data |
| UN-002 | FR-002, FR-007 | US-002, US-010 | Personalization & User Management |
| UN-003 | FR-003 | US-003 | Notifications |
| UN-004 | FR-004 | US-004 | Live Streaming |
| UN-005 | FR-005 | US-005 | Social Sharing |
| UN-006 | NFR-001 | US-006 | Performance |
| UN-007 | NFR-002 | US-007 | Reliability & Offline |
| UN-008 | NFR-003 | US-008 | Security & Compliance |
| UN-009 | NFR-004 | US-009 | Scalability |
| UN-010 | NFR-005, NFR-006 |  | Support & Quality |
| UN-011 | FR-008 | US-011 | Personalization & UI |

---
## Gaps & BA Recommendations

### Offline Data Expiry and Storage Limits
- **Observation:** While offline access to cached news, scores, and team info is specified, there is no detail on how long cached data is retained, how much storage is allocated, or how users are notified of stale data.
- **Recommendation:** Define cache expiry policy, storage limits for offline data, and user messaging for outdated content.

### Live Stream Provider Authentication Flows
- **Observation:** The requirements specify prompting for provider authentication if required, but do not detail the supported authentication flows or error handling if authentication fails.
- **Recommendation:** Clarify supported authentication flows for DAZN, Sky Sport, etc., and specify user experience for failed authentication.

### Widget and Theme Customization Scope
- **Observation:** Personalization now includes widgets and themes, but the types, limits, and supported customizations are not detailed.
- **Recommendation:** List available widgets, theme options, and any constraints on customization (e.g., number of widgets, color schemes).

---
## Summary Statistics

- **Total Discovered User Needs:** 11
- **Total Functional Requirements (FR):** 8
- **Total Non-Functional Requirements (NFR):** 6
- **Total User Stories (US):** 12
- **User Needs Coverage:** 11/11

### Priority Breakdown
- **High:** 18
- **Medium:** 4
- **Low:** 0
