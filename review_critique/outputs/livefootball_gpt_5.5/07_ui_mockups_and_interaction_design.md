# 07 UI Mockups and Interaction Design

## 1. Interaction Design Overview & Screen Architecture

This revised interaction design package translates the LiveFootball requirements into low-to-mid fidelity, self-contained responsive HTML mockups. This update resolves the minor polish issues identified in the latest IxD review by improving sharing-flow completeness and finalizing semantic action controls.

### Revision summary
- Retained the previously resolved fixes for **US-007**, **US-008**, and **US-012**.
- Updated **`news_home_mockup.html`** to explicitly show a **supported-device social sharing sheet** for **US-010 Scenario 1**.
- Replaced non-semantic Share controls in the news screen with semantic **`button`** elements.
- Updated **`live_ticker_streams_mockup.html`** so action elements use semantic **`button`** controls with clear accessible labels instead of ambiguous link-like elements.

### Design goals
- Support rapid startup and clear onboarding for Android and iOS users.
- Prioritize quick access to football news, live match data, and personalized content.
- Reflect requirement-aligned states including default, populated, success, update, restriction, and error/validation views.
- Preserve usability during weak or lost connectivity.
- Improve accessibility and developer handoff clarity with semantic control patterns.

### Screen architecture
1. **Startup / Registration / Login**
   - Entry point for supported mobile users.
   - Includes startup, registration success, login failure, and login success leading to personalized features.
2. **News Feed**
   - Personalized news based on favorite teams and selected sports channels.
   - Includes supported social sharing sheet and unavailable sharing state.
3. **Live Ticker & Stream Availability**
   - Real-time result monitoring and rights-aware live stream presentation with semantic action controls.
4. **Competitions, Teams & Players**
   - Browsing across national/international competitions and detailed entity profiles.
5. **Personalization & Notifications**
   - Editable preference management for clubs, channels, modules, and notification behavior.
6. **Offline Use & Feedback**
   - Offline usability messaging, reconnection state, end-user feedback submission, and product/support review queue.

---

## 2. HTML Mockups to User Stories Mapping Table

| HTML Mockup File | Covered User Stories | Requirement Traceability | Notes |
|---|---|---|---|
| `startup_login_mockup.html` | US-001, US-007 | FR-001, FR-007 | Includes valid returning-user login success state with access to personalized features |
| `news_home_mockup.html` | US-002, US-010 | FR-002, FR-010 | Revised to include supported-device social share sheet and semantic Share buttons |
| `live_ticker_streams_mockup.html` | US-003, US-006 | FR-003, FR-006 | Revised action controls to use semantic buttons with clear labels |
| `competitions_details_mockup.html` | US-004, US-005 | FR-004, FR-005 | Includes competition browser, populated team/player details, and unavailable content state |
| `personalization_notifications_mockup.html` | US-008, US-009 | FR-008, FR-009 | Includes editable controls, update flow, and updated-success state |
| `offline_feedback_mockup.html` | US-011, US-012 | FR-011, FR-012 | Includes feedback review panel for product/support team |

### User story coverage confirmation
All provided user stories are covered:
- US-001
- US-002
- US-003
- US-004
- US-005
- US-006
- US-007
- US-008
- US-009
- US-010
- US-011
- US-012

---

## 3. Detailed Screen Specifications & Component Breakdowns

### 3.1 Startup / Registration / Login (`startup_login_mockup.html`)
**Mapped stories:** US-001, US-007  
**Mapped requirements:** FR-001, FR-007

**Primary components**
- Brand/header block
- Supported platform indicator
- Startup hero message
- Primary CTAs for registration and login
- Registration form fields
- Login form fields
- Validation/help text
- Success and warning banners
- Post-login personalized quick access panel

**Key interaction behavior**
- Users can start from a clear app home/startup entry screen.
- New users can register directly at startup.
- Returning users can log in from the same startup flow.
- Validation state demonstrates error messaging for failed login.
- Successful login state explicitly shows access to personalized features such as favorite clubs and quick links to personalized news and live ticker.
- Supported device messaging reinforces Android/iOS-only availability.

**States represented**
- Default state: startup landing screen
- Populated state: registration success
- Error state: login validation failure
- Success state: returning-user login with personalized access

### 3.2 News Feed (`news_home_mockup.html`)
**Mapped stories:** US-002, US-010  
**Mapped requirements:** FR-002, FR-010

**Primary components**
- Personalized topic chips for clubs/channels
- News cards with source and recency metadata
- Semantic Share buttons
- Supported-device social share sheet/options panel
- Empty/default prompt for missing preferences
- Sharing unavailable banner

**Key interaction behavior**
- Feed prioritizes current football news relevant to saved preferences.
- When preferences are missing, the screen prompts configuration while still allowing general news access.
- Sharing is attached directly to content cards through semantic buttons.
- A dedicated share-options state shows device-supported sharing destinations after Share is selected, satisfying US-010 Scenario 1.
- Device limitation state is shown when sharing is unsupported.

**States represented**
- Default state: no preferences selected
- Populated state: personalized news feed
- Success/interaction state: supported share sheet visible
- Error state: device sharing unavailable

### 3.3 Live Ticker & Stream Availability (`live_ticker_streams_mockup.html`)
**Mapped stories:** US-003, US-006  
**Mapped requirements:** FR-003, FR-006

**Primary components**
- Match summary card
- Live score emphasis
- Match event timeline
- Live API status banner
- Approved stream provider CTA
- Rights restriction / not-started message
- Semantic action buttons for match details and stream launch

**Key interaction behavior**
- Live ticker emphasizes current score and recent events.
- Real-time update messaging clarifies dependency on external API data.
- When data is unavailable, users receive a clear temporary unavailability message.
- Live stream links/actions appear only when rights and broadcast conditions are satisfied.
- Match-details and stream actions now use semantic buttons with explicit accessible labels for implementation clarity.

**States represented**
- Default/edge state: no active live data available
- Populated state: active live match updates
- Error/restriction state: live data unavailable and ineligible stream access

### 3.4 Competitions, Teams & Players (`competitions_details_mockup.html`)
**Mapped stories:** US-004, US-005  
**Mapped requirements:** FR-004, FR-005

**Primary components**
- Competition category tags
- Competition list tiles
- Team profile summary card
- Player profile detail card
- Unavailable content banner

**Key interaction behavior**
- Users can browse both national and international football contexts.
- Team and player detail cards expose concise, high-value informational attributes.
- Missing or unavailable competition/profile data is surfaced explicitly rather than hidden.

**States represented**
- Default state: browse competition catalog
- Populated state: team and player details available
- Error/partial-data state: unavailable content and missing profile fields

### 3.5 Personalization & Notifications (`personalization_notifications_mockup.html`)
**Mapped stories:** US-008, US-009  
**Mapped requirements:** FR-008, FR-009

**Primary components**
- Editable favorite club checkboxes
- Editable preferred channel checkboxes
- Editable module checkboxes
- Notification preference checkboxes
- Notification state preview radios
- Save/update action buttons
- Updated-success confirmation panel

**Key interaction behavior**
- Users can explicitly add or remove favorite clubs, channels, and modules using visible form controls.
- Notification preferences can be enabled or disabled using semantic inputs rather than decorative toggles.
- Save/update actions make the preference modification flow explicit.
- Updated-success state confirms that changes have been applied to app behavior.
- Enabled versus disabled notification outcomes remain visible for traceability to US-009.

**States represented**
- Default/editable state: settings available for adjustment
- Populated state: previously selected options shown in controls
- Update-success state: revised preferences applied
- Behavioral state: notification enabled vs disabled outcome preview

### 3.6 Offline Use & Feedback (`offline_feedback_mockup.html`)
**Mapped stories:** US-011, US-012  
**Mapped requirements:** FR-011, FR-012

**Primary components**
- Offline warning banner
- Available offline content card
- Unavailable live features card
- Reconnected success banner
- Feedback form fields
- Submit CTA
- Success confirmation and validation example
- Product/support feedback review queue

**Key interaction behavior**
- Users are informed which features remain available without connectivity.
- Reconnection state clarifies that live capability resumes automatically.
- Feedback form supports direct in-app submission.
- Validation messaging shows expected handling of empty submissions.
- Product/support review panel shows submitted feedback entries with category, timestamp, submitter, and review status to satisfy the review requirement.

**States represented**
- Default state: feedback form ready
- Populated state: successful submission and reconnection
- Error/validation state: empty feedback validation, offline constraint messaging
- Review state: submitted feedback visible for support/product assessment

---

## 4. Visual Hierarchy, WCAG 2.1 Accessibility, & UX Trade-offs

### Visual hierarchy
- Important tasks are prioritized with large titles, clear banners, and high-contrast call-to-action buttons.
- Live score information is given the strongest visual emphasis due to time sensitivity.
- Secondary metadata such as source, timestamps, and contextual notes are visually subdued but still readable.
- Error, warning, and success states are color-coded and boxed to support quick scanning.

### WCAG 2.1 accessibility considerations
- HTML mockups use semantic text structure with visible headings and labels.
- Inputs are paired with labels to support form comprehension.
- Interactive components are represented with more semantic HTML patterns:
  - `button` elements for actionable controls such as Share, Open match details, Watch on DAZN, Save changes, and Submit feedback
  - `input type="checkbox"` for editable multi-select preferences
  - `input type="radio"` for mutually exclusive preview states
  - labeled text fields, textareas, and selects for data entry
- Important state changes are represented with both text and color, reducing reliance on color alone.
- Large touch-friendly controls support mobile interaction.
- Responsive grid layout supports multiple viewport sizes while preserving mobile intent.

### UX trade-offs
- Mockups intentionally use low-to-mid fidelity styling to focus review on structure and interaction, not final visual branding.
- Some stories are combined into shared screens to reduce navigation fragmentation and better match natural user workflows.
- The product/support feedback review area is represented within the same deliverable for compact traceability, though in a production system it may exist in a separate internal interface.
- Offline behavior is communicated through system banners and availability summaries instead of simulating full data synchronization mechanics.
- The 100,000 concurrent users, reliability testing, support process, GDPR compliance, and performance constraints are acknowledged as broader system/non-functional concerns that influence interaction decisions, but they do not require separate end-user mockup screens unless later expanded into explicit stories.

---

## Deliverables updated in this revision
Updated HTML mockups:
- `news_home_mockup.html`
- `live_ticker_streams_mockup.html`

Previously updated and retained:
- `startup_login_mockup.html`
- `personalization_notifications_mockup.html`
- `offline_feedback_mockup.html`
- `competitions_details_mockup.html`

Updated report:
- `07_ui_mockups_and_interaction_design.md`
