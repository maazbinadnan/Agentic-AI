## Business Analysis & Requirements Specification

### 5. Requirements & Story Traceability Matrix

| User Need ID | Derived Requirement IDs | Mapped User Story IDs | Primary Domain Area |
|--------------|-------------------------|-----------------------|---------------------|
| UN-001 | FR-001, FR-012, NFR-001, NFR-005 | US-001, US-011 | Platform / UI |
| UN-002 | FR-002, FR-003, FR-008 | US-002, US-003, US-007 | Personalization / News |
| UN-003 | FR-004, FR-012, NFR-002, NFR-005 | US-004, US-011 | Live Ticker |
| UN-004 | FR-005 | US-005 | Content Coverage |
| UN-005 | FR-006 | US-006 | Streaming Links |
| UN-006 | FR-006, FR-007, NFR-008 | US-006 | Rights Compliance |
| UN-007 | FR-008, FR-012 | US-007, US-011 | Notifications |
| UN-008 | FR-009 | US-008 | Authentication |
| UN-009 | FR-010 | US-009 | Social Sharing |
| UN-010 | FR-011, NFR-003, NFR-004 | US-010 | Reliability / Scalability |
| UN-011 | FR-014, NFR-006 | US-013 | Privacy / Compliance |
| UN-012 | FR-013, NFR-007 | US-012 | Support / Improvement |

### 6. Gaps & BA Recommendations

- **Default News Feed Rules:** The raw input does not define what content should be shown before a user selects favorite teams or preferred channels. Confirm default news feed behavior.
- **Notification Event Scope:** The exact event triggers, notification categories, delivery timing, and user preference granularity are not specified. Define notification business rules.
- **Authentication Method:** Registration and login are required, but supported methods (email/password, social login, OTP, etc.) are not stated. Confirm the authentication approach.
- **Offline Feature Scope:** The input states the app remains usable offline, but it does not define which features are supported offline versus online only. Clarify the offline capability matrix.
- **Streaming Provider Integration:** DAZN and Sky Sport are examples only. Confirm the definitive provider list, deep-link behavior, and fallback handling when a provider app is not installed.
- **Rights Determination Logic:** The method used to determine the user’s country and rights eligibility is not specified. Confirm geo-detection and compliance validation rules.
- **Real-Time SLA Definition:** “Real time” is stated, but no measurable refresh interval or acceptable latency from API receipt to UI display is given. Define a measurable live update SLA.
- **Supported Social Platforms:** The required social media platforms and content formatting rules are not listed. Confirm the supported sharing targets.
- **Feedback Collection Mechanism:** The raw input mentions continuous evaluation of user feedback and app reviews, but not whether feedback is collected in-app, from app stores, or via external tools. Clarify scope.
- **Performance Baseline for Peak Load:** The statement “without performance loss” lacks measurable service baselines such as response time, update latency, and error rate under 100,000 concurrent users. Define the baseline metrics.
- **GDPR Control Detail:** GDPR compliance is required, but no detail is provided for consent management, retention, data subject rights, or lawful basis. Elicit explicit privacy requirements.
- **Mockups and UI Specification Request:** HTML mockups were requested by the user, but the source document does not contain sufficient UI layout, branding, navigation, or interaction detail to derive validated mockups without assumptions. Provide low-fidelity concept only if explicitly accepted as assumption-based.

### 7. Summary Statistics

- **Total Discovered User Needs:** 12
- **Total Functional Requirements (FR):** 14
- **Total Non-Functional Requirements (NFR):** 8
- **Total User Stories (US):** 13
- **Priority Breakdown:**
  - Must Have: 9
  - Should Have: 4
  - Could Have: 1
  - Won't Have: 0
- **User Needs Coverage:** 12 / 12

### Additional Note on HTML Mockups

The request asked for “html mockups and everything.” As a business analyst, I have produced the in-scope requirements deliverables grounded strictly in the supplied raw document. Because the brief does not specify screen layouts, branding, navigation hierarchy, component states, or interaction rules in enough detail, production-quality mockups cannot be derived without introducing unsupported assumptions. If desired, a separate assumption-based low-fidelity mockup pack can be created in a subsequent iteration after stakeholder confirmation of the information architecture and UI expectations.