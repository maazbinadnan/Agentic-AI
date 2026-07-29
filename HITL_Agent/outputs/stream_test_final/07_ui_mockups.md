# 07_ui_mockups_and_interaction_design.md

## Section 1: Interaction Design Overview & Screen Architecture

The LiveFootball mobile app is designed for rapid, intuitive access to real-time football news, live results, and personalized content. The interface is mobile-first, clean, and minimal, inspired by Bento UI, and supports both light and dark modes. The primary navigation is via a side drawer, ensuring easy access to all modules. The app’s visual hierarchy, color palette, and typography (Roboto) are optimized for clarity, accessibility, and brand consistency.

**Core Screens:**
- Login/Registration (with consent modal)
- Onboarding (favorite teams, channels, notifications)
- Home (news feed, live ticker, favorite teams filter)
- Details (team/player info, stats, live stream, share modal)
- Settings (personalization, privacy, app preferences)

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File         | Mapped User Stories                | Visualizations / Core UI Components                                                                                 |
|------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `login.html`     | US-007, US-014                     | Login form, OAuth social buttons, Remember me, Error banner, GDPR consent modal                                    |
| `onboarding.html`| US-003, US-008, US-010             | Favorite teams/channels selection, Push notification opt-in, Offline/sync banner                                   |
| `home.html`      | US-001, US-002, US-004, US-010, US-011 | Side drawer nav, Favorite teams filter, Live ticker widget, News feed cards, Offline/error banners                  |
| `details.html`   | US-005, US-006, US-009             | Team/player statistics grid, Key players, Live stream link/button, Rights restriction banner, Social share modal   |
| `settings.html`  | US-003, US-008, US-014, US-010     | Personalization forms, Notification toggle, Dark mode switch, Privacy/GDPR banners, Offline/sync banner           |

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### login.html
- **Purpose:** Secure authentication and GDPR consent at app startup.
- **Components:**
  - Email/password fields, OAuth (Google/Apple) buttons
  - Remember me checkbox, error banner for failed login
  - Privacy consent modal (GDPR compliance)
  - Links to privacy policy and registration
- **Accessibility:**
  - All fields labeled, high-contrast, keyboard/tab navigation, ARIA roles for modals

### onboarding.html
- **Purpose:** Personalize user experience on first use or via settings.
- **Components:**
  - Multi-select for favorite teams and sports channels
  - Push notification opt-in
  - Offline/sync banner for network issues
- **Accessibility:**
  - Large touch targets, clear instructions, focus states

### home.html
- **Purpose:** Central dashboard for news, live results, and navigation.
- **Components:**
  - Side drawer navigation (mobile)
  - Favorite teams filter (pills)
  - Live ticker widget (real-time match updates)
  - News feed cards with share buttons
  - Offline and error banners
- **Accessibility:**
  - Semantic headings, ARIA for navigation, color contrast, responsive layout

### details.html
- **Purpose:** Deep dive into team/player info, stats, and live streams.
- **Components:**
  - Team/player header, statistics grid, key players list
  - Live stream link/button (with rights restriction banner)
  - Social share modal for news/game reports
  - Error/unavailable info banner
- **Accessibility:**
  - Alt text for images, clear section headings, modal focus management

### settings.html
- **Purpose:** Manage personalization, notifications, privacy, and app preferences.
- **Components:**
  - Favorite teams/channels selection, notification toggle
  - Dark mode switch, privacy policy links, GDPR consent banner
  - Offline/sync banner
- **Accessibility:**
  - Form labels, toggle switches with ARIA, clear feedback

## Section 4: Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

- **Visual Hierarchy:**
  - Brand green (#0E2804) and blue/orange accents for primary actions and highlights
  - Spacious card layouts, clear separation between modules, rounded corners, subtle shadows
  - Roboto font for modern, readable text; bold headings for key sections
- **Accessibility:**
  - All screens use high-contrast color schemes for both light and dark modes
  - Sufficient touch target sizes, keyboard navigation, ARIA roles for modals and navigation
  - Error and status banners use color and iconography, but also clear text for screen readers
  - Alt text for all images and icons
- **UX Trade-offs:**
  - Minimalist design prioritizes speed and clarity, but advanced users may desire more dense data views (future enhancement)
  - Side drawer navigation is optimal for mobile, but may require adaptation for tablet/desktop
  - Offline/limited network states are surfaced with clear banners, but some features are disabled to ensure reliability

---

**End of Report**
