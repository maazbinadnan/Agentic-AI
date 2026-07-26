# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `startup_login_mockup.html` | US-008, US-009 | Splash screen with app logo and loading indicator, Quick registration form, Login form, Error state for invalid credentials, Loading state for app startup |
| `preferences_mockup.html` | US-001 | Preferences selection screen, Favorite teams selector (checkboxes or chips), Sports channels selector, Save button, Confirmation message for saved preferences, Error state for unsaved changes |
| `news_feed_mockup.html` | US-002, US-007, US-010 | Personalized news feed, News article cards, Share button on each article, Offline indicator/banner, Sample populated state with articles, Empty state when no news available, Error state for failed news loading |
| `live_results_mockup.html` | US-003, US-010 | Live ticker module, Match cards with real-time updates, Offline indicator/banner, Empty state when no matches, Error state for failed live updates |
| `notifications_settings_mockup.html` | US-004 | Notification settings toggle, List of notification types (news, results), Save button, Confirmation message, Error state for failed save |
| `match_details_mockup.html` | US-005 | Match details view, Live stream link (if available), Live stream unavailable message (rights restriction), Sample match stats, Error state for failed stream link loading |
| `team_player_profile_mockup.html` | US-006 | Team profile page, Player profile page, Detailed info and statistics, Sample populated state, Empty state for no data, Error state for failed data loading |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for Preferences
A dedicated preferences page was chosen for clarity and ease of navigation, allowing users to select favorite teams and channels without distraction. Modals can be disruptive and limit space for multiple selections.

### Share Button Placement
Share buttons are placed directly on news article cards for immediate access, supporting US-007. This avoids extra steps and keeps sharing contextual.

### Offline Banner vs. Disabled UI
An offline banner is used to indicate limited connectivity, but the UI remains interactive for previously loaded content (US-010). Disabling the UI would frustrate users and reduce perceived reliability.

### Live Stream Link Visibility
Live stream links are conditionally shown based on rights (US-005). When unavailable, a clear message is displayed instead of hiding the section, improving transparency.

### Splash Screen with Loading Indicator
A splash screen with a loading indicator is used to visually communicate app startup performance (US-009). This reassures users during the two-second load window.
