# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `registration_login_mockup.html` | US-001, US-011 | Registration form, Login form, Error message for invalid registration, GDPR consent checkbox |
| `favorites_preferences_mockup.html` | US-002 | Favorite teams selection, Sports channels selection, Save preferences button |
| `news_feed_mockup.html` | US-003 | Personalized news feed, News article cards, Empty state (no favorites selected) |
| `live_ticker_mockup.html` | US-004 | Live ticker for favorite teams, Match result cards, Empty state (no matches) |
| `team_player_details_mockup.html` | US-005 | Team details view, Player details view, Sample stats and info |
| `live_stream_mockup.html` | US-006 | Live stream link (permitted state), No stream available (not permitted state) |
| `notifications_settings_mockup.html` | US-007 | Notification toggle, Sample notification preview, Disabled state |
| `share_news_mockup.html` | US-008 | Share button on news article, Social media platform selection modal |
| `startup_performance_mockup.html` | US-009 | Splash/loading screen, Performance indicator (2s timer) |
| `offline_mode_mockup.html` | US-010 | Offline banner, Cached content display, Network lost indicator |
| `cross_platform_mockup.html` | US-012 | Android/iOS download buttons, Platform info section |

---

## UI/UX Design Decisions & Trade-offs

### Registration/Login Modal vs. Dedicated Page
A dedicated page was chosen for clarity and to allow for GDPR consent visibility. Modal could obscure legal text and error states.

### Favorites Selection UI: Checkbox vs. Card Grid
Card grid allows for visual team/channel branding, but checkboxes are more accessible. Card grid used for mid-fidelity wireframe.

### Live Ticker: Inline vs. Separate Screen
Separate screen chosen to avoid cluttering news feed and to allow real-time updates without distraction.

### Notifications Settings: Toggle vs. Multi-Option
Simple toggle used for clarity and to match acceptance criteria. Multi-option would add unnecessary complexity.

### Share Modal vs. Inline Dropdown
Modal chosen for platform selection to avoid accidental sharing and to provide clear feedback.

### Offline Mode Banner Placement
Banner placed at top for visibility, but not intrusive. Could be modal, but would block interaction.

### Splash Screen Performance Indicator
Timer indicator used to visualize 2s load requirement. Progress bar could be used, but timer is clearer for wireframe.

### Live Stream Link Visibility
Conditional rendering of stream link based on rights. Explicit error state shown when not permitted.

### Cross-Platform Download UI
Separate buttons for Android/iOS for clarity. Could use auto-detect, but explicit choice is clearer for wireframe.
