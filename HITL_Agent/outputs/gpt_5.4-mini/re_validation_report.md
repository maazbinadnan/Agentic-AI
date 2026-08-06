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
| UN-001 | FR-001, FR-013 | NFR-001, NFR-004, NFR-005, NFR-008, NFR-010, NFR-011, NFR-012, NFR-013 | US-001, US-013 | PARTIAL |
| UN-002 | FR-002 | NFR-001, NFR-010 | US-002 | COMPLETE |
| UN-003 | FR-003 | NFR-002, NFR-003, NFR-005, NFR-006, NFR-010 | US-003 | COMPLETE |
| UN-004 | FR-003, FR-004, FR-009, FR-013 | NFR-002, NFR-004, NFR-005, NFR-010, NFR-011 | US-003, US-004, US-009, US-013 | COMPLETE |
| UN-005 | FR-005 | NFR-007, NFR-008 | US-005 | PARTIAL |
| UN-006 | FR-006 | NFR-007, NFR-009, NFR-010, NFR-013 | US-006 | PARTIAL |
| UN-007 | FR-007 | - | US-007 | PARTIAL |
| UN-008 | FR-008 | - | US-008 | PARTIAL |
| UN-009 | FR-009, FR-013 | - | US-009, US-013 | PARTIAL |
| UN-010 | FR-010 | - | US-010 | PARTIAL |
| UN-011 | FR-011 | - | US-011 | PARTIAL |
| UN-012 | FR-012 | - | US-012 | PARTIAL |
| UN-013 | FR-013 | - | US-013 | PARTIAL |

## 3. Syntax & Quality Standard Compliance
- **"Shall" Syntax Compliance (FR/NFR)**: PASS - All listed FRs and NFRs use mandatory "shall" phrasing.
- **Measurable SLA Criteria (NFR)**: FAIL - Only NFR-001 contains a concrete measurable threshold (2 seconds). NFR-002, NFR-003, NFR-004, NFR-005, NFR-009, NFR-010, NFR-011, NFR-012, and NFR-013 lack specific measurable/testable targets. Examples include vague terms such as "without degradation," "real time," "usable," "without unnecessary navigation steps," and "thorough".
- **Agile User Story Phrasing (US)**: PASS - All user stories follow the "As a ... I want to ... so that ..." structure.
- **Gherkin Acceptance Criteria (AC)**: PASS - All user stories contain at least 2 scenarios with Given/When/Then structure.
- **Priority Standardization (High/Med/Low)**: PASS - All priorities are constrained to High, Medium, or Low.

## 4. Identified Issues, Gaps & Warnings
- **Traceability Gaps**:
  - NFR source mapping is materially inconsistent with the user needs model.
  - UN-007 through UN-013 have no directly mapped NFRs, despite several of them clearly implying quality/compliance attributes.
  - NFR-002 is sourced to UN-001, UN-003, and UN-004, but semantically aligns to UN-012 (peak demand scalability).
  - NFR-003 is sourced to UN-003, but semantically aligns to UN-005 (live real-time ticker).
  - NFR-004 is sourced to UN-001 and UN-004, but semantically aligns to UN-011 (offline/limited connectivity usability).
  - NFR-006 is sourced to UN-003, but semantically aligns to UN-008 (rights-aware live stream links).
  - NFR-007 is sourced to UN-005 and UN-006, but semantically aligns to UN-013 (GDPR compliance).
  - NFR-008 is sourced to UN-005, but semantically aligns to UN-001 (mandatory login).
  - NFR-009 is sourced to UN-006, but semantically aligns to UN-009 (notifications).
  - Several user needs show only FR and US coverage but no NFR coverage, resulting in only partial end-to-end traceability.
- **Syntax / Standard Violations**:
  - FR-002 and FR-012 are categorized as functional requirements but are predominantly non-functional in nature (performance/scalability), creating classification inconsistency with NFR-001 and NFR-002.
  - NFR-006 and NFR-008 are categorized as non-functional requirements but are functional/behavioral constraints, overlapping with FR-008 and FR-001 respectively.
  - NFR-003 uses "real time" and "low enough" without a measurable latency target.
  - NFR-002 uses "without degradation of core application performance" without defining measurable service levels.
  - NFR-004 and NFR-011 duplicate overlapping resilience/offline expectations.
  - NFR-007 duplicates FR-013 at a high level without decomposing GDPR into auditable controls.
- **Ambiguities / Conflicts**:
  - Duplicate/overlapping requirements exist across FR and NFR sets for startup, scalability, login, rights gating, offline behavior, and GDPR handling, which may create downstream implementation and test duplication.
  - "Without performance degradation," "real time," "reliable operation," and "without unnecessary navigation steps" are ambiguous and not objectively testable.
  - Coverage requirement in FR-006 is broad but still depends on "supported" leagues/competitions; support boundaries are not defined.
  - Granularity is generally appropriate, but some requirements blend multiple concerns into single statements, especially FR-013 and NFR-007, making verification more difficult.
  - Edge-case coverage is limited for several areas, including failed registration, expired sessions, invalid region detection for stream rights, notification delivery failures, stale cache handling, and API outage behavior for live ticker.

## 5. Recommendations & Corrective Actions
1. Correct all NFR source mappings so each NFR traces to the semantically correct user need(s), especially NFR-002, NFR-003, NFR-004, NFR-006, NFR-007, NFR-008, and NFR-009.
2. Rebalance requirement classification:
   - Move performance/scalability statements such as FR-002 and FR-012 into NFRs only, or keep them in FRs with explicit rationale and remove duplication.
   - Move behavioral items such as NFR-006 and NFR-008 into FRs, or restate them as quality constraints if they must remain NFRs.
3. Make NFRs measurable and testable by adding explicit metrics, for example:
   - live ticker latency in seconds,
   - peak-load response time thresholds,
   - offline cache retention/availability expectations,
   - notification delivery targets,
   - UI navigation benchmarks,
   - support SLAs and defect resolution targets.
4. De-duplicate overlapping FR/NFR pairs and split compound requirements into smaller auditable requirements where needed.
5. Strengthen completeness by adding or refining requirements and/or acceptance criteria for edge cases such as authentication failures, password reset, network loss during live updates, unsupported competitions, stale cached data, unavailable streaming providers, and API outages.
6. Decompose GDPR compliance into specific verifiable controls where appropriate, such as consent capture, privacy notice access, data subject rights handling, secure storage/transmission, and retention/deletion behavior.
7. Preserve the current strong user story quality baseline; the user stories are structurally compliant and generally well scoped, but should be updated after requirement reclassification and traceability corrections.
