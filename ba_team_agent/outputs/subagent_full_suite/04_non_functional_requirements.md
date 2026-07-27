# 04_non_functional_requirements.md

## Section 1: Quality Attributes & Technical Scope

The LiveFootball mobile app is designed for Android and iOS platforms, serving as a central hub for football fans to access real-time news, live scores, team/player information, and live stream links. The technical scope encompasses:
- High-performance mobile UI and backend integration for live data and notifications
- Support for up to 100,000 concurrent users
- Robust offline and limited network operation
- Secure, GDPR-compliant user data processing
- Dynamic integration of live stream links with transmission rights enforcement
- Continuous improvement via user feedback and app reviews

**Key Quality Attributes:**
- Performance & Latency
- Scalability & Concurrency
- Security & Compliance
- Reliability & Availability
- Maintainability & Observability

## Section 2: Non-Functional Requirements Matrix

| ID        | Quality Attribute         | Requirement Description                                                                 | Target/Constraint                  |
|-----------|--------------------------|-----------------------------------------------------------------------------------------|------------------------------------|
| NFR-001   | Performance & Latency    | App must fully load and be ready for user interaction within 2 seconds of launch.        | ≤ 2 seconds (cold start)           |
| NFR-002   | Performance & Latency    | Live ticker updates must display new match data within 1 second of API receipt.          | ≤ 1 second update latency          |
| NFR-003   | Performance & Latency    | Notification delivery for live events must occur within 3 seconds of event trigger.      | ≤ 3 seconds                        |
| NFR-004   | Scalability & Concurrency| App backend must support 100,000 concurrent active users without performance degradation.| 100,000 concurrent users           |
| NFR-005   | Scalability & Concurrency| App must handle peak match-day traffic with no more than 1% error rate.                  | ≤ 1% error rate at peak load       |
| NFR-006   | Reliability & Availability| App must maintain 99.9% uptime (monthly) including during high-traffic events.           | ≥ 99.9% uptime SLA                 |
| NFR-007   | Reliability & Availability| App must remain usable offline for core features (news, scores, preferences).            | Offline usability for core features |
| NFR-008   | Reliability & Availability| App must function reliably with network latency up to 500ms and packet loss up to 5%.    | Operable under poor network         |
| NFR-009   | Security & Compliance    | All user data must be encrypted in transit (TLS 1.2+) and at rest (AES-256).             | TLS 1.2+, AES-256                  |
| NFR-010   | Security & Compliance    | App must enforce GDPR-compliant data processing and user consent management.              | GDPR compliance                    |
| NFR-011   | Security & Compliance    | Live stream links must only be shown when transmission rights are fulfilled per country.  | Rights enforcement per country      |
| NFR-012   | Security & Compliance    | Registration and login must use secure authentication (OAuth 2.0 or equivalent).         | OAuth 2.0 or equivalent            |
| NFR-013   | Maintainability & Observability| App must provide structured logging for all critical events and errors.             | Structured logs (JSON/ELK)         |
| NFR-014   | Maintainability & Observability| App must expose monitoring metrics (CPU, memory, API latency, error rates).         | Metrics via monitoring platform     |
| NFR-015   | Maintainability & Observability| App must support automated crash reporting and feedback collection.                  | Crash/feedback automation           |

## Section 3: Verification Methods & Compliance SLAs

| NFR ID    | Verification Method                  | Compliance SLA / Metric                |
|-----------|-------------------------------------|----------------------------------------|
| NFR-001   | Performance testing (Appium, XCUITest) | ≥ 95% launches ≤ 2s (monthly)          |
| NFR-002   | API latency monitoring, UI tests     | ≥ 99% updates ≤ 1s                     |
| NFR-003   | Notification delivery tests          | ≥ 98% notifications ≤ 3s               |
| NFR-004   | Load testing (JMeter, Locust)        | 100,000 concurrent users, ≤ 1% errors  |
| NFR-005   | Load testing, error rate monitoring  | ≤ 1% error rate at peak                |
| NFR-006   | Uptime monitoring (Pingdom, CloudWatch)| ≥ 99.9% uptime (monthly)              |
| NFR-007   | Offline usability tests              | Core features available offline         |
| NFR-008   | Network simulation tests             | Operable at 500ms latency, 5% loss     |
| NFR-009   | Security audit, encryption checks    | TLS 1.2+, AES-256 verified             |
| NFR-010   | GDPR audit, consent flow review      | 100% compliance                        |
| NFR-011   | Rights enforcement tests, geo checks | 100% compliance per country            |
| NFR-012   | Authentication penetration tests     | OAuth 2.0/equivalent verified          |
| NFR-013   | Log review, structured log validation| 100% critical events logged            |
| NFR-014   | Monitoring platform integration test | Metrics available, real-time           |
| NFR-015   | Crash/feedback system test           | Automated reporting enabled            |

---

**End of Document**
