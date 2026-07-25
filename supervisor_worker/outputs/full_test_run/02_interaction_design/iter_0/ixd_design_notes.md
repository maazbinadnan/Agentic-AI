# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `registration_login_mockup.html` | US-008, US-011 | Registration form (email/password, Google, Apple, Facebook), Login form, Password recovery modal, GDPR consent prompt |
| `preferences_mockup.html` | US-001 | Favorite teams selection grid, Sports channels selection list, Save preferences button |
| `news_feed_mockup.html` | US-002, US-006 | Personalized news feed, News article cards, Share button (social media options) |
| `live_results_mockup.html` | US-003 | Live ticker module, Match updates list, Sample match in progress |
| `match_details_mockup.html` | US-004 | Match details view, Live stream link (conditional), No rights alert banner |
| `team_player_profile_mockup.html` | US-005 | Team profile page, Player profile page, Detailed info sections |
| `notifications_settings_mockup.html` | US-007 | Notification type toggles, Quiet hours time picker, Save notification settings |
| `offline_sync_mockup.html` | US-010 | Offline banner, Previously loaded content, Sync status indicator |
| `performance_mockup.html` | US-009, US-013 | App launch splash screen, Performance status indicator, Peak usage info |
| `support_feedback_mockup.html` | US-014, US-015 | Support section (FAQs, contact form), Feedback submission form, Testing status badge |
| `privacy_settings_mockup.html` | US-016 | GDPR consent toggles, Data deletion request button, Data export request button |
| `platform_availability_mockup.html` | US-012 | Platform download links (Android/iOS), Feature parity info |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Password Recovery
A modal is used for password recovery to keep the user in context and reduce navigation friction. Pros: Faster, less disruptive. Cons: May be less discoverable for some users.

### Conditional Live Stream Link Visibility
Live stream link is shown only if rights are fulfilled; otherwise, an alert banner is displayed. Pros: Clear compliance, avoids user frustration. Cons: May require extra logic for country detection.

### Grid vs. List for Team Selection
Grid layout for favorite teams allows quick visual scanning and selection. Pros: Efficient, visually engaging. Cons: May be less accessible for screen readers.

### Share Button Placement
Share button is placed on each news article card for immediate access. Pros: Encourages sharing, easy to find. Cons: May clutter UI if too many articles.

### Quiet Hours Time Picker
Time picker for quiet hours allows granular control. Pros: Flexible, user-friendly. Cons: Slightly more complex UI.

### Offline Banner vs. Hidden State
Offline banner is used to inform users of limited connectivity. Pros: Transparency, user awareness. Cons: May take up screen space.

### Testing Status Badge
Badge indicates app testing status for transparency. Pros: Builds trust. Cons: May be ignored by users.
