# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `startup_auth_mockup.html` | US-008 | Splash screen, Registration form, Login form, Minimal steps flow, Error/validation states |
| `main_navigation_mockup.html` | US-009 | Main navigation bar (News, Live Ticker, Streams, Teams/Players), Direct access buttons, Active state indication |
| `preferences_mockup.html` | US-001 | Favorite teams selection, Sports channels selection, Save preferences button, Sample populated state, Validation/error state |
| `news_mockup.html` | US-002, US-007 | News feed for favorite teams, News article cards, Share button (social media), Empty state, Populated state, Error state |
| `live_ticker_mockup.html` | US-003 | Live match ticker for favorite teams, Match cards with real-time scores, Empty state, Populated state, Error state |
| `notifications_mockup.html` | US-004 | Notification toggle, Push notification settings, Sample notification preview, Error/validation state |
| `match_stream_mockup.html` | US-005 | Match detail view, Live stream link (rights available), Rights unavailable state (link hidden), Error state |
| `team_player_details_mockup.html` | US-006 | Team profile page, Player profile page, Detailed statistics, Sample populated state, Empty/error state |
| `settings_customization_mockup.html` | US-010 | Module configuration toggles, Interface connection options, Save configuration button, Populated state, Error/validation state |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Registration/Login
Chose dedicated startup screen for registration/login to minimize steps and avoid modal complexity, aligning with US-008's 'minimal steps' requirement.

### Navigation Bar Placement
Used persistent bottom navigation for direct access to main features (US-009), improving discoverability and reducing navigation friction.

### Favorites Selection UI
Used checkboxes and multi-select lists for teams/channels to maximize clarity and minimize accidental selection, supporting error/validation states.

### Live Stream Link Visibility
Stream link only shown when rights are available (US-005); error/rights-unavailable state is visually distinct to prevent confusion.

### Share Button Placement
Share button placed on each news/game report card for immediate access, supporting US-007's sharing flow without cluttering the UI.

### Settings Customization UI
Used toggles and checklists for module configuration (US-010) to allow granular personalization without overwhelming the user.
