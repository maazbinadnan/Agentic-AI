# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `login_registration_mockup.html` | US-008 | Login form (email/password), Third-party authentication buttons (Google, Apple, Facebook), Error/validation states for login/registration |
| `main_dashboard_mockup.html` | US-009 | Unified navigation bar (News, Live Ticker, Streams, Teams/Players, Settings), Welcome header, Quick access cards/links to main features |
| `preferences_mockup.html` | US-001 | Favorite teams selection (checkboxes/list), Sports channels selection (checkboxes/list), Save preferences button, Sync status indicator |
| `news_mockup.html` | US-002, US-007 | News feed (list of articles), Offline/cached news indicator, Share buttons (Facebook, Twitter, WhatsApp), Error/empty state for no news |
| `live_ticker_mockup.html` | US-003 | Live ticker (real-time match results), Offline/cached results indicator, Error/empty state for no matches |
| `notifications_settings_mockup.html` | US-004 | Notification toggle switches (News, Results), Push notification preview, Error/validation state for notification settings |
| `match_stream_mockup.html` | US-005 | Match detail view, Live stream link (when available), Rights-compliance indicator, Error state (stream unavailable) |
| `team_player_details_mockup.html` | US-006 | Team profile card, Player profile card, Offline/cached info indicator, Error/empty state for no details |
| `privacy_settings_mockup.html` | US-010 | Data export request button, Data deletion request button, Data correction form, Status/confirmation messages, Error/validation states |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Preferences
Dedicated preferences page chosen for clarity and easier navigation, as users need to select multiple teams/channels and see sync status. Modal could be cramped and less accessible.

### Unified Navigation Bar vs. Drawer Menu
Unified navigation bar provides direct access to all main features (US-009) and is more discoverable for new users. Drawer menu could hide features and reduce usability.

### Inline Share Buttons vs. Share Menu
Inline share buttons (Facebook, Twitter, WhatsApp) are more visible and reduce extra taps, supporting US-007. Share menu could be more scalable but less immediate.

### Toggle Switches for Notification Settings
Toggle switches are intuitive for enabling/disabling notification types (US-004). Dropdowns or checkboxes could be less clear for binary choices.

### Error/Empty States Representation
Explicit error/empty states included in each mockup to fulfill acceptance criteria and improve user feedback. Omitting these would reduce clarity in edge cases.
