# UI Mockups & Interaction Design

## 1. Interaction Design Overview & Screen Architecture

The LiveFootball UI is designed as a mobile-first, responsive football companion experience optimized for Android and iOS devices. Following stakeholder feedback, each HTML mockup now presents **three separate screens/states** to better communicate interaction outcomes, edge cases, and state transitions.

### Updated design goals reflected in the mockups
- Show primary happy-path interactions alongside failure, empty, loading, offline, disabled, and confirmation states.
- Improve reviewability by separating key application states visually within each HTML deliverable.
- Support clearer traceability to edge-case and usability expectations identified in validation.
- Preserve fast, uncluttered mobile-first layouts aligned with the 2-second readiness target.

### Screen architecture
1. **Authentication / startup**: `login.html`
2. **Personalized home overview**: `home_dashboard.html`
3. **Filtered news feed**: `news.html`
4. **Realtime match tracking and league browsing**: `live_ticker.html`
5. **Match, team, player, stream, and share details**: `details.html`
6. **Preferences, favorites, and alerts management**: `preferences_notifications.html`

## 2. HTML Mockups to States Mapping Table

| HTML File | State 1 | State 2 | State 3 |
|---|---|---|---|
| `login.html` | Initial login screen | Failed login state | Successful login / redirect state |
| `home_dashboard.html` | Personalized dashboard | Offline / cached-content dashboard | First-use / no favorites state |
| `news.html` | Loaded personalized news feed | No-results state | Loading / refreshing state |
| `live_ticker.html` | Active live match | Upcoming / pre-match state | Offline or unsupported state |
| `details.html` | Loaded match/team/player details | Stream rights restricted state | Share interaction state |
| `preferences_notifications.html` | Configured preferences | Notifications disabled state | Preferences saved confirmation |

## 3. Detailed UI Screen Specifications & Component Breakdowns

### 3.1 `login.html`
- **State 1:** Initial login form with email/password entry and account creation CTA.
- **State 2:** Failed login with explicit credential error feedback and retry/reset paths.
- **State 3:** Successful authentication confirmation with redirect to personalized home.

### 3.2 `home_dashboard.html`
- **State 1:** Standard personalized dashboard with favorites, live summary, and tailored news.
- **State 2:** Offline/cached mode clarifying stale data and unavailable live updates.
- **State 3:** Empty first-use dashboard prompting setup of favorite clubs and channels.

### 3.3 `news.html`
- **State 1:** Populated filtered feed with readable cards and sharing/read actions.
- **State 2:** Empty/no-results state when filters produce no matching stories.
- **State 3:** Loading/refresh state using skeleton placeholders.

### 3.4 `live_ticker.html`
- **State 1:** Active live match view with score and event timeline.
- **State 2:** Upcoming match view prior to kickoff.
- **State 3:** Offline/unavailable state showing connection and coverage constraints.

### 3.5 `details.html`
- **State 1:** Full match/team/player detail presentation.
- **State 2:** Stream rights restriction state for ineligible territories.
- **State 3:** Share-sheet interaction state for news or match report distribution.

### 3.6 `preferences_notifications.html`
- **State 1:** Existing configured preferences and enabled personalization.
- **State 2:** Notifications disabled explanation state.
- **State 3:** Save-success confirmation after updating settings.

## 4. Accessibility & UX Notes
- Multi-state mockups improve clarity around outcomes, errors, and edge conditions.
- Error, offline, and disabled states use text and structure in addition to color.
- Confirmation states reduce ambiguity after critical actions such as login and saving preferences.
- Empty/loading states support realistic mobile usage flows and validation of edge cases.

## Deliverables Generated
- `html/login.html`
- `html/home_dashboard.html`
- `html/news.html`
- `html/live_ticker.html`
- `html/details.html`
- `html/preferences_notifications.html`

Each HTML deliverable now includes **three separate screens/states** in response to stakeholder feedback.