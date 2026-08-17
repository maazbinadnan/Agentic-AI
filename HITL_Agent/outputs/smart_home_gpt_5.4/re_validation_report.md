# Requirements Engineering Validation Report

## 1. Executive Summary
- **Overall Validation Status**: NEEDS REVISION
- **Audit Date**: 2026-08-13
- **Deliverables Evaluated**:
  - [x] 01_elicitation_report.md
  - [x] 02_user_needs_report.md
  - [x] 03_functional_requirements.md
  - [x] 04_non_functional_requirements.md
  - [x] 05_user_stories.md

## 2. Requirements Traceability Matrix
| User Need ID | Functional Req ID | Non-Functional Req ID | User Story ID | Traceability Status |
|---|---|---|---|---|
| UN-001 | FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, FR-011, FR-020, FR-021 | NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-006, NFR-008, NFR-018, NFR-024, NFR-025, NFR-026, NFR-029 | US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-011, US-020, US-021 | COMPLETE |
| UN-002 | FR-005, FR-007, FR-008, FR-009, FR-011, FR-020, FR-021 | NFR-004, NFR-005, NFR-006, NFR-007, NFR-008, NFR-024, NFR-025, NFR-027, NFR-028, NFR-029 | US-005, US-007, US-008, US-009, US-011, US-020, US-021 | COMPLETE |
| UN-003 | FR-004, FR-012, FR-013, FR-014, FR-020 | NFR-009, NFR-010, NFR-018 | US-004, US-012, US-013, US-014, US-020 | COMPLETE |
| UN-004 | FR-004, FR-015, FR-020 | NFR-011, NFR-012, NFR-018 | US-004, US-015, US-020 | COMPLETE |
| UN-005 | FR-001, FR-002, FR-003, FR-004, FR-021 | NFR-003, NFR-013, NFR-014, NFR-015, NFR-016, NFR-017, NFR-018 | US-001, US-002, US-003, US-004, US-021 | COMPLETE |
| UN-006 | FR-002, FR-016, FR-017 | NFR-014, NFR-017, NFR-019, NFR-020 | US-002, US-016, US-017 | COMPLETE |
| UN-007 | FR-002, FR-016, FR-017, FR-018, FR-020 | NFR-014, NFR-017, NFR-019, NFR-020 | US-002, US-016, US-017, US-018, US-020 | COMPLETE |
| UN-008 | FR-002, FR-018 | NFR-014, NFR-017, NFR-021 | US-002, US-018 | COMPLETE |
| UN-009 | FR-004, FR-005, FR-012, FR-013, FR-015, FR-019, FR-020 | NFR-012, NFR-022, NFR-023, NFR-024, NFR-026, NFR-027, NFR-029, NFR-030 | US-004, US-005, US-012, US-013, US-015, US-019, US-020 | COMPLETE |

## 3. Syntax & Quality Standard Compliance
- **"Shall" Syntax Compliance (FR/NFR)**: **FAIL** - All FRs and all NFRs use "shall" syntax; however, one NFR contains mixed modal wording that weakens strictness: **NFR-014** uses both "shall enforce" and "shall additionally be permitted" appropriately, but no critical syntax defect exists there. The actual syntax failure is in the traceability metadata label inconsistency: FRs use **Source Need** while NFRs use **Source**. More importantly, some acceptance criteria use system-level "shall" inside user stories, which is acceptable for AC wording. No missing "shall" found in FR/NFR statements themselves. Marked FAIL overall because the deliverables introduce non-source-derived mandatory language without validation in several NFRs.
- **Measurable SLA Criteria (NFR)**: **FAIL** - Many NFRs are measurable and testable (e.g., NFR-001, 002, 003, 004, 007, 010, 011, 020, 021, 022, 023, 024, 025, 030). However, several NFRs are insufficiently measurable or rely on vague terms: **NFR-008** ("without loss of functional connectivity" is undefined), **NFR-018** (usability phrased qualitatively), **NFR-019** (authorization restriction is testable but not an SLA), **NFR-026** (fail-safe logging is measurable but "fail-safe state" is underdefined), **NFR-027** (restart recovery behavior is testable but not performance-based). Also, **NFR-015**, **NFR-016**, **NFR-017**, **NFR-019**, **NFR-028**, **NFR-029** are quality constraints, but not all contain concrete measurable acceptance thresholds.
- **Agile User Story Phrasing (US)**: **PASS** - All user stories follow the standard "As a ... I want to ... so that ..." structure.
- **Gherkin Acceptance Criteria (AC)**: **PASS WITH WARNINGS** - All 21 user stories include at least 2 scenarios and each scenario uses Given / When / Then structure. Warning: scenario titles are prefixed with "Scenario:" but not formal fenced Gherkin; acceptable in markdown, though some scenarios are descriptive rather than strongly test-data-driven.
- **Priority Standardization (High/Med/Low)**: **FAIL** - Priorities are standardized as **High**, **Medium**, or **Low** in user needs and requirements; however, the compliance criterion specifies **High/Med/Low**. The deliverables consistently use **Medium** instead of **Med**. This is internally consistent but not strictly compliant with the requested standard.

## 4. Identified Issues, Gaps & Warnings
- **Traceability Gaps**: None found in core forward/backward traceability. Every UN is mapped to one or more FR/NFR entries, and every FR has a corresponding US. No orphan UN, FR, NFR, or US identifiers detected.
- **Syntax / Standard Violations**:
  - **NFR source validity issue:** **NFR-015** mandates TLS 1.2 or higher, but the elicitation report explicitly states TLS/HTTPS was **not confirmed** and cannot be treated as mandatory from the current source set.
  - **Invented specificity without elicited basis:** **NFR-009** (4 schedule periods/day), **NFR-012** (90-day retention), **NFR-016** (15-minute timeout), **NFR-022** (24-hour backup cadence), **NFR-023** (4-hour restore), **NFR-024** (99.0% availability), **NFR-028** (120V/15A), **NFR-030** (720-hour MTBSF) are measurable but not supported by the elicitation evidence or ground-truth source.
  - **Metadata inconsistency:** FRs cite **Source Need** while NFRs cite **Source**. This is a formatting inconsistency that weakens audit readability.
  - **Priority label strictness issue:** uses **Medium** instead of **Med**.
- **Ambiguities / Conflicts**:
  - **Conflict with elicitation assumptions:** The elicitation report states TLS is not confirmed, but **NFR-015** makes it mandatory.
  - **Potential role ambiguity:** **FR-002** and **NFR-014** define broad RBAC, but the elicitation report notes the detailed permission matrix remains ambiguous. Current requirements may overstate role granularity as fully defined.
  - **Granularity concern:** The specification is mostly cohesive and not over-decomposed into UI micro-controls. However, several NFRs appear over-synthesized from assumptions rather than source-backed scope, introducing false precision.
  - **Security workflow incompleteness:** Alarm armed/disarmed modes, entry/exit delays, acknowledgement/reset behavior, and breach semantics remain unspecified despite FR-010/011 and NFR-025/026.
  - **Environmental control incompleteness:** Thermostat/humidistat set-point ranges, increments, deadband/tolerance, and override behavior remain undefined.
  - **Backup/recovery incompleteness:** FR-019 is traceable, but restore workflow is not covered by any user story and is only implied by NFR-023.

## 5. Recommendations & Corrective Actions
1. **Revise unsupported NFRs** to align strictly with elicited and source-backed evidence. Either remove or explicitly mark as assumptions pending approval: NFR-009, NFR-012, NFR-015, NFR-016, NFR-022, NFR-023, NFR-024, NFR-028, NFR-030.
2. **Resolve the TLS contradiction** by either:
   - removing NFR-015 from the current baseline, or
   - updating the elicitation record with stakeholder confirmation that TLS is mandatory.
3. **Standardize metadata labels** across FRs and NFRs, using one convention such as **Source Need** for both.
4. **Normalize priorities** to the mandated enumeration exactly as required by the audit standard. If strict compliance is required, replace **Medium** with **Med** throughout; otherwise update the standard to permit **Medium**.
5. **Add missing behavioral clarifications** in a refinement cycle for:
   - thermostat/humidistat set-point ranges and increments,
   - deadband/tolerance and override behavior,
   - security armed/disarmed states,
   - breach trigger semantics,
   - alarm reset/acknowledgement behavior,
   - communication-loss handling scope.
6. **Strengthen testability of qualitative NFRs** such as NFR-008 and NFR-018 by defining measurable criteria, e.g., packet success rate, supported browsers, maximum clicks/tasks, task completion rate, or usability success thresholds.
7. **Consider adding user stories** for restore/recovery and audit logging if those NFRs remain in scope, to improve end-to-end traceability from quality constraints into verifiable user-facing or operational scenarios.
8. **Retain the current FR→US mapping**, as it is complete and structurally strong; the main revision need is not traceability coverage but source fidelity and unsupported precision.
