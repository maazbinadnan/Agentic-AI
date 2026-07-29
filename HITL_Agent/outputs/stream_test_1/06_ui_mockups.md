# 06_ui_mockups.md

## Section 1: Interaction Design Overview & Screen Architecture

The LiveFootball mobile app is designed to provide football fans with a fast, intuitive, and comprehensive platform for following football news, live results, team/player details, and live streams. The UI architecture is modular, with each core workflow mapped to a dedicated, responsive screen. Navigation is consistent and bottom-oriented for mobile ergonomics. Error and offline states are explicitly visualized to support edge cases and accessibility.

**Screen Architecture:**
- **Splash/Loading Screen:** Fast startup, loading indicator, error state for slow loads.
- **Login/Registration:** Email/password, OAuth, GDPR notice, error handling.
- **Dashboard:** News feed, favorite team filter, live ticker widget, share buttons, offline banner.
- **Live Ticker:** Real-time match updates, error/offline banners, match list.
- **Details:** Team/player info, stats grid, recent matches, error state.
- **Live Stream:** Stream link (rights-checked), info/error banners.
- **Settings:** Favorite teams/channels, notification toggle, offline mode, GDPR actions, error/info banners.

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File         | Mapped User Stories                | Visualizations / Core UI Components                                                                 |
|------------------|------------------------------------|-----------------------------------------------------------------------------------------------------|
| `splash.html`    | US-001, US-014                     | Loading spinner, app logo, error banner for slow/performance issues                                 |
| `login.html`     | US-011, US-017                     | Login/registration form, OAuth buttons, GDPR notice, error banner                                   |
| `dashboard.html` | US-002, US-003, US-008, US-012, US-013 | News feed cards, favorite teams filter, live ticker widget, share button, offline banner, navigation |
| `liveticker.html`| US-004, US-006, US-013, US-014      | Live match list, real-time updates, offline/cached banner, error banner, navigation                 |
| `details.html`   | US-007, US-008                      | Team/player stats grid, recent matches, error banner, navigation                                    |
| `livestream.html`| US-005                              | Live stream link button, info/error banners, rights compliance message, navigation                  |
| `settings.html`  | US-003, US-009, US-010, US-017      | Favorite teams/channels selection, notification toggle, offline mode, GDPR actions, error/info banners, navigation |

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### Splash/Loading Screen (`splash.html`)
- **Purpose:** Fast app startup, communicates loading state, handles slow/performance issues.
- **Components:**
  - App logo
  - Spinner/loading indicator
  - Loading message
  - Error banner (for slow load or high-traffic events)
- **Edge Cases:** Shows error if load >2s or >100,000 users (US-001, US-014)

### Login/Registration (`login.html`)
- **Purpose:** Secure, simple authentication and onboarding.
- **Components:**
  - Email/password fields
  - OAuth (Google, Facebook) buttons
  - Remember me checkbox
  - Register/Forgot password links
  - GDPR/Privacy policy notice
  - Error banner for invalid login/registration (US-011, US-017)

### Dashboard (`dashboard.html`)
- **Purpose:** Central hub for news, live ticker, and navigation.
- **Components:**
  - Top navigation bar (brand, settings, notifications)
  - Favorite teams filter dropdown
  - Live ticker widget (quick match update)
  - News feed cards (with share button)
  - Offline/cached info banner
  - Bottom navigation bar (Home, Live Ticker, Teams, Settings)
- **Edge Cases:** No news available, offline state (US-002, US-013)

### Live Ticker (`liveticker.html`)
- **Purpose:** Real-time match updates, robust to network issues.
- **Components:**
  - Live match list with scores and time
  - Offline/cached results banner
  - Error banner for server issues
  - Bottom navigation bar
- **Edge Cases:** Server unavailable, limited/no connectivity (US-004, US-006, US-013)

### Details (`details.html`)
- **Purpose:** Team/player deep dive.
- **Components:**
  - Team/player name, logo, league
  - Stats grid (wins, draws, losses, goals)
  - Recent matches list
  - Error banner for missing data
  - Bottom navigation bar
- **Edge Cases:** No info available (US-007)

### Live Stream (`livestream.html`)
- **Purpose:** Access to live streams, rights-aware.
- **Components:**
  - Stream info banner (rights fulfilled)
  - Error banner (rights restricted)
  - Stream link button (e.g., DAZN)
  - Rights compliance message
  - Bottom navigation bar
- **Edge Cases:** Rights not fulfilled (US-005)

### Settings (`settings.html`)
- **Purpose:** Personalization, notifications, GDPR, offline mode.
- **Components:**
  - Favorite teams/channels multi-select
  - Notification and offline mode toggles
  - Custom interface URL input
  - GDPR data deletion button
  - Error/info banners
  - Bottom navigation bar
- **Edge Cases:** Invalid config, GDPR request (US-009, US-017)

## Section 4: Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

- **Visual Hierarchy:**
  - Primary actions (login, share, watch stream) use high-contrast buttons.
  - Navigation is persistent and bottom-aligned for thumb reachability.
  - Error/info banners are prominent and color-coded (red for errors, yellow for offline, blue for info).
- **Accessibility:**
  - All screens use semantic HTML5 and ARIA roles where appropriate.
  - Color contrast meets WCAG 2.1 AA standards.
  - All interactive elements are keyboard/touch accessible.
  - Forms use proper labels and error feedback.
  - Responsive layouts adapt to mobile and tablet breakpoints.
- **UX Trade-offs:**
  - Minimalist, card-based design for speed and clarity.
  - Offline and error states are always visible to prevent user confusion.
  - Social sharing and GDPR actions are surfaced but not intrusive.
  - Some advanced personalization (custom interface URL) is optional to avoid overwhelming new users.

---

**End of UI Mockups & Interaction Design Report**
