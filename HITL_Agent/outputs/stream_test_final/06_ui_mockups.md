# LiveFootball App – UI Mockups & Interaction Design Report

## Section 1: Interaction Design Overview & Screen Architecture

The LiveFootball app is designed as a fast, mobile-first platform for football fans to access live scores, news, team/player details, and live streams. The interface is optimized for rapid loading, accessibility, and seamless navigation, even under limited network conditions. The following core screens and flows are implemented:

- **Login:** Secure authentication with email/password and OAuth, including error handling.
- **Onboarding:** Guided selection of favorite teams and notification preferences for personalized content.
- **Dashboard:** Central hub for live ticker, news, and quick access to favorite teams.
- **Details:** Deep dive into team/player stats, fixtures, and live stream access.
- **Settings:** User preferences for notifications, favorites, channels, privacy, and logout.
- **Offline:** Informative fallback for network loss, maintaining partial usability.

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File         | Mapped User Stories                | Visualizations / Core UI Components                                                                 |
|------------------|------------------------------------|-----------------------------------------------------------------------------------------------------|
| `login.html`     | US-001, US-002                     | Login form, OAuth social buttons, Remember me checkbox, Error banner                                |
| `onboarding.html`| US-003, US-004, US-005              | Team selection cards, Progress bar, Notification opt-in switch, Guided onboarding flow              |
| `dashboard.html` | US-006, US-007, US-008, US-009      | Navigation bar, Favorite teams filter, Live ticker widget, News feed cards, Share buttons           |
| `details.html`   | US-010, US-011, US-012, US-013      | Team/player statistics grid, Fixtures tab, Players list, Live stream link button, Social share      |
| `settings.html`  | US-014, US-015, US-016, US-017      | Notification toggle, Edit favorites, Channel selector, GDPR/privacy link, Logout                   |
| `offline.html`   | US-018                              | Offline state banner, Retry button, Offline info                                                    |

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### 1. Login (`login.html`)
- **Components:**
  - Email/password fields (with validation)
  - OAuth buttons (Google, Facebook)
  - Remember me checkbox
  - Error banner for failed login
  - Register link
- **Accessibility:**
  - Proper label associations, keyboard navigation, ARIA roles for error

### 2. Onboarding (`onboarding.html`)
- **Components:**
  - Team selection cards (visual, selectable, keyboard accessible)
  - Progress bar for onboarding steps
  - Notification opt-in switch
  - Next/Finish buttons
- **Accessibility:**
  - Focusable cards, clear instructions, color contrast

### 3. Dashboard (`dashboard.html`)
- **Components:**
  - Navigation bar (brand, notifications, settings)
  - Favorite teams quick filter (badges, edit)
  - Live ticker (real-time updates, ARIA live region)
  - News feed cards (title, summary, read/share buttons)
- **Accessibility:**
  - ARIA live for ticker, alt text for images, keyboard navigation

### 4. Details (`details.html`)
- **Components:**
  - Team/player header (badge, name, league)
  - Tabbed interface (Stats, Fixtures, Players)
  - Stats table, fixtures list, player roster
  - Live stream button (contextual)
  - Social share button
- **Accessibility:**
  - Tab roles, table semantics, alt text, ARIA labels

### 5. Settings (`settings.html`)
- **Components:**
  - Notification toggle (switch)
  - Edit favorites button
  - Channel selector (dropdown)
  - GDPR/privacy link
  - Logout button
- **Accessibility:**
  - Labeled controls, focus order, link semantics

### 6. Offline (`offline.html`)
- **Components:**
  - Offline icon/banner
  - Retry button
  - Info link
- **Accessibility:**
  - Clear messaging, button focus, alt text

## Section 4: Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

- **Visual Hierarchy:**
  - Primary actions (login, next, finish, share) are visually prominent.
  - Key information (live scores, news) is prioritized at the top of screens.
  - Consistent use of color and iconography for quick recognition.

- **Accessibility (WCAG 2.1):**
  - Sufficient color contrast for text and controls.
  - All interactive elements are keyboard accessible.
  - ARIA roles and labels for dynamic/live regions and error states.
  - Alt text for all icons and images.
  - Responsive layouts for mobile and tablet.

- **UX Trade-offs:**
  - Minimalist onboarding to reduce friction, but allows later customization in settings.
  - Live ticker and news are prioritized for immediacy, with deeper info a tap away.
  - Offline mode provides clear feedback but limits interactivity to maintain clarity.

---

**End of Report**
