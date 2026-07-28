# 7. UI Mockups & Interaction Design Report

## HTML Mockup-to-User Story Mapping Table

| HTML File           | Mapped User Stories         | Visualizations / Core UI Components                  |
|---------------------|----------------------------|-----------------------------------------------------|
| `login.html`        | US-008                     | Login form, OAuth buttons, Remember me checkbox      |
| `dashboard.html`    | US-001, US-002, US-003, US-004, US-005, US-009 | Live ticker, news feed, stream links, team selector, notification bar, navigation menu |
| `team_details.html` | US-006                     | Team info, player list, league details               |
| `settings.html`     | US-004, US-005             | Favorite teams/channels selection, notification toggles, save button |
| `news_details.html` | US-007                     | News article, share button                          |

## Screen Layout Specifications

- **login.html:** Centered login form with email/username, password, remember me, OAuth buttons, and registration link. Responsive for mobile.
- **dashboard.html:** Header, navigation bar, notification bar, live ticker section, news feed, live stream links. Modular layout for easy navigation.
- **team_details.html:** Team logo, basic info, player list. Clean, readable layout for quick access to details.
- **settings.html:** Multi-select for favorite teams/channels, notification toggles, save button. Simple, accessible layout.
- **news_details.html:** News headline, meta info, content, share button. Focused, distraction-free reading experience.

## UI/UX Trade-offs

- **Performance vs. Richness:** Minimalist design for fast load times (<2s), prioritizing essential content and interactions.
- **Modularity:** UI components are modular for extensibility and consistent experience across screens.
- **Accessibility:** High-contrast, readable fonts, clear labels, and large touch targets. Accessibility features (screen reader, ARIA roles) recommended for production.
- **Offline Mode:** Notification bar and cached data display for offline scenarios.
- **Social Sharing:** Dedicated share button in news details for easy access.
- **Personalization:** Settings screen allows granular control over favorites and notifications.

## Interaction Design Notes

- Navigation is persistent and intuitive, allowing users to switch between modules easily.
- Real-time updates are visually indicated in the live ticker and notification bar.
- Error and offline states are handled gracefully with user feedback.
- Registration/login is streamlined with OAuth options for quick access.
- All screens are responsive and optimized for mobile devices.
