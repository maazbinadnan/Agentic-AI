# 04_non_functional_requirements.md

## Section 1: Quality Attributes & Technical Scope

The LiveFootball app is a free, account-based mobile platform for football fans, available on Android and iOS. The technical scope covers all user-facing modules (news, live ticker, notifications, personalization, social sharing), the user interface, backend integrations (APIs, notification system), and compliance with privacy and transmission rights. The app excludes administrative roles, paid features, and non-football content.

**Key Quality Attributes:**
- **Performance & Latency:** Fast app startup, real-time data updates, responsive UI.
- **Scalability & Concurrency:** High concurrent user support, robust under peak loads.
- **Security & Compliance:** Secure authentication, GDPR-compliant data processing, transmission rights enforcement.
- **Reliability & Availability:** Consistent operation, offline usability, resilience to network issues.
- **Maintainability & Observability:** Structured logging, monitoring, user feedback integration.

---

## Section 2: Non-Functional Requirements Matrix

| ID        | Requirement                                                                                  | Quality Attribute         | Rationale / Source                |
|-----------|----------------------------------------------------------------------------------------------|--------------------------|-----------------------------------|
| NFR-001   | The app must fully load and be ready for user interaction within 2 seconds of startup.        | Performance & Latency    | UN-012, Operational Req           |
| NFR-002   | The app must display live ticker updates with a maximum latency of 1 second from API receipt. | Performance & Latency    | UN-004, Operational Req           |
| NFR-003   | The app must support at least 100,000 concurrent active users without performance degradation.| Scalability & Concurrency| UN-018, Operational Req           |
| NFR-004   | The app must maintain a minimum uptime of 99.9% per calendar month.                          | Reliability & Availability| Operational Req                   |
| NFR-005   | The app must remain usable offline, providing access to previously loaded data and UI.        | Reliability & Availability| UN-017, Operational Req           |
| NFR-006   | The app must function reliably with network latency up to 500ms and intermittent connectivity.| Reliability & Availability| UN-016, Operational Req           |
| NFR-007   | All user authentication and registration must use secure protocols (e.g., OAuth 2.0, TLS 1.2+).| Security & Compliance    | UN-001, UN-002, Stakeholder Q&A   |
| NFR-008   | All personal data must be processed and stored in compliance with GDPR.                      | Security & Compliance    | UN-019, Operational Req           |
| NFR-009   | Live stream links must only be displayed when transmission rights are fulfilled for the user's country.| Security & Compliance    | UN-011, Operational Req           |
| NFR-010   | All sensitive data at rest and in transit must be encrypted using AES-256 and TLS 1.2+.      | Security & Compliance    | Security Best Practice            |
| NFR-011   | The app must provide structured logging for all critical operations and errors.               | Maintainability & Observability| Operational Req, Support         |
| NFR-012   | The app must expose monitoring metrics (e.g., API response times, user activity, error rates).| Maintainability & Observability| Operational Req                  |
| NFR-013   | The app must provide a feedback mechanism for users to report issues and suggestions.         | Maintainability & Observability| UN-020, Operational Req           |
| NFR-014   | The app must undergo automated regression, performance, and security testing before each release.| Maintainability & Observability| Operational Req                  |

---

## Section 3: Verification Methods & Compliance SLAs

| NFR ID    | Verification Method                          | Compliance SLA / Metric                |
|-----------|----------------------------------------------|----------------------------------------|
| NFR-001   | Automated performance tests, manual stopwatch| ≥95% of launches <2s                   |
| NFR-002   | API latency monitoring, real-time test cases | ≥99% updates <1s latency               |
| NFR-003   | Load testing, cloud scaling simulations      | ≥100,000 concurrent users, <5% error rate|
| NFR-004   | Uptime monitoring, incident logs             | ≥99.9% uptime/month                    |
| NFR-005   | Offline usability tests, UI review           | Core features accessible offline       |
| NFR-006   | Network simulation tests                     | No critical failures at 500ms latency  |
| NFR-007   | Security audit, protocol inspection          | 100% secure auth flows                 |
| NFR-008   | GDPR compliance audit, privacy policy review | 100% compliance, no violations         |
| NFR-009   | Geo-rights validation, country-based tests   | 100% legal stream display              |
| NFR-010   | Encryption audit, penetration testing        | 100% AES-256/TLS 1.2+ coverage         |
| NFR-011   | Log review, structured log format check      | 100% critical ops logged               |
| NFR-012   | Monitoring dashboard, metric review          | Metrics available for all modules      |
| NFR-013   | UI review, feedback form test                | Feedback accessible to all users       |
| NFR-014   | CI/CD pipeline test reports                  | 100% test coverage pre-release         |

---

**End of Document**
