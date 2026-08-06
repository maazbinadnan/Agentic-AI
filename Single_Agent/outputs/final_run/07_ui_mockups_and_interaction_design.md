# 7. UI Mockups and Interaction Design

## HTML Mockup-to-User Story Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `auth_preferences.html` | US-001, US-002, US-008, US-010 | Startup login form, registration CTA, favorite team/channel chips, notification toggles, offline preference state, retry sync action |
| `news_dashboard.html` | US-003, US-005, US-009 | Personalized news feed, category tabs, article cards, empty-state personalization prompt, share action and share failure state |
| `live_match.html` | US-004, US-006, US-007, US-010 | Live score header, event timeline, no-live-match state, delayed live data warning, rights-restricted stream state, retry action |

## Screen Layout Specifications

### 1. `auth_preferences.html`
- **Primary Purpose:** Support low-friction startup access and preference setup.
- **Layout Structure:** Hero banner at top, authentication card, then configuration content using chips and simple toggles.
- **Primary Components:** Email/password fields, login button, registration CTA, team/channel selectors, notification status rows, offline warning.
- **Interaction Notes:** Prioritizes immediate first-use clarity and fast account entry while preserving settings visibility if the user is offline.

### 2. `news_dashboard.html`
- **Primary Purpose:** Present personalized football news as the app’s central information hub.
- **Layout Structure:** Top navigation header, pill-style feed filters, vertical feed of article cards, empty-state card, and sharing-state card.
- **Primary Components:** Feed tabs, article metadata, article CTAs, personalization prompt, sharing feedback message.
- **Interaction Notes:** The feed emphasizes scanability and quick entry into stories while making personalization and sharing discoverable.

### 3. `live_match.html`
- **Primary Purpose:** Deliver real-time match awareness with clear status communication under live and degraded conditions.
- **Layout Structure:** Prominent score summary card above a chronological event timeline, accompanied by warning banners for degraded states.
- **Primary Components:** Scoreboard, live minute indicator, event list, empty state guidance, rights restriction message, retry action.
- **Interaction Notes:** The design makes score and match state the visual focus, while warnings explain delays or rights limitations without hiding context.

## UI/UX Trade-offs and Design Rationale

### Direct Access vs. Information Density
The app requirement emphasizes direct access to information. The mockups therefore use shallow layouts with important data surfaced early. The trade-off is that advanced filtering and deep metadata are intentionally minimized in the first-layer designs to avoid slowing core use cases.

### Real-Time Visibility vs. Cognitive Load
For live ticker screens, highly visible scoreboards and concise event lists help users process real-time updates quickly. The trade-off is that detailed analytics or expanded commentary are not shown in the core mobile layout.

### Personalization Simplicity vs. Configuration Power
Preference selection is represented with chips and simple toggles to reduce setup effort. The trade-off is that more granular controls, such as nested competition preferences or advanced alert rules, would require a deeper settings experience not shown here.

### Rights Compliance vs. User Convenience
The stream state explicitly withholds links when rights are invalid. This protects legal compliance but may frustrate users, so the UI includes explanatory messaging rather than silently omitting access.

### Offline Continuity vs. Freshness Accuracy
Offline-capable screens prioritize continuity by showing cached information and preserved navigation. The UI therefore surfaces banners and stale-state cues to balance usability with transparency about data freshness.

## Interaction Flow Summary
1. User launches the app and logs in or registers.
2. User configures favorite clubs, channels, and notifications.
3. User lands on personalized news and can browse broader content.
4. On match day, user opens the live ticker for real-time updates.
5. User may inspect team/player context or attempt to open a live stream link.
6. User can share content, receive notifications, and continue using cached content when offline.

## Coverage Notes
- All mockups are self-contained HTML5 artifacts.
- Each HTML file includes populated, empty/unconfigured, and error/offline/restricted states in one responsive grid as required.
- The visual states directly align to the core user stories and highlight critical edge cases from the source requirements.