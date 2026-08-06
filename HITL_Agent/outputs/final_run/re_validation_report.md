# Requirements Engineering Validation Report

## 1. Executive Summary
- **Overall Validation Status**: NEEDS REVISION
- **Audit Date**: 2026-08-06
- **Deliverables Evaluated**:
  - [x] 01_elicitation_report.md
  - [x] 02_user_needs_report.md
  - [x] 03_functional_requirements.md
  - [x] 04_non_functional_requirements.md
  - [x] 05_user_stories.md

## 2. Requirements Traceability Matrix
| User Need ID | Functional Req ID | Non-Functional Req ID | User Story ID | Traceability Status |
|---|---|---|---|---|
| UN-001 | FR-001 | NFR-001 | US-001 | COMPLETE |
| UN-002 | FR-003, FR-005 | NFR-002 | US-003, US-005 | COMPLETE |
| UN-003 | FR-004, FR-005 | NFR-003 | US-004, US-005 | COMPLETE WITH WARNING |
| UN-004 | FR-008, FR-009 | NFR-004 | US-008, US-009 | COMPLETE WITH WARNING |
| UN-005 | FR-006 | NFR-005 | US-006 | COMPLETE WITH WARNING |
| UN-006 | FR-007 | NFR-006 | US-007 | COMPLETE WITH WARNING |
| UN-007 | FR-010 | NFR-007 | US-010 | COMPLETE WITH WARNING |
| UN-008 | FR-011 | NFR-008 | US-011 | COMPLETE WITH WARNING |
| UN-009 | FR-002 | NFR-009 | US-002 | COMPLETE |
| UN-010 | FR-004 | NFR-010 | US-004 | COMPLETE WITH WARNING |
| UN-011 | FR-012, FR-013 | NFR-011 | US-012, US-013 | COMPLETE WITH WARNING |
| UN-012 | FR-014 | NFR-012 | US-014 | COMPLETE WITH WARNING |
| UN-013 | FR-015 | - | US-015 | INCOMPLETE |
| UN-014 | FR-003, FR-018 | - | US-003, US-018 | INCOMPLETE |
| UN-015 | FR-016 | - | US-016 | INCOMPLETE |
| UN-016 | FR-017 | - | US-017 | INCOMPLETE |

## 3. Syntax & Quality Standard Compliance
- **"Shall" Syntax Compliance (FR/NFR)**: PASS - All functional and non-functional requirements use mandatory "shall" phrasing.
- **Measurable SLA Criteria (NFR)**: FAIL - Only NFR-001 contains a concrete measurable threshold. NFR-002, NFR-003, NFR-004, NFR-007, NFR-009, NFR-010, NFR-011, and NFR-012 use vague terms such as "real time," "usable," "without performance loss," "directly and consistently," "streamlined," "as soon as," and "thorough" without measurable acceptance thresholds. NFR-005 and NFR-006 are more testable policy/compliance constraints but still lack explicit verification criteria.
- **Agile User Story Phrasing (US)**: PASS - All user stories follow the "As a... I want to... so that..." structure.
- **Gherkin Acceptance Criteria (AC)**: PASS WITH WARNINGS - Every user story includes at least 2 scenarios with Given/When/Then structure. However, many Then statements use requirement language ("shall") rather than observable test outcomes, and some scenarios remain high-level rather than concretely testable.
- **Priority Standardization (High/Med/Low)**: PASS - All priorities are standardized to High, Medium, or Low.

## 4. Identified Issues, Gaps & Warnings
- **Traceability Gaps**:
  - No non-functional requirements trace cleanly to UN-013, UN-014, UN-015, or UN-016, despite those needs being quality-oriented and likely deserving explicit NFR coverage.
  - Several NFR source mappings appear misaligned:
    - NFR-002 (live ticker latency) is mapped to UN-002, but is more appropriately derived from UN-004.
    - NFR-003 (offline usability) is mapped to UN-003, but is more appropriately derived from UN-013.
    - NFR-004 (100,000 concurrent users) is mapped to UN-004, but is more appropriately derived from UN-015.
    - NFR-005 (rights compliance) is mapped to UN-005, but is more appropriately derived from UN-008.
    - NFR-006 (GDPR compliance) is mapped to UN-006, but is more appropriately derived from UN-016.
    - NFR-007 (UI accessibility/consistency) is mapped to UN-007, but is more appropriately derived from UN-014.
    - NFR-008 (UI/module consistency on server updates) is mapped to UN-008, but is more appropriately derived from UN-014.
    - NFR-010 (notification timeliness) is mapped to UN-010, but is more appropriately derived from UN-011.
    - NFR-011 (testing/support process) and NFR-012 (feedback evaluation) are introduced from the source text but are not traceable to any defined user need in 02_user_needs_report.
  - As a result, the current traceability chain is formally incomplete/inaccurate even though most business topics are represented.
- **Syntax / Standard Violations**:
  - NFR measurability is insufficient across most NFRs.
  - FR-001 includes a performance constraint that overlaps substantially with NFR-001; this is not invalid, but it blurs the distinction between functional and non-functional specification.
  - Gherkin scenarios are structurally present, but several acceptance criteria are not strongly testable because they use vague outcomes such as "currently unavailable," "remain usable," or "without loss of core application performance" without measurable conditions.
- **Ambiguities / Conflicts**:
  - Potential category inconsistency: performance, scalability, GDPR, offline resilience, and UI consistency are expressed as FRs and also as NFR themes, creating duplication and possible maintenance conflict.
  - The requirement set includes broad qualitative phrases from the source text without operational definition, including:
    - "real time"
    - "usable offline"
    - "without performance loss"
    - "at any time"
    - "directly accessible"
    - "streamlined authentication flow"
    - "thorough testing"
  - NFR-011 and NFR-012 concern internal process/operating model rather than product qualities visible to end users; they may belong in project quality plans or operational requirements rather than product NFRs.
  - Granularity is generally appropriate and not over-decomposed into UI field-level detail. However, some synthesis could be improved by separating product capabilities from quality constraints more cleanly.

## 5. Recommendations & Corrective Actions
1. **Correct NFR traceability mappings** so each NFR references the right source user need, especially for offline use, scalability, rights compliance, GDPR, UI consistency, and notification timing.
2. **Add or revise user needs** for pre-release testing/support and continuous feedback evaluation if those items are intentionally retained as requirements; otherwise remove NFR-011 and NFR-012 from the product specification.
3. **Strengthen NFR measurability** by introducing explicit metrics, for example:
   - live ticker refresh latency in seconds,
   - offline feature availability scope,
   - response-time/availability thresholds under 100,000 concurrent users,
   - notification delivery time targets,
   - authentication completion step/time targets,
   - compliance verification criteria for GDPR and rights enforcement.
4. **Refactor duplicated quality constraints** by keeping behavioral capabilities in FRs and moving performance, scalability, compliance, resilience, and consistency measures into NFRs with unique IDs and non-overlapping wording.
5. **Make acceptance criteria more testable** by replacing vague Then outcomes with measurable or observable results, such as explicit latency, visibility, persistence, or error-message behaviors.
6. **Re-run traceability validation** after revisions to ensure every UN has accurate downstream FR/NFR links and every NFR is justified by a defined user need.
