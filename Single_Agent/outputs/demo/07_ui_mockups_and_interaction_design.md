# 7. UI Mockups & Interaction Design

## HTML Mockup to User Story Mapping

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `login.html` | US-001, US-010 | Login form, registration CTA, privacy notice link, validation messaging, offline startup banner |
| `dashboard.html` | US-002, US-003, US-009 | Personalized home feed, favorite teams chips, preferred channels, news cards, offline status, empty setup prompt |
| `live_ticker.html` | US-004, US-009 | Match header, scoreline, event timeline, refresh timestamp, no-live-match state, API/offline error state |
| `discovery_details.html` | US-005 | Competition list, team cards, player detail panel, search/filter bar, offline unavailable state |
| `streams_notifications.html` | US-006, US-007 | Broadcast cards, region-rights labels, stream CTA, notification toggles, permission warning, restricted state |
| `share_privacy.html` | US-008, US-010 | News/report detail card, share sheet buttons, unavailable share state, privacy summary, data protection indicators |

## Screen Layout Specifications

### 1. Login / Startup
- Primary purpose: enable rapid startup access to sign in or register.
- Layout: logo and performance badge at top, primary authentication card, secondary registration CTA, contextual privacy link.
- States: default populated form, invalid credential error, offline limited-start state.

### 2. Dashboard / Personalized Home
- Primary purpose: provide the central football information hub.
- Layout: top app bar, favorites summary chips, channel filters, featured news list, bottom navigation.
- States: personalized populated feed, unconfigured/empty feed prompting setup, offline cached-news state.

### 3. Live Ticker
- Primary purpose: surface real-time match information with minimal cognitive load.
- Layout: current match score header, event stream timeline, latest update timestamp, quick access tabs.
- States: active live match, no current live match, service unavailable/offline fallback.

### 4. Discovery & Details
- Primary purpose: enable exploration across leagues, competitions, teams, and players.
- Layout: search/filter controls, card-based lists, detail summary section, stat blocks.
- States: populated discovery/detail view, empty selection/search state, offline unavailable detail state.

### 5. Streams & Notifications
- Primary purpose: combine match access actions and proactive user-alert settings.
- Layout: live broadcast card with provider and rights status, stream CTA, notification preference switches, explanatory alerts.
- States: stream available with rights, stream unavailable due to start time/region, permission denied or offline state.

### 6. Share & Privacy
- Primary purpose: allow outbound sharing while reinforcing trust and compliance.
- Layout: article/report content summary, share action row, privacy info card, data-use explanation panel.
- States: share-ready state, sharing unavailable state, privacy/restricted info state.

## UI/UX Trade-offs

### Fast Access vs. Rich Onboarding
- The startup experience prioritizes quick entry with minimal fields to support the 2-second readiness target.
- Trade-off: deeper profile capture is deferred to later personalization screens to reduce launch friction.

### Personalization Depth vs. Simplicity
- Favorites and preferred channels are exposed as lightweight chips and toggles rather than complex nested preference trees.
- Trade-off: simpler controls improve usability but may limit advanced filtering in early releases.

### Real-Time Density vs. Readability
- The live ticker emphasizes recent key events, scoreline, and timestamping instead of overwhelming users with dense raw event feeds.
- Trade-off: this improves mobile readability while potentially hiding lower-priority event granularity.

### Legal Compliance vs. User Expectation
- Region-restricted stream states are explicit to avoid misleading users about inaccessible broadcasts.
- Trade-off: visible restrictions may disappoint users, but they improve transparency and legal compliance.

### Offline Resilience vs. Data Freshness
- Cached content remains visible during connectivity loss, paired with stale-state indicators.
- Trade-off: users retain app usefulness, but not all information remains current until reconnection.

### Sharing Convenience vs. Platform Dependence
- Native sharing entry points are favored for consistency across devices and social platforms.
- Trade-off: exact downstream presentation depends on the mobile OS and installed apps.