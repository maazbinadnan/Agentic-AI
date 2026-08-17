# 07 UI Mockups and Interaction Design

## Section 1: Interaction Design Overview & Screen Architecture

This approved interaction design package has been lightly refined to incorporate the remaining non-blocking implementation feedback from the latest IxD review. The requirements coverage remains unchanged, but affected mockups now better communicate semantic control intent and active navigation orientation.

### Screen Architecture

1. **Startup & Authentication** (`startup_auth_mockup.html`)
   - App launch, startup login/registration, validation messaging, and privacy consent touchpoints.
   - Refined to use semantic form controls in the mockup structure.
2. **News, Preferences & Notifications** (`news_preferences_notifications_mockup.html`)
   - Personalized news behavior, team/channel selection controls, preference update interactions, and notification states.
   - Refined to represent preferences as semantic search, checkbox, tab, and button controls rather than static visual chips alone.
3. **Live Ticker, Stream & Offline** (`live_ticker_stream_offline_mockup.html`)
   - Real-time results, stream-link visibility, rights restriction, offline continuity, and connectivity-restored resync state.
4. **Browse Details & Share** (`browse_details_share_mockup.html`)
   - Coverage browsing, team/player details, social platform selection, share success, and share unavailable behavior.
   - Refined to represent platform choice with semantic radio controls.
5. **Unified Interface, Feedback & Privacy** (`unified_interface_feedback_privacy_mockup.html`)
   - Integrated shell, stakeholder feedback review states, and GDPR-restricted actions.
   - Refined to add an explicit active navigation indicator for orientation.

All HTML files remain self-contained, responsive, and use the required `.wrap`, `.grid`, `.phone`, and `.screen` layout pattern.

## Section 2: HTML Mockups to User Stories Mapping Table

| User Story | Summary | Mockup File(s) | Coverage |
|---|---|---|---|
| US-001 | Launch Mobile App | `startup_auth_mockup.html` | supported launch, startup ready, platform boundary |
| US-002 | View Personalized News | `news_preferences_notifications_mockup.html` | filtered feed, no preferences default feed, saved personalization preview |
| US-003 | Manage Favorites and Channels | `news_preferences_notifications_mockup.html` | searchable/selectable clubs/channels, first save flow, update add/remove/save flow |
| US-004 | Follow Live Results | `live_ticker_stream_offline_mockup.html` | live updates available, no live data, offline cached events |
| US-005 | Browse Leagues, Teams, and Players | `browse_details_share_mockup.html` | populated details, no item selected, unavailable detail |
| US-006 | Access Live Stream Links | `live_ticker_stream_offline_mockup.html` | eligible stream shown, pre-broadcast empty, rights-restricted hidden |
| US-007 | Receive Notifications | `news_preferences_notifications_mockup.html` | alerts enabled, alerts off, device permission blocked |
| US-008 | Register and Log In | `startup_auth_mockup.html` | successful login, empty registration, invalid credentials |
| US-009 | Share Content to Social Media | `browse_details_share_mockup.html` | platform selection, selected-platform handoff success, share unavailable |
| US-010 | Use App During Connectivity Issues | `live_ticker_stream_offline_mockup.html` | offline cached continuity, no-data view, restored-connectivity resync |
| US-011 | Navigate Unified Interface | `live_ticker_stream_offline_mockup.html`, `unified_interface_feedback_privacy_mockup.html` | consistent shell, active navigation orientation, stable data updates |
| US-012 | Provide Product Feedback | `unified_interface_feedback_privacy_mockup.html` | stakeholder review inbox, evaluated feedback records, no new feedback records |
| US-013 | Protect Personal Data | `startup_auth_mockup.html`, `unified_interface_feedback_privacy_mockup.html` | consent capture, compliant processing context, blocked non-compliant action |

## Section 3: Detailed Screen Specifications & Component Breakdowns

### 3.1 Startup & Authentication
**File:** `startup_auth_mockup.html`
- **Stories/Requirements:** US-001, US-008, US-013 / FR-001, FR-009, FR-014
- **Components:** semantic email/password inputs, registration inputs, checkbox consent, authentication banners, primary/secondary buttons.
- **Acceptance traceability:**
  - US-001 Scenario 1: startup experience shown on supported device.
  - US-001 Scenario 2: unsupported-platform note is communicated.
  - US-008 Scenario 1: valid login state grants entry.
  - US-008 Scenario 2: invalid/incomplete credentials show blocking error.
  - US-013 Scenario 1: privacy consent/data handling acknowledgement included.
- **Refinement note:** visual placeholder fields were replaced with semantic form controls to better communicate accessible implementation intent.

### 3.2 News, Preferences & Notifications
**File:** `news_preferences_notifications_mockup.html`
- **Stories/Requirements:** US-002, US-003, US-007 / FR-002, FR-003, FR-008
- **Components:** semantic tab buttons, search inputs, checkbox-based multi-select lists, selected-summary chips, notification rows, save/update buttons, state banners.
- **Acceptance traceability:**
  - US-002 Scenario 1: populated state shows feed preview filtered by saved clubs/channels.
  - US-002 Scenario 2: empty state shows default-content behavior when nothing is configured.
  - US-003 Scenario 1: empty/unconfigured state plus populated saved state show selecting clubs/channels and first save behavior.
  - US-003 Scenario 2: update state explicitly shows removing Arsenal, adding Juventus, replacing channels, and saving updated preferences.
  - US-007 Scenario 1: notifications toggled on in populated state.
  - US-007 Scenario 2: alerts off and device-permission-blocked state represented.
- **Refinement note:** static chip-only selectors were upgraded to clearer search + checkbox selection patterns to support later keyboard/screen-reader implementation.

### 3.3 Live Ticker, Stream & Offline
**File:** `live_ticker_stream_offline_mockup.html`
- **Stories/Requirements:** US-004, US-006, US-010, US-011 / FR-004, FR-006, FR-007, FR-011, FR-012
- **Components:** score header, event timeline, stream availability banner, stream CTA, offline warning, rights restriction message, reconnection/resync state.
- **Acceptance traceability:**
  - US-004 Scenario 1: populated state shows continuously updated live events.
  - US-004 Scenario 2: empty state shows no live data available.
  - US-006 Scenario 1: stream link appears only in eligible live state.
  - US-006 Scenario 2: rights-restricted state suppresses usable stream link.
  - US-010 Scenario 1: offline state preserves supported functionality using cached events.
  - US-010 Scenario 2: connectivity-restored state shows resumed retrieval of current online data after reconnection.
  - US-011 Scenario 2: content refresh occurs without breaking access patterns.

### 3.4 Browse Details & Share
**File:** `browse_details_share_mockup.html`
- **Stories/Requirements:** US-005, US-009 / FR-005, FR-010
- **Components:** competition header, team card, player card, selected report card, radio-based platform options, share CTA, success banner, unavailable-detail banner.
- **Acceptance traceability:**
  - US-005 Scenario 1: populated state shows league/team/player/report information.
  - US-005 Scenario 2: unavailable-detail state communicates missing information.
  - US-009 Scenario 1: populated state includes supported social-platform selection and successful content handoff to the selected platform.
  - US-009 Scenario 2: error state informs the user when sharing is unavailable.
- **Refinement note:** share-platform choice now communicates a true mutually exclusive selection model.

### 3.5 Unified Interface, Feedback & Privacy
**File:** `unified_interface_feedback_privacy_mockup.html`
- **Stories/Requirements:** US-011, US-012, US-013 / FR-012, FR-013, FR-014
- **Components:** persistent shell, module navigation rail, explicit active navigation state, stakeholder feedback inbox cards, evaluation-status card, no-records state, privacy center, blocked-action banner.
- **Acceptance traceability:**
  - US-011 Scenario 1: integrated modules remain reachable from the single shared interface.
  - US-011 Scenario 2: interface remains consistent during data updates.
  - US-012 Scenario 1: populated stakeholder-review state shows feedback/app reviews available for evaluation.
  - US-012 Scenario 2: empty stakeholder-review state explicitly shows no new feedback records.
  - US-013 Scenario 2: privacy/error state blocks unsupported personal-data action.
- **Refinement note:** active navigation styling was added to improve orientation within the unified shell.

## Section 4: Visual Hierarchy, WCAG 2.1 Accessibility, & UX Trade-offs

### Visual Hierarchy
- Persistent top bars label each subcase clearly.
- Primary actions remain visually prominent through filled buttons.
- Search, selection, and review workflows are grouped into bordered sections and cards for mobile scanning.
- Active navigation highlighting improves wayfinding in the unified shell.

### WCAG 2.1 Accessibility Considerations
- Mockups now better signal semantic implementation intent through visible form controls such as inputs, checkboxes, radios, and buttons.
- Error, success, offline, and restricted states are explained with text labels rather than color alone.
- Search and multi-select preference controls are organized in predictable reading order.
- Active navigation state is visually distinguished for orientation support.
- Touch targets remain large and spaced for mobile use.

### UX Trade-offs
- These remain low-to-mid fidelity mockups intended for handoff clarity rather than production-complete component behavior.
- Multi-state side-by-side layouts prioritize acceptance coverage and edge-case communication over strict simulation of one linear runtime flow.
- Accessibility behavior such as keyboard handling, screen-reader announcements, and focus management is indicated by semantic structure but still requires implementation detail in development.

## Revision Summary Against Latest Review

In response to the latest approved review feedback:
- **Startup & Authentication refined:** visual placeholder fields/buttons updated to semantic inputs, checkbox, and buttons.
- **News / Preferences refined:** static chip-only selection replaced with clearer search + checkbox multi-select pattern while preserving saved/update states.
- **Browse / Share refined:** platform choice updated to radio-style selection.
- **Unified shell refined:** active navigation indicator added for the current section.

All affected deliverables have been updated directly in the target output directory.