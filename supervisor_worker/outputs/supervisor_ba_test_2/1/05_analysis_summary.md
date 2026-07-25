# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001, NFR-001, NFR-004 | US-001 | App Performance & Content Delivery |
| UN-002 | FR-002, FR-003 | US-002, US-003 | Personalization & Notifications |
| UN-003 | FR-003 | US-003 | Notifications |
| UN-004 | FR-004, NFR-006 | US-004 | Live Streaming & Compliance |
| UN-005 | FR-005 | US-005 | Social Sharing |
| UN-006 | FR-006, NFR-005 | US-006 | Offline Access & Reliability |
| UN-007 | FR-007, NFR-002 | US-007 | Scalability & Performance |
| UN-008 | FR-008, NFR-003 | US-008 | Data Protection & Compliance |
| UN-009 | FR-009 | US-009 | User Registration & Login |
| UN-010 | FR-010 | US-010 | Quality Assurance & Continuous Improvement |
| UN-011 | FR-011 | US-011 | Localization |
| UN-012 | FR-006 | US-006 | Offline Access |
| UN-013 | FR-012 | US-012 | Live Streaming Integration |

---
## Gaps & BA Recommendations

### Offline Data Update Mechanism
- **Observation:** While the app caches news, scores, and team/player info for up to 7 days, it is unclear how and when the cache is refreshed or invalidated if the user is online.
- **Recommendation:** Specify the cache refresh policy and whether users can manually refresh cached data when online.

### Notification Granularity
- **Observation:** Notification preferences are now included, but the specific types (e.g., goals, cards, match start/end, news, transfers) are not detailed.
- **Recommendation:** Define the available notification types users can select for their favorite teams.

### Live Stream Player Capabilities
- **Observation:** The requirement specifies in-app browser or native player, but does not clarify if features like Chromecast, AirPlay, or picture-in-picture are required.
- **Recommendation:** Clarify if advanced playback features (e.g., casting, PiP) are in scope for the live stream player.

### User Feedback Channels
- **Observation:** Continuous improvement is based on user feedback, but the mechanisms for collecting feedback (in-app form, app store reviews, etc.) are not specified.
- **Recommendation:** Define the channels through which user feedback will be collected and prioritized.

---
## Summary Statistics

- **Total Discovered User Needs:** 13
- **Total Functional Requirements (FR):** 12
- **Total Non-Functional Requirements (NFR):** 6
- **Total User Stories (US):** 12
- **User Needs Coverage:** 13/13

### Priority Breakdown
- **High:** 18
- **Medium:** 6
- **Low:** 0
