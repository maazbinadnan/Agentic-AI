# 07_ui_mockups.md — LiveFootball UI Mockups & Interaction Design

## Section 1: Interaction Design Overview & Screen Architecture

LiveFootball is designed as a mobile-first, premium broadcast-style football companion for Android and iOS. The mockups translate the operational requirements, user stories, and visual design requirements into standalone HTML5 screens that can be opened directly from the `html/` subfolder.

### Core UX principles

1. **Fast match-day access**: the authenticated interface prioritizes live score cards, cached content, and skeleton/fallback states to support the two-second startup readiness target.
2. **Separated startup flow**: authentication/login and onboarding/personalization are represented as separate HTML mockups to keep sign-in fast and the preference setup optional and focused.
3. **Bottom-tab module integration**: the authenticated app uses a consistent five-tab navigation model: Home, Live, News, Teams, and Profile.
4. **Rights-compliant streaming**: live broadcast access is represented as third-party provider deep links only; unavailable, not-yet-started, and country-restricted states are explicit.
5. **Offline resilience**: cached-content banners, stale data indicators, disabled server-dependent controls, and reconnecting states prevent user misunderstanding under poor connectivity.
6. **Trust and GDPR clarity**: privacy controls, secure account cues, data export/delete workflows, and sharing payload minimization are surfaced in user-facing settings.
7. **Accessible sport data scanning**: live states use text labels plus color/iconography, score typography uses tabular numerals, and primary touch targets meet mobile accessibility guidance.

### Screen architecture

- **Authentication login**: startup login/registration tab, non-specific error handling, password recovery, social sign-in, privacy/legal access, and secure credential cues.
- **Onboarding preferences**: optional post-authentication club/channel preference setup with multi-select chips, skip action, GDPR cue, and offline-change guidance.
- **Home dashboard**: personalized match-day overview with favorite live match, cached/offline banner, personalized news, fallback/skeleton news, and upcoming fixtures.
- **Live match detail**: sticky match header, live score, event timeline, API error fallback, stale ticker indicator, stats, and authorized/suppressed stream access.
- **News article / sharing**: readable article page, cached article state, sticky share action, native share preview, and privacy-safe share payload explanation.
- **Team/player detail**: team header, follow state, overview/stat cards, player summary, league table excerpt, cached detail state, and unavailable-content fallback.
- **Stream rights state**: explicit display of three provider states: authorized deep link, broadcast not started, and rights not confirmed/suppressed.
- **Notification settings**: in-app toggles, OS permission-denied guidance, withdrawal/offline disabled-state handling.
- **Profile/privacy/offline**: personalization summary, cached content management, GDPR workflows, optional consent controls, and secure storage trust cues.

---

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `auth_login.html` | US-001, US-014, US-016 | Login/register tabs, non-specific authentication error banner, secure login button, Apple/Google continuation, password recovery, privacy/legal cue, post-login onboarding handoff |
| `onboarding_preferences.html` | US-002, US-003, US-009, US-012, US-014, US-016 | Favorite club search, sports channel multi-select chips, save/skip preferences actions, GDPR trust cue, offline-change guidance |
| `home_dashboard.html` | US-002, US-003, US-004, US-011, US-012, US-013, US-014 | Bottom tab navigation, personalized home dashboard, live match card, cached/offline status banner, shareable news card, skeleton fallback state, upcoming fixtures |
| `live_match_detail.html` | US-004, US-007, US-008, US-011, US-012, US-013, US-014 | Sticky live score header, live event timeline, API error fallback, stale/reconnecting warning, match stats, authorized DAZN link, suppressed rights state, disabled offline refresh |
| `news_article_share.html` | US-003, US-010, US-011, US-013, US-014, US-016 | News article layout, cached article banner, sticky share bar, native share sheet preview, privacy-safe share payload, cancellation-safe sharing explanation |
| `team_player_detail.html` | US-002, US-005, US-006, US-011, US-012, US-013, US-014 | Team broadcast header, follow state, overview tabs, season statistics grid, featured player card, league table excerpt, cached detail warning, unavailable-content fallback |
| `stream_rights_state.html` | US-007, US-008, US-014 | Stream provider cards, authorized deep-link button, broadcast-not-started disabled state, country-rights unavailable/suppressed state, compliance explanation |
| `notification_settings.html` | US-002, US-009, US-012, US-014, US-016 | Notification opt-in toggles, favorite-team event preferences, OS permission-denied alert, open-device-settings action, offline save-disabled state, consent withdrawal rationale |
| `profile_privacy_offline.html` | US-002, US-011, US-012, US-013, US-014, US-016 | Profile summary, offline mode indicator, personalization chips, server-dependent controls disabled offline, cached content inventory, GDPR privacy/export/delete workflows, secure storage trust cues |
| `auth_onboarding.html` | Traceability notice only | Previous combined file retained as a navigation/traceability notice pointing to `auth_login.html` and `onboarding_preferences.html`; not the final implementation reference |

---

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### 3.1 `auth_login.html` — Authentication startup

**Purpose:** Represent the first protected-app interaction. The screen keeps login/registration separate from onboarding so startup authentication remains focused and quick.

**Key components:**
- **Brand header:** football logo, LiveFootball wordmark, and compact performance cue: `Ready in under 2 seconds`.
- **Login/register segmented tabs:** communicates a simple startup auth flow without a heavy multi-screen wizard.
- **Authentication form:** email/password fields, remember-me checkbox, forgot-password link, primary secure login button, and Apple/Google continuation button.
- **Non-specific error banner:** rejects invalid credentials without exposing whether the email or password was incorrect.
- **Post-login handoff notice:** states that users proceed to a separate onboarding preferences screen after successful login or registration.
- **Privacy/legal cue:** plain-language privacy notice and secure credential handling cue.

**Interaction notes:**
- Login controls are at least 48px high to support mobile touch accessibility.
- The screen is intentionally optimized for a fast startup path and does not mix preference setup into credential entry.

### 3.2 `onboarding_preferences.html` — Personalization onboarding

**Purpose:** Represent the optional post-authentication preference setup for favorite clubs and sports channels.

**Key components:**
- **Step context:** indicates that onboarding follows authentication.
- **Favorite club search and chips:** searchable covered European clubs with multi-select favorite chips.
- **Preferred sports channel chips:** lets users tailor news sources and broadcast/provider relevance.
- **GDPR/offline trust cues:** states that privacy controls are available in Profile and offline changes are paused until connected.
- **Save and skip actions:** supports both immediate personalization and quick entry into the app.

**Interaction notes:**
- Club and channel chips are designed as multi-select controls.
- Preference saving is online/server-dependent; the UI includes offline warning language to align with US-012.
- The separate screen supports the operational requirement for uncomplicated login at app startup while still enabling personalization.

### 3.3 `home_dashboard.html` — Personalized match-day dashboard

**Purpose:** Provide the fastest route to relevant live match data, personalized news, and recent/fixture information after login.

**Key components:**
- **Sticky top area:** greeting, notifications shortcut, and search affordance.
- **Offline cached banner:** persistent but non-blocking `Offline - showing cached dashboard` state with timestamp.
- **Live hero card:** high-contrast live pill, favorite-team score, match minute, and disabled/controlled refresh affordance.
- **Personalized news card:** source/channel, cached time, thumbnail placeholder, and share action.
- **Skeleton fallback block:** illustrates lightweight startup/loading behavior for fresh content.
- **Bottom navigation:** Home, Live, News, Teams, Profile.

**Interaction notes:**
- The live match card provides direct access to the ticker.
- The Manage button routes to personalization settings.
- Cached and skeleton states prevent blank screens during poor connectivity or peak load.

### 3.4 `live_match_detail.html` — Live ticker and match detail

**Purpose:** Show near real-time football match state while handling API failure and legal streaming constraints.

**Key components:**
- **Sticky match header:** competition label, live match minute, team crests, team names, and score.
- **Reconnecting/stale warning:** explicit text indicator for last known live data.
- **Event timeline:** time, icon, event label, and explanatory description for goal, card, and half-time events.
- **API error fallback:** controlled alert communicating external live-data unavailability.
- **Broadcast access card:** authorized DAZN deep link and suppressed Sky Sport state.
- **Match stats card:** possession, shots, corners, and disabled offline refresh control.

**Interaction notes:**
- Live events use both icons and text; color is never the only event signal.
- External provider links are visually distinct in Link Blue and clearly presented as third-party navigation.
- Refresh is disabled offline so users do not assume a live API update occurred.

### 3.5 `news_article_share.html` — Article reading and native sharing

**Purpose:** Support personalized football news consumption and privacy-safe native sharing.

**Key components:**
- **Article header:** image placeholder, personalized/source metadata, headline, and readable body typography.
- **Cached article banner:** marks offline content and states which actions are unavailable.
- **Sticky share bar:** primary share action and secondary copy-link action.
- **Native share preview card:** demonstrates payload minimization: title, public URL, source, and no personal data.
- **Related cached match report card:** bridges news to match-report content.

**Interaction notes:**
- The share action is intended to invoke the native Android/iOS share sheet.
- Cancellation returns the user to the article without error.
- Personalization metadata, account identifiers, auth tokens, and notification preferences are excluded from the shared payload.

### 3.6 `team_player_detail.html` — Team/player/league context

**Purpose:** Provide detailed covered European club and player information, with graceful degradation when data is cached or unavailable.

**Key components:**
- **Broadcast-style team header:** club badge placeholder, league/country, team name, and follow button.
- **Horizontal section tabs:** Overview, Fixtures, Squad, Stats, News.
- **Cached warning:** timestamped stale-content state and explicit note that follow/unfollow requires connectivity.
- **Season statistics grid:** position, points, goal difference.
- **Featured player card:** player identity and compact player stats.
- **League table excerpt:** compact football table with clear row dividers.
- **Unavailable fallback:** message for temporary supported-detail endpoint failure.

**Interaction notes:**
- The follow button visually confirms personalization, while the cached warning prevents offline false saves.
- Tables use compact rows but maintain readable spacing and high contrast.

### 3.7 `stream_rights_state.html` — Broadcast rights and deep-link rules

**Purpose:** Isolate the stream access rules and make rights-compliant behavior easy to validate.

**Key components:**
- **Authorized provider card:** valid rights, broadcast begun, and active DAZN deep-link button.
- **Not-started card:** provider rights exist but link remains unavailable until broadcast start.
- **Rights-not-confirmed card:** link suppressed when country rights are missing, invalid, unavailable, or uncertain.
- **Compliance note:** reiterates that LiveFootball does not host or embed streams.

**Interaction notes:**
- Disabled provider buttons include explanatory labels rather than only greying out controls.
- The default behavior for uncertain metadata is suppression, matching the operational requirement.

### 3.8 `notification_settings.html` — Notification opt-in and permission handling

**Purpose:** Let users manage favorite-team notifications while respecting OS permission state and consent withdrawal.

**Key components:**
- **Global notification toggle:** shows combined in-app setting and device permission state.
- **Granular toggles:** goals/red cards, kickoff reminders, news/match reports.
- **Permission-denied alert:** clear guidance that operating-system permission is required.
- **Open device settings button:** route to platform settings.
- **Offline save-disabled state:** prevents server-dependent notification preference changes offline.

**Interaction notes:**
- Toggle labels are descriptive and avoid relying on icon-only controls.
- Consent withdrawal and notification disabling are framed as user-controlled actions.

### 3.9 `profile_privacy_offline.html` — Profile, privacy, and offline state

**Purpose:** Provide a single account hub for personalization, cached content, privacy rights, consent, and secure trust cues.

**Key components:**
- **Profile summary:** avatar, user name, secure account pill, and offline mode pill.
- **Personalization chips:** favorite clubs and preferred sports channels.
- **Disabled offline management button:** prevents false preference updates.
- **Cached content inventory:** news articles, team pages, and stale live ticker snapshots.
- **Privacy & GDPR controls:** privacy notice, export data, delete account, optional consent withdrawal.
- **Trust cues:** platform-secure/encrypted storage and privacy-safe sharing statement.

**Interaction notes:**
- GDPR workflows are intentionally prominent in Profile rather than hidden in legal-only pages.
- Offline mode disables server-dependent privacy/consent changes where immediate server confirmation is required.

---

## Section 4: Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

### Visual hierarchy

- **Live match information is primary:** score, match minute, and `LIVE` labels use the largest typography and highest contrast.
- **Cards organize information density:** news, stats, streams, privacy, and settings all use rounded cards for fast scanning.
- **Status messages are visually persistent:** offline, stale, reconnecting, and rights-restricted states are placed near the affected content, not hidden in global system messages.
- **Bottom navigation is always available:** authenticated screens use consistent tab labels and icons to support direct access to core modules.

### Accessibility choices

- **Contrast:** color combinations are selected to meet WCAG AA intent; dark theme uses light text on navy surfaces, and critical labels use high-contrast backgrounds.
- **Non-color-only status:** live, goal, red card, offline, rights unavailable, and error states include text and/or icons in addition to color.
- **Touch targets:** primary buttons, bottom tabs, switches, and icon buttons are designed around 48px minimum height.
- **Screen-reader support:** mockups include semantic elements, roles such as `alert`, `status`, `dialog`, and `navigation`, plus accessible labels for key icon-only buttons.
- **Text scaling:** layouts use flexible card structures and responsive grids to better tolerate larger text sizes.
- **Reduced cognitive load:** disabled states explain why an action is unavailable, especially for offline and rights-restricted cases.

### Performance-oriented UI decisions

- **Self-contained assets:** mockups avoid heavy images and use CSS gradients/placeholders to represent thumbnails, badges, and provider logos.
- **Separated startup screens:** login is no longer bundled with preference onboarding, reducing perceived startup complexity and keeping the first action focused.
- **Skeleton/fallback states:** the home dashboard demonstrates lightweight loading blocks to reduce perceived wait time.
- **Restrained animation:** only basic switch transition behavior is included; heavy transitions are avoided to preserve startup responsiveness.
- **Cached-first rendering:** offline screens show previously loaded content immediately with stale timestamps, supporting the app's limited-connectivity requirement.

### UX trade-offs

- **Separated login and onboarding vs. fewer files:** splitting authentication and onboarding creates clearer implementation references and a cleaner startup flow, while the retained `auth_onboarding.html` notice preserves traceability to the previous combined artifact.
- **Explicit rights restriction vs. hiding completely:** where useful, the UI shows that a stream exists but the link is suppressed. This improves transparency while still preventing unauthorized access.
- **Condensed typography vs. readability:** condensed styling reinforces the sports broadcast identity, but longer news text uses more readable body typography to avoid fatigue.
- **Offline read-only mode vs. queued changes:** the mockups block server-dependent actions offline rather than queuing silent updates, reducing the risk that users believe preferences or consent changes were saved.

---

## Generated HTML Files

The following standalone mockups were saved under:

`C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\hitl_agent\outputs\gpt-5.5\html\`

1. `auth_login.html`
2. `onboarding_preferences.html`
3. `home_dashboard.html`
4. `live_match_detail.html`
5. `news_article_share.html`
6. `team_player_detail.html`
7. `stream_rights_state.html`
8. `notification_settings.html`
9. `profile_privacy_offline.html`
10. `auth_onboarding.html` — retained as a traceability notice pointing to the split authentication and onboarding files.
