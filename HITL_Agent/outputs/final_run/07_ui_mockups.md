# 07_ui_mockups.md

## 1. Interaction Design Overview & Screen Architecture

This interaction design package translates the mobile football app user stories into responsive, self-contained HTML mockups aligned with the approved visual direction: **light theme**, **green accent**, **modern sans-serif typography**, **bottom tab navigation**, and a **sporty dynamic** mobile aesthetic.

### Design approach
- **Mobile-first architecture** using phone-frame mockups and responsive CSS grids.
- **Unified interface language** across all modules to satisfy the requirement for a consistent multi-module experience.
- **Bottom tab navigation** used as the persistent primary wayfinding pattern: **Home, News, Live, Streams, Profile**.
- **Fast-scanning content hierarchy** prioritizing scores, status tags, headlines, filters, and alert banners.
- **State-based design** included in every HTML file using side-by-side subcases:
  - primary/populated state
  - empty/unconfigured state
  - error/offline/restricted state

### Screen architecture
1. **Startup & Authentication**
   - Splash/startup readiness cues
   - Registration and login
   - Authentication error and blocked-access state
2. **Home / News / Personalization Hub**
   - Unified app landing experience
   - Favorite club and preferred channel selection
   - Personalized news feed
   - Unsupported selection and no-results handling
3. **Competitions / Team / Player Details**
   - National and international league browsing
   - Team and player detail pages
   - Unavailable competition/detail data state
4. **Live Match Center / Streams**
   - Live ticker event feed
   - Auto-refresh behavior representation
   - Scheduled-match empty state
   - API unavailable and geo-rights restricted stream state
5. **Notifications / Sharing / Offline**
   - Favorite-team notification opt-in
   - Device share sheet pattern
   - Offline cached-content experience
   - Unsupported sharing and restricted-notification activation

### Interaction principles reflected in the mockups
- **One-thumb usability:** primary controls are large, bottom-oriented, and touch-friendly.
- **Quick comprehension under live conditions:** high-contrast chips, status badges, and short text blocks support rapid reading.
- **Resilient UX:** users always receive clear feedback for unsupported, unavailable, offline, or restricted situations.
- **Consistency over novelty:** identical structural shells are preserved across modules to reflect system stability even when external data changes.

## 2. HTML Mockups to User Stories Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `startup_auth.html` | US-001, US-002 | Startup readiness badge, login form, registration form, OAuth/social buttons, remember me checkbox, GDPR consent checkbox, authentication error banner, blocked access state |
| `home_news_personalization.html` | US-003, US-004, US-005 | Unified home hub, bottom tab navigation, favorite club selection grid, preferred sports channel toggles, filter chips, personalized news cards, empty news state, unsupported selection error banner |
| `competitions_details.html` | US-006, US-007, US-018 | League and competition browser, national/international category chips, team details hero card, player statistics grid, empty preselection state, unavailable data state, structural consistency under data changes |
| `live_ticker_streams.html` | US-008, US-009, US-010, US-011 | Live ticker event feed, auto-refresh/live status badge, cached last-known state, scheduled match empty state, live stream CTA, broadcast-not-started state, geo-rights restriction banner |
| `notifications_sharing_offline.html` | US-012, US-013, US-014, US-015 | Favorite-team notification toggles, saved notification confirmation, notifications-off state, share CTA, device share sheet, unsupported share error, offline cached content message, retry connection action |

## 3. Detailed UI Screen Specifications & Component Breakdowns

### 3.1 `startup_auth.html`
**Purpose:** Represent app startup, quick readiness perception, onboarding entry, registration, login, and invalid authentication handling.

**Key components**
- Branded startup/auth hero area with readiness badge
- Email/password form fields
- Remember-me checkbox
- Password recovery link
- Apple and Google continuation buttons
- Registration form with GDPR consent checkbox
- Authentication status banners
- Persistent bottom navigation visual language for consistency

**Important interactions**
- User can choose login or registration at startup.
- Successful authentication conceptually unlocks app modules.
- Invalid credentials preserve the user in the authentication flow.
- Startup state visually reinforces the sub-2-second readiness requirement.

### 3.2 `home_news_personalization.html`
**Purpose:** Show how the authenticated user lands in a unified app shell and personalizes content by clubs and channels.

**Key components**
- Greeting/header region with notification affordance
- Filter chips for favorites, leagues, and channels
- Favorite-club selection cards
- Supported-channel toggle controls
- Personalized news feed cards with channel tags
- No-configuration and no-matching-news messages
- Unsupported selection rejection message

**Important interactions**
- User selects favorite teams and supported sports channels.
- Saved preferences shape the personalized feed.
- Unsupported teams/channels are rejected with explicit feedback.
- Unified module access is visually retained even when feed content is empty.

### 3.3 `competitions_details.html`
**Purpose:** Provide a browsing and drill-down experience for leagues, competitions, teams, and players.

**Key components**
- Competition filter chips
- Supported competitions list
- Team detail hero panel
- Player detail card with statistics
- Empty state for no selection yet
- Competition/team/player unavailable banners
- Recovery action list for retry and alternate browsing

**Important interactions**
- User browses national and international competitions.
- User opens team or player details from supported datasets.
- If data is unavailable, the interface remains stable and offers recovery paths.
- Layout consistency reflects robustness during external data changes.

### 3.4 `live_ticker_streams.html`
**Purpose:** Capture the live-match experience, including real-time updates and conditional stream availability.

**Key components**
- Match hero area with teams and scoreline
- Live/Upcoming badges
- Event timeline for ticker actions
- “Updated seconds ago” timestamping
- Stream card with rights-verified CTA
- Scheduled-match state with no stream link before broadcast start
- API unavailable banner with last cached state retained
- Geo-rights restriction state for blocked streams

**Important interactions**
- Live ticker updates automatically when new API data arrives.
- Last known match state remains visible when no new update is received.
- Stream links only appear after broadcast start.
- Stream links are suppressed when rights are not valid in the user’s country.

### 3.5 `notifications_sharing_offline.html`
**Purpose:** Show preference-based alerts, native sharing flow, and graceful operation under weak or absent connectivity.

**Key components**
- Favorite-team notification toggles
- Saved-preferences confirmation banner
- Notifications-off explanatory state
- Shareable news card
- Native device share-sheet representation
- Unsupported-share state
- Offline cached-content access card
- Online-content unavailable warning and retry action

**Important interactions**
- User manually enables notifications only for favorite teams.
- Users receive event alerts only when toggles are active.
- Sharing is available for supported content types only.
- Cached content remains available offline while fresh online-only content is blocked.

## 4. Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

### Visual hierarchy
- **Primary green CTA treatment** is reserved for core actions such as login, create account, open stream, share, and retry.
- **Red** is used sparingly for critical or restricted states such as auth errors, rights restrictions, and unavailable live data.
- **Blue/information accents** support non-critical informational states and metadata.
- **Large score typography** and **strong team-name emphasis** improve readability during live match use.
- **Rounded cards and clear spacing** reduce cognitive load in high-density sports content.

### Accessibility considerations
- Color selections are based on strong contrast against white and pale backgrounds to support **WCAG 2.1-oriented readability**.
- Components use **text plus color** for live, warning, and restricted states rather than relying on color alone.
- Touch targets are visually sized to approximately **44x44px or larger** for mobile use.
- Font hierarchy supports quick scanning with readable body text and strong headline differentiation.
- Error and empty states are explicit, concise, and action-oriented.
- Bottom navigation improves reachability for one-handed usage.

### UX trade-offs and rationale
- **Single-file multi-state screens** were used intentionally to satisfy design review efficiency and compare normal, empty, and failure cases side-by-side.
- **Moderate information density** balances match-day richness with readability on narrow mobile screens.
- **Subtle visual styling over heavy animation** supports perceived performance and battery efficiency.
- **Persistent structural consistency** was prioritized over highly customized per-module layouts to reinforce learnability and resilience.
- **Inline status banners** were favored over hidden toasts so that system conditions remain visible and reviewable in static mockups.

### Non-functional UX implications reflected visually
- **Performance perception:** startup readiness and lightweight card layouts reinforce the sub-2-second load expectation.
- **Scalability trust:** stable shells and preserved layouts suggest dependable operation during peak traffic.
- **Privacy trust:** GDPR consent and account-state messaging make lawful handling visible in the interface.
- **Offline resilience:** cached-content language ensures the product remains useful during connectivity loss.

## Deliverables generated
- `html/startup_auth.html`
- `html/home_news_personalization.html`
- `html/competitions_details.html`
- `html/live_ticker_streams.html`
- `html/notifications_sharing_offline.html`

These files are responsive, self-contained HTML mockups intended for design review, stakeholder walkthroughs, and downstream UI engineering alignment.