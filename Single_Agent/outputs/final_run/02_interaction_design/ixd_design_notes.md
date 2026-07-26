# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `startup_auth_mockup.html` | US-008 | Registration form, Login form, Minimal onboarding steps, Error/validation messages |
| `preferences_mockup.html` | US-001, US-007 | Favorite teams selection, Sports channels selection, Save preferences button, Notification toggle, Error/validation messages |
| `news_feed_mockup.html` | US-002, US-006 | Personalized news feed, News article cards, Share button (social media), Empty state, Error/validation messages |
| `live_ticker_mockup.html` | US-003 | Live ticker for favorite teams, Match cards with real-time updates, Empty state, Error/validation messages |
| `team_player_details_mockup.html` | US-004 | Team profile card, Player profile card, Detailed stats section, Empty state, Error/validation messages |
| `match_details_stream_mockup.html` | US-005 | Match details card, Live stream link (if permitted), Rights restriction message (if not permitted), Error/validation messages |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Preferences
A dedicated preferences page was chosen for clarity and ease of navigation, allowing users to select favorite teams, channels, and notification settings in one place. Modals could interrupt flow and limit visibility of options.

### Combined News Feed and Sharing
Sharing functionality is integrated directly into news article cards for efficiency, rather than a separate modal or page, reducing steps and keeping the flow seamless.

### Live Ticker as Separate Screen
Live ticker is a dedicated screen to avoid cluttering the news feed and to provide focused, real-time updates. This separation improves usability for users tracking matches.

### Conditional Live Stream Link Display
Live stream links are conditionally shown based on rights, with clear messaging if unavailable. This avoids confusion and sets user expectations.

### Minimal Onboarding for Registration/Login
Startup screen prioritizes minimal steps for registration/login, reducing friction and supporting quick access, as per user story requirements.
