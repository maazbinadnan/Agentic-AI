# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `login_registration_mockup.html` | US-001 | Login form (email/password), Social login buttons (Google, Apple, Facebook), Registration form, Error message for failed login |
| `preferences_mockup.html` | US-002 | Favorite teams selection (checkboxes/cards), Sports channels selection, Save preferences button |
| `news_feed_mockup.html` | US-003 | Filtered news list, News article cards, Empty state when no news matches preferences |
| `live_ticker_mockup.html` | US-004 | Live ticker for ongoing matches, Real-time update indicator, Empty state when no matches are live |
| `team_player_details_mockup.html` | US-005 | Team details section, Player details section, Sample stats and info |
| `live_stream_mockup.html` | US-006 | Live stream access button, Restricted access message, External player launch indicator |
| `share_mockup.html` | US-007 | Share button on news/match report, Social media options (Facebook, Twitter, WhatsApp), Native sharing dialog indicator |
| `notifications_mockup.html` | US-008 | Notification settings (toggle switches), Notification type selection, Sample push notification preview |
| `ui_consistency_mockup.html` | US-009 | UI module layout, Server update notification banner, Unchanged interface indicator |
| `module_configuration_mockup.html` | US-010 | Module configuration section, Official module add button, Third-party module attempt message |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Registration/Login
A dedicated page was chosen for clarity and accessibility, ensuring all login/registration options and error states are visible and easy to navigate.

### Checkboxes vs. Cards for Team/Channel Selection
Checkboxes provide quick selection and accessibility, while cards offer better visual grouping. Cards were used for teams, checkboxes for channels to balance clarity and speed.

### Inline Error Messages vs. Alert Banners
Inline error messages were used for login/registration to keep feedback close to the action, improving usability and reducing cognitive load.

### Real-time Updates Indicator
A subtle real-time update indicator was added to the live ticker to reassure users of ongoing updates without distracting from content.

### Restricted Live Stream Access Messaging
A clear message is shown when live streams are restricted, preventing confusion and setting user expectations.

### Native Sharing Dialog vs. Custom Share Modal
Native OS sharing dialog is indicated for best compatibility and accessibility, avoiding unnecessary custom UI complexity.

### Notification Settings as Toggles
Toggle switches are used for notification types for quick, accessible configuration, with a preview to clarify impact.

### Module Configuration: Official vs. Third-party
Official modules are clearly separated from third-party attempts, with explicit messaging to prevent user frustration.

### UI Consistency Banner
A subtle banner is used to indicate server updates without disrupting the interface, maintaining user trust and continuity.
