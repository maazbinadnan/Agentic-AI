# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `preferences.html` | US-001 | Favorite teams selection grid, Sports channels selection list, Save preferences button, Sample error state for unsaved preferences |
| `dashboard.html` | US-002, US-008 | News feed for favorite teams, Live results ticker, Offline/cached data banner, Sample populated and empty states |
| `notifications.html` | US-003 | Notification toggle switch, Sample push notification preview, Error state for notification permission denied |
| `match_details.html` | US-004 | Match details card, Live stream link (if available), Rights restriction message (if not available) |
| `team_player_profile.html` | US-005 | Team profile section, Player profile section, Statistics table, Sample error state for missing data |
| `news_share.html` | US-006 | News article view, Share button, Social media platform selection modal, Error state for failed share |
| `startup.html` | US-007 | Splash screen, Loading indicator, Performance timer mockup |
| `gdpr.html` | US-009 | GDPR compliance info banner, Consent checkbox, Error state for missing consent |
| `login_register.html` | US-010 | Registration form, Login form, Quick access button, Validation error messages |
| `download_install.html` | US-011 | App store download buttons, Platform availability info, Install confirmation message |

---

## UI/UX Design Decisions & Trade-offs

### Preferences: Grid vs. List for Team Selection
Grid allows for quick visual scanning and selection, but may be less accessible for screen readers. List is more accessible but slower for users with many favorites. Grid chosen for speed and visual clarity.

### Dashboard: Combined News & Results vs. Separate Screens
Combining news and live results in one dashboard reduces navigation steps and aligns with user desire for quick access. Separate screens could allow deeper focus but would slow down information retrieval.

### Notifications: Toggle vs. Detailed Settings
Simple toggle switch is faster for most users and matches acceptance criteria. Detailed settings could offer more control but add complexity not requested.

### Live Stream Link: Inline vs. Modal
Inline display in match details keeps context and reduces navigation. Modal could highlight the link but adds unnecessary steps.

### Team/Player Profile: Tabs vs. Single Scroll
Tabs allow quick switching between team and player info, but single scroll is simpler and easier for wireframe fidelity. Single scroll chosen for clarity.

### News Sharing: Modal vs. Inline Dropdown
Modal for platform selection is clearer and prevents accidental sharing. Inline dropdown is faster but less explicit. Modal chosen for error handling and clarity.

### Startup: Splash Screen vs. Direct Dashboard
Splash screen with loading indicator helps visualize performance requirement. Direct dashboard would be faster but doesn't show startup state.

### GDPR Consent: Banner vs. Dedicated Screen
Banner is less intrusive and keeps user in flow, but dedicated screen ensures explicit consent. Banner with checkbox chosen for clarity and minimal disruption.

### Login/Register: Combined vs. Separate Forms
Combined form reduces navigation and matches 'quick' requirement. Separate forms could be clearer but slower. Combined chosen for speed.

### Download/Install: Platform Buttons vs. Text Links
Buttons are visually prominent and match app store conventions. Text links are less noticeable. Buttons chosen for clarity.
