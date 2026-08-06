# 07 UI Mockups and Interaction Design

## 1. Interaction Design Overview & Screen Architecture

This revised interaction design package translates the approved functional requirements and agile user stories for the LiveFootball mobile application into low-to-mid fidelity responsive HTML mockups. The update resolves the review issues by adding explicit success transitions, applied-configuration feedback, notification activation and delivery states, connection-restored behavior, and stronger semantic control guidance.

### Revision Summary Against IxD Review

- **US-002 fixed:** startup screens now show successful login and successful registration outcomes that explicitly grant access to the app and indicate the destination state after access.
- **US-009 fixed:** personalization screens now include a visible notification activation control, saved preference confirmation, and a delivered notification example for a favorite-team event.
- **US-008 fixed:** modular interface screens now include actual configuration controls, a save action, and confirmation that the saved arrangement has been applied while fixed components remain preserved.
- **US-011 fixed:** live ticker screens now include a reconnection/resume-update state demonstrating automatic online recovery after temporary offline use.
- **Accessibility improved:** interactive items previously shown as generic `div` elements are now represented with semantic `form`, `label`, `input`, `button`, and `a` elements, plus visible focus styling and aria labels in the mockups.

### Screen Architecture Summary

1. **Startup & Authentication**
   - Entry point for Android and iOS users.
   - Covers startup access, registration, login, validation failures, and successful access transitions.

2. **Personalization, News, Notifications & Sharing**
   - Supports favorite team and channel selection.
   - Displays personalized football news.
   - Includes notification toggle, saved confirmation, delivered push state, and social sharing affordances.

3. **Live Ticker, Match Center & Stream Rights Handling**
   - Displays real-time live ticker updates.
   - Shows pre-match empty state.
   - Handles live data unavailability, restricted live streams, offline continuity, and reconnection recovery.

4. **Browse Coverage & Modular Interface Configuration**
   - Supports browsing of leagues, competitions, teams, and players.
   - Shows detailed team/player information.
   - Represents configurable modules with save/apply controls while preserving fixed components.

5. **Feedback & Support Review**
   - Represents support-team-side access to user feedback and app review inputs.
   - Includes populated, empty, and ingestion error states.

All mockups use a common responsive grid pattern and include at least three states per file:
- Populated state
- Empty/unconfigured state
- Error, offline, or restricted state

## 2. HTML Mockups to User Stories Mapping Table

| HTML Mockup File | User Stories Covered | Functional Requirements Covered | Notes |
|---|---|---|---|
| `startup_auth_mockup.html` | US-001, US-002 | FR-001, FR-002 | App startup, supported device access, registration, login, validation failure, success access transition |
| `personalization_news_mockup.html` | US-003, US-004, US-009, US-010 | FR-003, FR-004, FR-009, FR-010 | Favorites, channels, personalized news, notification toggle and delivery, semantic share actions |
| `live_ticker_streams_mockup.html` | US-005, US-007, US-011 | FR-005, FR-007, FR-011 | Real-time live ticker, stream rights gating, offline continuity, restored-connection resume state |
| `browse_details_interface_mockup.html` | US-006, US-008 | FR-006, FR-008 | Browse leagues/teams/players and configure modular interface with save/apply confirmation |
| `feedback_support_mockup.html` | US-012 | FR-012 | Feedback intake and review analysis view |

### Complete User Story Coverage Check

| User Story | Covered In |
|---|---|
| US-001 | `startup_auth_mockup.html` |
| US-002 | `startup_auth_mockup.html` |
| US-003 | `personalization_news_mockup.html` |
| US-004 | `personalization_news_mockup.html` |
| US-005 | `live_ticker_streams_mockup.html` |
| US-006 | `browse_details_interface_mockup.html` |
| US-007 | `live_ticker_streams_mockup.html` |
| US-008 | `browse_details_interface_mockup.html` |
| US-009 | `personalization_news_mockup.html` |
| US-010 | `personalization_news_mockup.html` |
| US-011 | `live_ticker_streams_mockup.html` |
| US-012 | `feedback_support_mockup.html` |

## 3. Detailed Screen Specifications & Component Breakdowns

### 3.1 `startup_auth_mockup.html`
**Stories:** US-001, US-002  
**Requirements:** FR-001, FR-002

**Primary components:**
- App brand/header area
- Mobile platform support cue
- Login form fields using semantic input controls
- Registration form fields using semantic input controls
- Primary and secondary action buttons
- Validation or access failure messaging
- Success confirmation banner showing that app access is granted
- Destination-preview card showing transition into the authenticated app experience

**States included:**
- Populated sign-in state with successful login outcome
- Empty first-use registration state with successful account creation outcome
- Error state for failed access or invalid login

### 3.2 `personalization_news_mockup.html`
**Stories:** US-003, US-004, US-009, US-010  
**Requirements:** FR-003, FR-004, FR-009, FR-010

**Primary components:**
- Favorite team selection controls
- Preferred sports channel selection controls
- Save preferences action
- Explicit notification activation toggle
- Saved preference confirmation banner
- Personalized article cards
- Received notification example for a relevant favorite-team event
- Share links for supported social channels only

**States included:**
- Populated personalized feed with notifications enabled and preferences saved
- Empty onboarding/setup state without saved preferences
- Delivery/error state showing received alert, permission issue, unsupported share availability, and cached content fallback

### 3.3 `live_ticker_streams_mockup.html`
**Stories:** US-005, US-007, US-011  
**Requirements:** FR-005, FR-007, FR-011

**Primary components:**
- Match score summary
- Real-time event timeline
- Stream availability link
- Rights restriction messaging
- Offline continuity messaging
- Reconnection confirmation banner
- Post-recovery event refresh example

**States included:**
- Populated live match center with ongoing updates
- Empty/pre-match state before ticker begins
- Error/restricted/reconnected state for unavailable API data, rights-ineligible stream, offline mode, and resumed updates after connection restoration

### 3.4 `browse_details_interface_mockup.html`
**Stories:** US-006, US-008  
**Requirements:** FR-006, FR-008

**Primary components:**
- League/competition list
- Team detail panel
- Player summary badge
- Module configuration controls using checkboxes
- Fixed vs optional module indicators
- Save layout action
- Applied configuration confirmation state

**States included:**
- Populated browse and configured module state with applied save confirmation
- Empty state before selection/configuration
- Error/preservation state with unavailable detail data and automatic retention of fixed components

### 3.5 `feedback_support_mockup.html`
**Stories:** US-012  
**Requirements:** FR-012

**Primary components:**
- Feedback review cards
- Source labels
- Issue/improvement tags
- Empty feedback placeholder
- Data ingestion failure message

**States included:**
- Populated support analysis state
- Empty state with no feedback records
- Error state when feedback source is unavailable

## 4. Visual Hierarchy, WCAG 2.1 Accessibility, & UX Trade-offs

### Visual Hierarchy
- Each screen uses a clear top bar with feature name and state label to support design review and traceability.
- Primary actions are visually emphasized with filled buttons or highlighted control groups.
- Content is grouped using cards, banners, and spacing to separate configuration from live content.
- Edge-case messaging uses warning and error surfaces placed near the affected content area.
- Success transitions are now made explicit with green confirmation banners and follow-on destination cues.

### WCAG 2.1 Accessibility Considerations
- High-contrast text/background combinations are used for legibility.
- Buttons, toggles, links, checkboxes, and chips are shown using semantic interactive elements instead of presentation-only containers.
- Visible focus outlines are included in the mockup CSS to communicate keyboard navigation expectations.
- Labels and `aria-label` usage are included for key controls where the textual cue may otherwise be ambiguous.
- Status messages are grouped in bordered banners for clear recognition and can be implemented with appropriate live-region semantics.
- Layouts are responsive via CSS Grid and remain readable at varying widths.
- Information is not conveyed by color alone; labels such as “Success Access,” “Received Alert,” “Offline mode active,” and “Connection restored” provide text equivalents.

### UX Trade-offs
- Multiple related stories remain grouped into composite mockups where workflows are tightly connected, reducing duplication while preserving explicit traceability.
- Low-to-mid fidelity presentation continues to favor requirement validation and state coverage over exact visual brand styling.
- Some back-office/support representations are still shown in a mobile frame for consistency with the required deliverable format, even though operational tooling may later be designed for web/admin contexts.
- Reconnection and successful-save transitions are represented as explicit state panels rather than animation sequences, because the deliverable format is static HTML rather than executable prototype logic.

## Delivered Files
- `html/startup_auth_mockup.html`
- `html/personalization_news_mockup.html`
- `html/live_ticker_streams_mockup.html`
- `html/browse_details_interface_mockup.html`
- `html/feedback_support_mockup.html`
- `07_ui_mockups_and_interaction_design.md`
