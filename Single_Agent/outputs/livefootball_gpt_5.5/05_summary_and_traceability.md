# 5. Requirements Analysis & Summary

## Traceability Matrix

| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |
|---|---|---|---|
| UN-001 | FR-001; NFR-001, NFR-002, NFR-011 | US-001 | App Startup & Cross-Platform Experience |
| UN-002 | FR-002 | US-002, US-015 | Authentication |
| UN-003 | FR-003, FR-004, FR-016 | US-003, US-004, US-012 | Personalization |
| UN-004 | FR-004, FR-005, FR-006 | US-004, US-005, US-006 | News |
| UN-005 | FR-007, FR-008, FR-009; NFR-009, NFR-010 | US-007, US-018 | Live Ticker |
| UN-006 | FR-010 | US-008 | League & Competition Coverage |
| UN-007 | FR-011, FR-012 | US-009, US-010 | Team & Player Profiles |
| UN-008 | FR-013, FR-014, FR-015 | US-011 | Legal Live Stream Access |
| UN-009 | FR-016, FR-017 | US-012, US-013 | Notifications |
| UN-010 | FR-006, FR-018 | US-006 | Social Sharing |
| UN-011 | FR-009, FR-019; NFR-005, NFR-006 | US-001, US-007, US-014 | Offline & Network Resilience |
| UN-012 | FR-002, FR-014; NFR-007, NFR-008, NFR-011, NFR-012 | US-011, US-015, US-017 | Privacy, Security & Compliance |
| UN-013 | FR-020; NFR-003, NFR-004, NFR-009, NFR-012 | US-016, US-017, US-018 | Scalability, Support & Quality |

---
## Gaps & BA Recommendations

### External API Contract and Data Ownership
- **Observation:** The source document states that live data is retrieved from an external server but does not define provider identity, data schema, API limits, uptime, or permitted caching.
- **Recommendation:** Establish formal API contracts including endpoints, authentication, rate limits, retry behavior, schema versioning, data latency, and outage escalation procedures.

### Live-Stream Rights Determination
- **Observation:** Rights compliance is required, but the country detection method, legal data source, provider deeplink behavior, and edge cases such as VPN or travel are unspecified.
- **Recommendation:** Define a rights-rule service using provider metadata, user location/country settings, broadcast status, and auditable decision logs reviewed by legal stakeholders.

### Authentication Scope
- **Observation:** Registration and login are described as uncomplicated, but required authentication methods are not specified.
- **Recommendation:** Confirm whether MVP supports email/password only, Apple Sign-In, Google Sign-In, guest mode, password reset, multi-factor authentication, and account deletion.

### Offline Mode Boundaries
- **Observation:** The app must remain usable offline, but the exact content cache scope and retention duration are unclear.
- **Recommendation:** Define offline content rules for favorites, news summaries, profiles, results, images, and live ticker last-known state, including cache expiry and storage limits.

### Notification Taxonomy
- **Observation:** Notifications are required for current events, news, and results, but detailed categories and frequency controls are missing.
- **Recommendation:** Define notification categories such as kickoff, goal, red card, halftime, full-time, lineup, breaking news, transfer news, and quiet-hours settings.

### Supported Regions and Languages
- **Observation:** National and international coverage is requested, but launch countries and languages are not listed.
- **Recommendation:** Confirm launch markets, localization needs, timezone handling, league names, country-specific content restrictions, and right-to-left language requirements if applicable.

### Performance Test Definition
- **Observation:** The system must serve 100,000 simultaneous users without performance loss, but success metrics are not measurable beyond the concurrency count.
- **Recommendation:** Define target response times, error rates, throughput, load-test scenarios, device models, network profiles, and pass/fail thresholds.

### GDPR Operational Controls
- **Observation:** GDPR compliance is stated, but user rights workflows are not elaborated.
- **Recommendation:** Implement explicit privacy notice, consent records, data export, account deletion, retention policy, processor register, breach response, and data protection impact assessment.

---
## Summary Statistics

- **Total Discovered User Needs:** 13
- **Total Functional Requirements (FR):** 20
- **Total Non-Functional Requirements (NFR):** 12
- **Total User Stories (US):** 18
- **User Needs Coverage:** 13/13

### Priority Breakdown
- **High:** 42
- **Medium:** 21
- **Low:** 0
