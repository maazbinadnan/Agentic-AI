# 07 UI Mockups & Interaction Design

## 1. Interaction Design Overview & Screen Architecture

The LiveFootball interaction design follows a **mobile-first, dark-mode, sporty dynamic** visual language aligned to the supplied design requirements. The screen architecture is built around rapid access to high-frequency football tasks: authentication, personalized discovery, live match tracking, rights-aware streaming, and privacy/feedback support.

### Screen Architecture
1. **Authentication / Onboarding**
   - Entry gate at startup with mandatory authentication before access.
   - Supports login/register patterns, validation states, consent acknowledgement, and quick social sign-in affordances.
2. **Home Dashboard**
   - Central landing screen prioritizing favorite-team news, live match status, and competition coverage.
   - Includes side-menu-oriented information architecture while preserving quick mobile shortcuts.
3. **Preferences & Notifications**
   - Dedicated configuration area for favorite clubs, preferred channels, and explicit notification opt-in.
   - Makes personalization state visible and editable.
4. **Live Ticker & Match Details**
   - Real-time match monitoring view with continuously refreshing events, score state, detailed statistics, team/player references, and lawful stream entry points.
5. **Privacy, Feedback & Offline Awareness**
   - Support-oriented view combining GDPR transparency, offline fallback messaging, cached-content communication, and feedback submission patterns.

### Interaction Principles
- **Fast scanning first:** live scores, timestamps, badges, and headlines use strong hierarchy and high contrast.
- **Persistent consistency:** navigation and module framing remain stable even when server data updates or fails.
- **Consent-aware UX:** notifications and personal-data processing are visually tied to user choice.
- **Graceful degradation:** offline, empty, and API-unavailable states are treated as first-class UI states.
- **Mobile responsiveness:** all screens collapse cleanly to narrow widths and preserve touch-friendly controls.

## 2. HTML Mockups to User Stories Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `auth_onboarding.html` | US-001, US-002, US-020 | Login/register switcher, mandatory authentication gate, validation error banner, password error state, remember me checkbox, OAuth buttons, GDPR consent notice |
| `home_dashboard.html` | US-004, US-005, US-006, US-016, US-018, US-019 | Side menu, mobile quick nav, personalized news feed, favorite club chips, preferred channel chips, live match cards, league coverage list, startup performance card, stable dashboard modules |
| `preferences_notifications.html` | US-003, US-013, US-014, US-020, US-021 | Favorite clubs selector, preferred sports channels selector, save action, notification opt-in toggle, alert-type settings, privacy information shortcut, sync failure state |
| `live_ticker_match_details.html` | US-007, US-008, US-009, US-010, US-011, US-012, US-015, US-018 | Real-time ticker event list, match score header, statistics cards, connectivity fallback banner, rights-aware stream panel, team/player detail cards, external stream CTA, share panel |
| `privacy_feedback_offline.html` | US-017, US-021, US-022, US-018, US-020 | Offline banner, cached-content indicators, in-app privacy notice cards, remote-content fallback messaging, feedback form, queued-for-sync state, consistency messaging |

## 3. Detailed UI Screen Specifications & Component Breakdowns

### 3.1 `auth_onboarding.html`
**Purpose:** Satisfies startup authentication requirements and prevents progression until login/registration is completed.

**Primary components**
- Branded splash-style hero area for large screens.
- Login/register segmented control.
- Email and password fields with invalid state example.
- Error banner showing failed authentication.
- Remember-me checkbox and forgot-password link.
- Primary login CTA.
- Google/Apple social auth buttons.
- GDPR/privacy consent acknowledgment card.

**Key interaction notes**
- Error states are non-destructive and allow immediate correction/resubmission.
- The consent copy clarifies privacy expectations without overwhelming the primary flow.
- Layout supports very quick visual comprehension to align with startup speed expectations.

### 3.2 `home_dashboard.html`
**Purpose:** Delivers the core personalized home experience once the user is authenticated.

**Primary components**
- Side-menu navigation for desktop/tablet and compact bottom quick navigation for mobile.
- Personalized feed module driven by saved favorite clubs and preferred channels.
- Empty-state example when no relevant news is currently available.
- Quick-action cards for favorites, channels, leagues, and alerts.
- Live match cards with strong score emphasis.
- Coverage panel listing national/international competitions and no-content state.
- Startup SLA / performance indicator and stable online-status chip.

**Key interaction notes**
- Content is deliberately grouped into modular cards so updated data can change without shifting overall screen structure.
- Quick actions reduce friction for common mobile tasks despite the side-menu design preference.
- A live matchday banner elevates high-priority, time-sensitive content.

### 3.3 `preferences_notifications.html`
**Purpose:** Central place for storing and updating personalization and consent settings.

**Primary components**
- Favorite-club selection grid.
- Preferred sports-channel selection grid.
- Save changes CTA.
- Notification opt-in control and alert subtype list.
- Preview widgets showing how personalization affects app output.
- Privacy information shortcut.
- Sync failure/offline-preservation message.

**Key interaction notes**
- The screen clearly separates **content preference** from **communication consent**.
- Preview widgets help users understand the practical effect of their choices.
- Error handling preserves confidence by stating local settings remain intact if synchronization fails.

### 3.4 `live_ticker_match_details.html`
**Purpose:** Supports real-time match following, detail exploration, lawful stream access, and social sharing.

**Primary components**
- Live status banner with last-refresh timestamp.
- Match hero header with competition, live minute, and score.
- Compact statistical summary cards.
- Event timeline with highlighted major event styling.
- Connectivity/API fallback warning.
- Streaming panel with rights-valid / broadcast-started visible state and hidden/suppressed state explanation.
- Team and player info cards.
- Share card simulating device-native share options.

**Key interaction notes**
- The event stream is optimized for vertical scrolling and quick scan patterns on matchday.
- Streaming access is clearly externalized to comply with the requirement to open provider deep links instead of embedding playback.
- Failure messaging preserves last known data and avoids interface disruption.

### 3.5 `privacy_feedback_offline.html`
**Purpose:** Makes privacy transparency, offline resilience, and continuous-improvement capture visible to users and stakeholders.

**Primary components**
- Prominent offline banner.
- Privacy information cards explaining what data is used, why, and how consent works.
- In-app fallback when remote privacy content is unavailable.
- Feedback submission form.
- Queued-for-sync state for offline submission.
- Cached-content status list distinguishing what remains available versus what requires connectivity.
- UI consistency note for malformed/external data changes.

**Key interaction notes**
- Offline communication is informative rather than alarming.
- Privacy details are chunked into digestible cards for readability on mobile.
- Feedback capture is designed to continue functioning under intermittent connectivity.

## 4. Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

### Visual Hierarchy
- **Primary emphasis:** scores, live status, and screen titles use bold weights and larger sizing.
- **Secondary emphasis:** metadata such as source, timestamps, and competition labels use smaller, muted text.
- **State cues:** green for selected/success states, amber for live/in-progress, blue for links/actions, red for errors and critical interruptions.
- **Card-based grouping:** rounded 12px+ containers and dark surfaces segment dense football data into scan-friendly modules.

### Accessibility Considerations
- High-contrast dark palette selected to maintain readability for headlines, labels, and status states.
- Touch targets are visually large and padded for mobile use.
- Form inputs include clear labels rather than placeholder-only guidance.
- Error states are shown with text, not color alone.
- Layouts are responsive and linearize into single-column flows for smaller screens.
- Semantic hierarchy is maintained with heading levels and grouped regions to support assistive technologies.
- Consent and privacy information are surfaced in plain language blocks to improve comprehension.

### UX Trade-offs
- **Side menu vs. mobile speed:** stakeholder preference for side menu is respected, but mobile quick-access navigation is also introduced to avoid excessive reach/click depth for live tasks.
- **Dense football data vs. readability:** card segmentation and strong typography balance compact information display with clarity.
- **Real-time richness vs. resilience:** live refresh cues are visible, but fallback states preserve last-known data to support unstable networks.
- **Legal stream discoverability vs. rights compliance:** stream calls-to-action are intentionally conditional and explanatory when hidden.
- **Fast startup vs. feature breadth:** the UI concept favors immediate utility and modular loading over heavy animation or decorative elements.

## Deliverables Generated
- `html/auth_onboarding.html`
- `html/home_dashboard.html`
- `html/preferences_notifications.html`
- `html/live_ticker_match_details.html`
- `html/privacy_feedback_offline.html`
- `07_ui_mockups.md`
