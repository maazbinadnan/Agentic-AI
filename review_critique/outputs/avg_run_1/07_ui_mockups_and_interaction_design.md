# 07 UI Mockups and Interaction Design

## Section 1: Interaction Design Overview & Screen Architecture

This interaction design package translates the approved functional requirements and user stories for the **LiveFootball** mobile app into low-to-mid fidelity responsive HTML mockups. The mockups focus on clarity, mobile information hierarchy, core task flows, and edge-case visibility rather than visual polish.

### Design Intent
- Provide a **single integrated mobile experience** for football fans.
- Prioritize **fast startup and direct access** to key modules.
- Support **personalization** through favorites, channels, and notifications.
- Make **live experiences** prominent while showing graceful fallback states when data is unavailable, restricted, or offline.
- Keep **fixed UI structure stable** while content modules update dynamically.

### Screen Architecture
The generated mockups are grouped by feature areas:

1. **Authentication Entry**
   - Startup, registration, login
2. **Preference Management**
   - Favorite clubs, preferred channels, notifications
3. **Content Consumption**
   - Personalized news feed and sharing
4. **Live Match Experience**
   - Live ticker and stream access
5. **Football Information Browsing**
   - Leagues, competitions, teams, players, offline support
6. **Platform-Level Navigation**
   - Unified interface and feedback evaluation support

Each HTML file includes:
- A responsive grid wrapper
- At least 3 side-by-side subcases
- Primary/populated state
- Empty or unconfigured state
- Error, restricted, or offline state

---

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML Mockup File | Covered User Stories | Related Functional Requirements | Coverage Summary |
|---|---|---|---|
| `auth_startup_mockup.html` | US-001 | FR-001, FR-009 | Startup access, registration, login success, empty registration, invalid login handling |
| `favorites_notifications_mockup.html` | US-002, US-007 | FR-002, FR-007 | Favorite clubs, preferred channels, save/update preferences, notification opt-in and disabled state |
| `news_sharing_mockup.html` | US-003, US-008 | FR-003, FR-008 | Personalized news feed, non-personalized fallback feed, article/report sharing and sharing unavailable state |
| `live_ticker_streams_mockup.html` | US-004, US-006 | FR-004, FR-006 | Live ticker updates, unavailable live data, stream link display, rights restriction behavior |
| `browse_details_offline_mockup.html` | US-005, US-010 | FR-005, FR-010 | League/team/player detail access, initial browse state, offline cached use and live-data limitation |
| `unified_interface_feedback_mockup.html` | US-009, US-011 | FR-009, FR-011 | Integrated module navigation, stable interface layout, stakeholder feedback evaluation with empty state |

### Full User Story Coverage Check
- US-001: Covered
- US-002: Covered
- US-003: Covered
- US-004: Covered
- US-005: Covered
- US-006: Covered
- US-007: Covered
- US-008: Covered
- US-009: Covered
- US-010: Covered
- US-011: Covered

---

## Section 3: Detailed Screen Specifications & Component Breakdowns

### 3.1 `auth_startup_mockup.html`
**User Story Coverage:** US-001  
**Requirement Trace:** FR-001, FR-009

**Subcases included:**
1. Populated login success state
2. Empty registration state
3. Invalid credential error state

**Components:**
- Brand/startup hero section
- Login/register tab switch
- Form fields for identity and password
- Success and error feedback banners
- Primary action and secondary alternative action
- Privacy/GDPR notice reference

**Interaction Notes:**
- The startup screen reduces decision load by surfacing auth immediately.
- Validation messaging is inline and prominent.
- Post-login state signals successful personalization access.

### 3.2 `favorites_notifications_mockup.html`
**User Story Coverage:** US-002, US-007  
**Requirement Trace:** FR-002, FR-007

**Subcases included:**
1. Saved favorite teams and channels with notifications enabled
2. No preferences selected
3. Notification permission/activation blocked

**Components:**
- Favorite club chip selector
- Preferred channel chip selector
- Save preference action
- Notification toggle card
- Informational and error banners

**Interaction Notes:**
- Preferences are represented as selectable chips for quick mobile scanning.
- Notification activation is visually separated because it depends on both app setting and device permission.
- Empty state explains why personalization is not active yet.

### 3.3 `news_sharing_mockup.html`
**User Story Coverage:** US-003, US-008  
**Requirement Trace:** FR-003, FR-008

**Subcases included:**
1. Personalized news feed with relevant content cards
2. Generic feed when no preferences exist
3. Share unavailable device state

**Components:**
- Search/filter style input field
- News cards with team/channel tags
- Share and open actions
- Empty-state message for non-personalized browsing
- Share failure alert

**Interaction Notes:**
- Tags make the basis of personalization transparent.
- Sharing is kept at card level to reduce steps.
- When sharing is unavailable, the user is informed without blocking article access.

### 3.4 `live_ticker_streams_mockup.html`
**User Story Coverage:** US-004, US-006  
**Requirement Trace:** FR-004, FR-006

**Subcases included:**
1. Live match with updating event timeline and valid stream access
2. No selected/available live match data
3. API/live-data failure combined with rights restriction

**Components:**
- Match score summary panel
- Live status indicator
- Event timeline
- Stream availability note
- Rights restriction/error message
- Retry or browse action

**Interaction Notes:**
- The score block is visually dominant to reflect user intent during live viewing.
- Timeline events are arranged vertically for quick chronological comprehension.
- Rights restrictions are shown clearly and separately from data availability to avoid ambiguity.

### 3.5 `browse_details_offline_mockup.html`
**User Story Coverage:** US-005, US-010  
**Requirement Trace:** FR-005, FR-010

**Subcases included:**
1. Populated league/team/player information state
2. No item selected yet
3. Offline state with cached details and blocked live retrieval

**Components:**
- Competition header card
- Team and player detail list items
- Browse entry CTA
- Offline banner and recovery action
- Error banner for unavailable live retrieval

**Interaction Notes:**
- Information is chunked into cards to reduce cognitive overload.
- Offline mode preserves continuity by emphasizing cached content availability.
- The distinction between static details and live data is explicit.

### 3.6 `unified_interface_feedback_mockup.html`
**User Story Coverage:** US-009, US-011  
**Requirement Trace:** FR-009, FR-011

**Subcases included:**
1. Integrated home with stable module entry points and available feedback volume
2. Empty feedback review state
3. No feedback inputs available while main shell remains usable

**Components:**
- Persistent primary navigation
- Module summary cards
- Live ticker quick-access area
- Feedback review summary panel
- Empty/error message area

**Interaction Notes:**
- Stable navigation reinforces the requirement for a unified interface.
- Feedback evaluation is represented as a stakeholder-facing review view because the requirement is process/support-oriented rather than an end-user action.
- Core navigation remains unchanged across states to reflect interface consistency under server updates.

---

## Section 4: Visual Hierarchy, WCAG 2.1 Accessibility, & UX Trade-offs

### Visual Hierarchy
The mockups use a simple hierarchy based on:
- Top bars for state labeling and orientation
- High-contrast hero/summary panels for major tasks
- Card grouping for modular information scanning
- Banner messages for system feedback
- Clear primary action buttons for forward progress

### WCAG 2.1 Accessibility Considerations
The mockups were structured to support accessibility-oriented implementation:
- High contrast between text and background in most critical areas
- Text labels paired with fields instead of placeholder-only inputs
- Error and success states communicated with text, not color alone
- Large tap targets for buttons, chips, and navigation items
- Consistent layout to support predictability and recognition
- Simple reading order suitable for screen reader translation in implementation

### UX Trade-offs
- **Low-to-mid fidelity over branding:** prioritizes requirement traceability and interaction clarity.
- **Grouped story coverage:** some related stories were combined into one screen file to maintain coherence and reduce duplication.
- **Stakeholder feedback flow:** US-011 is represented as a review dashboard concept even though it is not a core fan-facing mobile action.
- **Offline scope:** offline behavior is intentionally constrained to already available/cached information, aligning with the stated requirement rather than implying full offline parity.
- **Rights-aware stream handling:** stream access is shown only when valid, avoiding speculative watch flows beyond stated requirements.

---

## Deliverables Generated
HTML mockups saved to the output directory `html/`:
- `auth_startup_mockup.html`
- `favorites_notifications_mockup.html`
- `news_sharing_mockup.html`
- `live_ticker_streams_mockup.html`
- `browse_details_offline_mockup.html`
- `unified_interface_feedback_mockup.html`

This report provides full traceability from the available user stories and functional requirements to the UI mockup deliverables.