# 7. UI Mockups & Interaction Design

## HTML Mockup-to-User Story Mapping

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `onboarding_auth.html` | US-001 | Startup login form, registration form, validation error state |
| `home_news.html` | US-003, US-009 | Personalized feed, preference chips, cached content state, offline notice |
| `live_ticker.html` | US-004 | Live score header, event timeline, no-live-match state, provider failure state |
| `discover_details.html` | US-005 | Competition cards, team details, player detail preview, unavailable data state |
| `streams_notifications_settings.html` | US-002, US-006, US-007 | Stream link panel, rights restriction state, notification toggles, stream unavailable state |
| `sharing_profile.html` | US-008, US-002, US-009 | Share action entry point, profile summary, empty share state, offline fallback |

## Screen Layout Specifications

### 1. Onboarding & Authentication
- Entry screen for new and returning users.
- Primary actions: Log In, Create Account.
- Error state includes clear validation/credential feedback.
- Layout emphasizes rapid access at startup with minimal fields.

### 2. Home / Personalized News
- Displays selected preference chips at the top for context.
- News content is card-based for fast scanning.
- Empty state guides users toward preference setup.
- Offline state clearly distinguishes cached content from live content.

### 3. Live Ticker
- Scoreline and match minute are visually prioritized.
- Event feed uses a vertical timeline pattern for readability.
- Empty state handles periods with no live matches.
- Error state preserves last known data to maintain usefulness.

### 4. Discover & Details
- Supports broad browsing across competitions, teams, and players.
- Cards summarize the hierarchy of football entities.
- Error state addresses missing or unavailable detail data.
- Designed to scale to national and international coverage.

### 5. Streams, Notifications & Settings
- Combines lawful stream access with personalized alert controls.
- Populated state demonstrates official provider links only when eligible.
- Restricted state communicates rights-based unavailability clearly.
- Notification settings are shown as simple rows for low-friction management.

### 6. Sharing & Profile
- Sharing entry point is embedded in content context.
- Profile summary reinforces personalization persistence.
- Empty and offline/error states support graceful fallback behavior.

## UI/UX Trade-offs and Design Rationale
- **Speed vs. Density:** The layouts prioritize quick scanning and minimal startup friction over feature-dense dashboards.
- **Resilience vs. Real-Time Purity:** Offline and degraded states intentionally show cached or last known data to preserve utility during network/API issues.
- **Compliance vs. Convenience:** Stream availability is explicitly constrained by rights-based eligibility, which may reduce apparent availability but is necessary for lawful access.
- **Consistency vs. Modularity:** Shared visual patterns across screens support the requirement that modules remain consistent despite external server changes.
- **Personalization vs. Simplicity:** Preference controls are grouped into intuitive screens to avoid overcomplicating onboarding while still enabling tailored experiences.

## Interaction Notes
- Bottom-tab or primary navigation is recommended for Home, Live, Discover, and Profile areas.
- Pull-to-refresh is recommended for live and news screens when connectivity is present.
- Inline banners should be used for offline, degraded API, and rights restriction messages.
- Device-native share sheets and push-notification permissions should be used to align with Android and iOS behavior.
