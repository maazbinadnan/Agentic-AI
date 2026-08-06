## Business Analysis & Requirements Specification

### 5. Requirements & Story Traceability Matrix

| User Need ID | Derived Requirement IDs | Mapped User Story IDs | Primary Domain Area |
|--------------|-------------------------|-----------------------|---------------------|
| UN-001 | FR-001, NFR-001, NFR-005 | US-001 | App Access |
| UN-002 | FR-003, FR-004 | US-003, US-004 | Personalization and News |
| UN-003 | FR-005, NFR-002 | US-005 | Live Ticker |
| UN-004 | FR-006 | US-006 | Football Information |
| UN-005 | FR-007, NFR-007 | US-007 | Streaming |
| UN-006 | FR-001, FR-002 | US-002 | Authentication |
| UN-007 | FR-003, FR-008, FR-009, NFR-006 | US-003, US-008, US-009 | Personalization |
| UN-008 | FR-010 | US-010 | Social Sharing |
| UN-009 | FR-011, NFR-003 | US-011 | Offline Reliability |
| UN-010 | NFR-004 | None | Scalability |
| UN-011 | FR-005, FR-009, NFR-002 | US-005, US-009 | Notifications and Live Updates |
| UN-012 | NFR-008 | None | Privacy and Compliance |
| UN-013 | FR-012, NFR-009 | US-012 | Quality and Support |

### 6. Gaps & BA Recommendations

- **Account Registration Data Fields Not Defined:** The raw input states that registration and login should be uncomplicated, but it does not define required registration fields, identity verification rules, password policy, or social sign-in options. Stakeholders should confirm the minimum account data set and authentication method.
- **Notification Trigger Rules Not Defined:** The input mentions notifications for news and results of favorite teams, but it does not specify which event types should trigger notifications, delivery timing, frequency limits, or quiet hours. These rules should be defined before implementation.
- **Offline Scope Not Defined:** The input states that the app remains usable offline, but it does not specify which content must be cached and what actions must remain available without connectivity. Stakeholders should define the minimum offline content set and expected user experience.
- **Live Ticker Refresh Intervals Not Quantified:** The requirement for real-time updates is clear, but the acceptable polling or push interval is not specified. Technical and business stakeholders should agree on refresh frequency and latency targets.
- **Preferred Sports Channels Model Not Defined:** The concept of selecting preferred sports channels is mentioned, but the list of supported channels, content licensing model, and filtering behavior are not specified.
- **Live Stream Provider Integration Scope Not Defined:** DAZN and Sky Sport are given as examples, but the actual supported provider list, integration mechanism, and link sourcing rules are not defined.
- **Country Determination for Rights Compliance Not Defined:** The app must display streams only where rights are fulfilled, but the method for determining a user’s country is not specified. Stakeholders should define whether country is inferred by device locale, IP geolocation, account profile, or another method.
- **Social Media Platforms Not Defined:** The raw input requires direct social sharing but does not specify which platforms are in scope or whether native share sheets are acceptable.
- **Support and Feedback Workflow Not Defined:** The input states that feedback and app reviews are evaluated continuously, but it does not specify whether this requires an internal admin function, external review aggregation, or a manual business process.
- **Performance Loss Threshold Not Defined for Peak Load:** The app must serve 100,000 concurrent users without performance loss, but measurable service level thresholds for acceptable response times under load are not specified.

### 7. Summary Statistics

- **Total Discovered User Needs:** 13
- **Total Functional Requirements (FR):** 12
- **Total Non-Functional Requirements (NFR):** 9
- **Total User Stories (US):** 12
- **Priority Breakdown:**
  - Must Have: 7
  - Should Have: 4
  - Could Have: 1
  - Won't Have: 0
- **User Needs Coverage:** 13 / 13
