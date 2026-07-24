# HTML Mockups

## Interaction Design Overview

### 1. Screen Architecture & Mapping
---ARCH_MAPPING---
| Screen / File Name | Mapped User Story / Requirement | Key Interactions & States Visualized |
| :--- | :--- | :--- |
| `startup_home_mockup.html` | US-001 | Splash/loading, error (low memory), main UI loaded |
| `personalized_news_feed_mockup.html` | US-002 | Favorite selection, personalized/general news, empty state |
| `live_ticker_mockup.html` | US-003 | Live ticker updates, no live matches state |
| `team_player_info_mockup.html` | US-004 | Team details, roster, player modal, recent results |
| `live_stream_link_mockup.html` | US-005 | Live stream link visible/hidden based on rights |
| `registration_login_mockup.html` | US-006 | Registration/login forms, validation, error/success states |
| `notifications_mockup.html` | US-007 | Notification enable/disable, confirmation state |
| `social_share_mockup.html` | US-008 | Share button, share dialog state |
| `offline_access_mockup.html` | US-009 | Offline banner, cached data, no data state |
| `feedback_mockup.html` | US-010 | Feedback form, rating, error/success states |
---END_ARCH_MAPPING---


### 2. UI/UX Design Notes & Trade-offs
---DESIGN_TRADEOFFS---
- **Startup/App Launch:** Used a centered splash with a spinner and clear error banner for low memory, per NFR. Main UI is stubbed for post-load state.
- **Personalized News Feed:** Favorites selection is prominent; news feed adapts to selection. Empty state message for no favorites.
- **Live Ticker:** Real-time updates visualized with a blinking dot and event list. No live matches state is clear and non-intrusive.
- **Team/Player Info:** Team page shows roster, stats, and results. Player modal overlays for details, accessible via keyboard.
- **Live Stream Link:** Stream link only shown if rights fulfilled; otherwise, a muted message. No speculative navigation.
- **Registration/Login:** Tabbed form, password toggle, error and success states inline. Only email/password shown due to lack of social login detail.
- **Notifications:** Simple switch for enable/disable, with confirmation. No granularity due to requirements gap.
- **Social Sharing:** Share button triggers dialog state. No platform icons due to unspecified platforms.
- **Offline Access:** Banner and cached data sections. No data state is explicit and user-friendly.
- **Feedback:** Form with textarea and star rating. Error and success states inline. No extra fields or flows.
---END_DESIGN_TRADEOFFS---


### 💾 Saved HTML Mockups
- `startup_home_mockup.html`
- `personalized_news_feed_mockup.html`
- `live_ticker_mockup.html`
- `team_player_info_mockup.html`
- `live_stream_link_mockup.html`
- `registration_login_mockup.html`
- `notifications_mockup.html`
- `social_share_mockup.html`
- `offline_access_mockup.html`
- `feedback_mockup.html`