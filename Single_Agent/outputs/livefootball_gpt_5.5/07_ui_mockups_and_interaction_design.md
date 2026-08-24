# 7. UI Mockups & Interaction Design Report

## Interaction Design Overview
The mockups define a mobile-first LiveFootball experience optimized for rapid startup, direct access to live football information, personalization, legal streaming access, notification control, offline resilience, and privacy management. Each HTML file is standalone and responsive, using embedded CSS and light JavaScript to demonstrate critical interactions.

## HTML Mockup-to-User Story Mapping

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `login.html` | US-001, US-002, US-003, US-015 | Login/register tabs, account form, favorite-club onboarding chips, startup performance note, privacy/GDPR notice |
| `dashboard.html` | US-001, US-003, US-005, US-007, US-012, US-013, US-016 | Personalized home, favorite match cards, live status, top news, notification summary, preferred channel chips |
| `news.html` | US-004, US-005, US-006, US-014 | Personalized news filters, article cards, share buttons, cached fallback warning, preferred source chips |
| `live_ticker.html` | US-007, US-014, US-018 | Live score panel, refresh status, chronological events, simulated API update, reconnecting/last-known-state message |
| `match_details_streams.html` | US-007, US-011, US-014 | Match summary, provider links, country rights check, disabled restricted stream states, cached match facts |
| `team_player_details.html` | US-008, US-009, US-010, US-014 | Search field, team profile, statistics, fixtures/results, squad list, interactive player profile panel |
| `settings.html` | US-003, US-004, US-012, US-013, US-015, US-017 | Notification toggles, personalization settings, privacy center actions, feedback/support submission |

## Screen Layout Specifications

### `login.html`
- **Purpose:** Supports uncomplicated startup authentication and initial personalization.
- **Primary Components:** Brand hero, login/register segmented control, email/password fields, session persistence option, third-party sign-in placeholder, club chips, privacy note.
- **Key Interactions:** Toggle login/register mode; submit authentication demo; select favorite clubs conceptually.
- **Requirement Coverage:** Startup, authentication, personalization, GDPR transparency.

### `dashboard.html`
- **Purpose:** Serves as the central football hub after login.
- **Primary Components:** Personalized hero, live match cards, top news module, notification summary, preferred channel display, bottom navigation.
- **Key Interactions:** Access live matches, open stream area, manage favorites.
- **Requirement Coverage:** Fast central information access, favorite-team focus, news, live ticker entry, notifications.

### `news.html`
- **Purpose:** Displays current football news filtered by favorite teams and preferred sports channels.
- **Primary Components:** Filter chips, article cards, source/time metadata, share actions, cached fallback banner.
- **Key Interactions:** Filter source/team context; invoke native share sheet when supported.
- **Requirement Coverage:** Personalized news, source preferences, social sharing, offline fallback.

### `live_ticker.html`
- **Purpose:** Demonstrates real-time match updates and external API resilience.
- **Primary Components:** Live score header, match clock, connection/refresh status, event timeline, simulated API update.
- **Key Interactions:** Simulate receipt of new API event; show reconnecting state while preserving last data.
- **Requirement Coverage:** Live ticker, real-time refresh, API validation, graceful outage state.

### `match_details_streams.html`
- **Purpose:** Presents match facts and legally governed stream-link availability.
- **Primary Components:** Match score summary, rights-check banner, provider list, enabled/disabled stream buttons, restriction messages.
- **Key Interactions:** Open authorized provider link; view blocked/restricted state.
- **Requirement Coverage:** Broadcast-start gating, country rights compliance, transparent unavailable states.

### `team_player_details.html`
- **Purpose:** Shows team and player information with cached profile indicators.
- **Primary Components:** Search input, team statistics, fixture/result list, squad list, interactive player profile panel.
- **Key Interactions:** Select a player to render player profile details.
- **Requirement Coverage:** League/team/player coverage, search-oriented navigation, partial data handling.

### `settings.html`
- **Purpose:** Allows users to configure notifications, personalization, privacy, and support/feedback.
- **Primary Components:** Notification switches, favorite-club/channel summary, privacy center actions, account deletion request, feedback button.
- **Key Interactions:** Toggle notification categories; submit feedback; access privacy center.
- **Requirement Coverage:** Notification preferences, GDPR rights, support diagnostics, continuous improvement.

## UI/UX Trade-offs

### Mobile-First Over Desktop Complexity
- **Decision:** Mockups prioritize mobile layout and bottom navigation because the product is a mobile app.
- **Trade-off:** Desktop layouts are supported responsively, but advanced desktop-specific interactions are intentionally limited.

### Dashboard Aggregation Over Deep Navigation
- **Decision:** The dashboard aggregates live scores, news, channels, and notification state.
- **Trade-off:** Aggregation improves speed but requires clear visual hierarchy to avoid information overload.

### Legal Transparency for Streams
- **Decision:** Restricted streams are shown as disabled with explanatory text rather than silently hidden in the mockup.
- **Trade-off:** Transparency improves trust and supportability; final legal guidance may prefer full hiding in some markets.

### Cached Fallback Messaging
- **Decision:** Offline/cached states are visible in news, ticker, and profile screens.
- **Trade-off:** This may add visual noise during normal use, but it clarifies resilience behavior under poor connectivity.

### Lightweight JavaScript for Demonstration
- **Decision:** Mockups use minimal inline JavaScript for tab switching, live-event simulation, player selection, and sharing demonstration.
- **Trade-off:** This keeps files standalone while avoiding production framework assumptions.

## Accessibility and Usability Notes
- Use high-contrast green/dark palette and large tap targets.
- Maintain semantic headings and labels for core forms.
- Ensure future production implementation provides screen-reader labels for icons, focus states, dynamic live-region announcements for ticker events, and OS-level notification permission explanations.

## Recommended Next UI Activities
1. Validate navigation model with 5-8 representative football fans.
2. Define exact content hierarchy for match day versus non-match day.
3. Prototype native notification permission flows for iOS and Android.
4. Conduct accessibility review against WCAG 2.1 AA.
5. Align stream-link UX with legal and provider-branding constraints.
