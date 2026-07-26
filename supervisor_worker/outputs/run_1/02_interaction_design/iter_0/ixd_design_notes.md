# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `preferences.html` | US-001 | Favorite teams/channels selection list, Add/remove/update controls, Selection limit error message, Save button |
| `news_feed.html` | US-002, US-007 | Personalized news feed, News article cards, Share button/modal for each article |
| `live_ticker.html` | US-003 | Live ticker module, Match updates list, Real-time indicator |
| `team_player_profiles.html` | US-004 | Team list, Player list, Profile detail modal/page, Statistics section |
| `live_stream.html` | US-005 | Live stream access panel, Stream link/button, Unavailable message for restricted regions |
| `notification_settings.html` | US-006 | Notification type toggles, Enable/disable notifications, Sample notification preview |
| `login_register.html` | US-008 | Email/password login form, Social login buttons, Registration form, Error/validation messages |
| `splash_loading.html` | US-009 | Splash screen, Loading indicator, Performance timer |
| `offline_mode.html` | US-010 | Offline status banner, Cached content display, Last update time indicator |
| `server_update_consistency.html` | US-011 | Consistency check banner, Module status indicators |
| `privacy_gdpr.html` | US-012 | Privacy policy section, Data deletion request form, Confirmation modal |
| `platform_availability.html` | US-013 | Platform badges (Android/iOS), Store links, Availability info |
| `performance_concurrency.html` | US-014 | Performance status banner, Concurrent user indicator |
| `support_stability.html` | US-015 | Support resources section, Contact/help links, App stability info |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Team/Player Profiles
Used dedicated pages for detailed profiles to allow richer statistics and easier navigation, avoiding modal clutter.

### Share Button Placement
Placed share buttons directly on news cards for quick access, balancing visibility and avoiding excessive UI elements.

### Error Messaging for Selection Limits
Used inline error messages near selection controls for immediate feedback, improving usability.

### Offline Banner vs. Popup
Chose persistent banner for offline status to avoid interrupting user flow, ensuring awareness without annoyance.

### Splash Screen Loading Indicator
Used simple spinner and timer to communicate fast loading, avoiding unnecessary animation that could slow perceived performance.

### Notification Settings Granularity
Provided toggle switches for each notification type, balancing user control and interface simplicity.

### Support Access Location
Placed support links in a dedicated section for discoverability, avoiding clutter in main navigation.
