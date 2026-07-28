# 06. UI Mockups & Interaction Design Report

## Section 1: Interaction Design Overview & Screen Architecture

The LiveFootball mobile app is designed to provide football fans with a fast, seamless, and highly personalized experience. The UI architecture is modular, with each screen supporting a core user journey mapped directly to user stories and acceptance criteria. The design emphasizes:
- **Speed:** Splash/loading screen ensures readiness within two seconds (US-001).
- **Personalization:** Users can select favorite teams/channels and receive tailored news and notifications (US-003, US-010).
- **Comprehensive Coverage:** News, live ticker, leagues, and detailed team/player info are easily accessible (US-002, US-004, US-005, US-006).
- **Reliability:** Offline and error states are handled gracefully (US-012, US-013).
- **Privacy:** GDPR compliance and user data controls are integrated (US-017).

**Screen Architecture:**
- Splash/Loading
- Login/Registration
- Home/Dashboard
- Live Ticker/Results
- Leagues/Competitions
- Team/Player Details
- Personalization/Settings
- News Article/Share Modal
- Error/Offline/High Load
- GDPR/Privacy Modal

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File         | Mapped User Stories                | Visualizations / Core UI Components                                      |
|-------------------|-----------------------------------|--------------------------------------------------------------------------|
| `splash.html`     | US-001, US-013                    | Animated logo, loading indicator, high load/error message                |
| `login.html`      | US-014, US-017                    | Login/registration form, OAuth, GDPR consent, error banner               |
| `dashboard.html`  | US-002, US-003, US-009, US-010, US-012 | News feed, favorite teams filter, nav bar, notification icon, offline banner |
| `live_ticker.html`| US-004, US-008                    | Live match list, real-time updates, error/cached data banner             |
| `leagues.html`    | US-005                            | Leagues/competitions list, search/filter, error message                  |
| `details.html`    | US-006, US-007                    | Team/player profile, stats, live stream link, share button, error state  |
| `settings.html`   | US-003, US-010, US-017            | Favorite teams/channels selection, notification toggle, GDPR/data deletion|
| `article.html`    | US-011                            | News article view, social share modal, error banner                      |
| `error.html`      | US-001, US-012, US-013            | Full-screen error/offline/high load messages                             |
| `gdpr.html`       | US-017                            | GDPR info, consent, data deletion request                                |

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### Splash/Loading (`splash.html`)
- Animated football logo and app name
- Spinner/progress indicator
- Error message for slow load or high traffic
- Responsive, centered layout

### Login/Registration (`login.html`)
- Email/password fields, "Remember me" checkbox
- OAuth login (Google, Facebook)
- GDPR consent text and privacy policy link
- Error banner for failed login
- Register and password reset links

### Home/Dashboard (`dashboard.html`)
- Top navigation bar with quick links to modules and notifications
- Favorite teams filter dropdown
- News feed cards with images, titles, summaries, and share buttons
- Offline/cached data banner
- Responsive grid for news

### Live Ticker/Results (`live_ticker.html`)
- Header with real-time update label
- List of live and finished matches with scores and event updates
- Error/cached data banner for network issues

### Leagues/Competitions (`leagues.html`)
- Search bar for filtering leagues/competitions
- Grid/list of league cards with icons and country labels
- Error banner for data unavailability

### Team/Player Details (`details.html`)
- Team/player profile header with logo and league
- Stats grid (wins, draws, losses, points)
- Live stream link button (conditional)
- Share button
- Player list with roles
- Error banner for unavailable info

### Personalization/Settings (`settings.html`)
- Multi-select for favorite teams and channels
- Notification toggle switch
- GDPR/data deletion controls and info

### News Article/Share Modal (`article.html`)
- Article title, author, date, image, and content
- Share to social button
- Error banner for sharing failures

### Error/Offline/High Load (`error.html`)
- Prominent error icon and message
- Retry button
- Used for offline, high load, or technical issues

### GDPR/Privacy Modal (`gdpr.html`)
- GDPR compliance info
- Data deletion and export request form
- Confirmation message

## Section 4: Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

- **Visual Hierarchy:**
  - Primary actions (login, share, watch live) use bold colors and large buttons.
  - Navigation and filters are placed at the top for quick access.
  - Error and offline states use high-contrast banners or overlays.
- **Accessibility:**
  - All interactive elements have sufficient color contrast and large touch targets.
  - Forms use proper labels and ARIA roles where needed.
  - Images have alt text; icons are accompanied by text or tooltips.
  - Responsive layouts ensure usability on all device sizes.
- **UX Trade-offs:**
  - Used Bootstrap for rapid, consistent, and accessible UI scaffolding.
  - Some demo data and static images are used for mockup clarity.
  - Error and offline states are visually prominent to reduce user confusion.
  - GDPR and privacy controls are always accessible from settings and login.

---

**End of UI Mockups & Interaction Design Report**
