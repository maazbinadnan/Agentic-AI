# 07_ui_mockups_and_interaction_design.md

## Section 1: Interaction Design Overview & Screen Architecture

The LiveFootball app is designed as a mobile-first, cross-platform (Android/iOS) football news and live ticker application. The user interface (UI) is minimalist, dark-themed, and uses a side drawer for navigation. The design emphasizes rapid access to football content, real-time updates, and personalization, while ensuring accessibility and GDPR compliance.

**Core Screens:**
- Login/Registration
- Dashboard (Home)
- News Feed
- Live Ticker
- Leagues & Competitions
- Live Streams
- Team & Player Details
- Settings

All screens use the Inter font, a dark blue (#0F172A) background, and accent colors for clarity and accessibility. Layouts are responsive, with rounded cards, clear visual hierarchy, and error/empty states for robust UX.

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File                | Mapped User Stories                | Visualizations / Core UI Components                                                      |
|------------------------- |------------------------------------|-----------------------------------------------------------------------------------------|
| `login.html`             | US-015, US-024                     | Login form, OAuth social buttons, Remember me, Error banner, GDPR notice                |
| `dashboard.html`         | US-002, US-003, US-012, US-016     | Side drawer nav, Favorite teams filter, Live ticker widget, News feed cards             |
| `news.html`              | US-003, US-004, US-017, US-018     | News channel filter, News cards, Share button, Prompt for favorite teams                |
| `liveticker.html`        | US-005, US-010, US-011, US-019, US-020 | Team selector, Live ticker grid, Error state for live data                              |
| `leagues.html`           | US-006                             | League/competition cards, Error state for unsupported leagues                           |
| `livestreams.html`       | US-008, US-009, US-020             | Live stream links, Rights-based display, Error/rights banners                           |
| `team_player_details.html`| US-007                             | Team info, Player stats grid, Error state                                               |
| `settings.html`          | US-004, US-013, US-014, US-017, US-024 | Theme switch, News channel selection, Notification toggles, GDPR/account controls       |

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### login.html
- **Purpose:** Secure entry point for registration/login (US-015, US-024)
- **Components:**
  - Email/password fields, Remember me, OAuth (Google/Facebook), Error banner, GDPR notice
  - Responsive, accessible form fields with clear focus states

### dashboard.html
- **Purpose:** Main hub for navigation and personalized content (US-002, US-003, US-012, US-016)
- **Components:**
  - Side drawer navigation (Home, News, Live Ticker, Leagues, Streams, Settings, Logout)
  - Favorite teams filter (chips), Live ticker widget (real-time scores), News feed cards
  - Top bar for quick access to settings

### news.html
- **Purpose:** Aggregated football news, customizable by channels and favorite teams (US-003, US-004, US-017, US-018)
- **Components:**
  - News channel filter (chips/buttons), News cards (headline, summary, team tag)
  - Share button (social), Prompt banner for favorite teams if none selected

### liveticker.html
- **Purpose:** Real-time match updates for favorite teams (US-005, US-010, US-011, US-019, US-020)
- **Components:**
  - Team selector (dropdown), Live ticker grid (match, score, time)
  - Error banner for unavailable data or offline state

### leagues.html
- **Purpose:** Browse all supported leagues/competitions (US-006)
- **Components:**
  - League cards (name, country, view link), Error banner for unsupported leagues

### livestreams.html
- **Purpose:** Access live stream links when available and rights-fulfilled (US-008, US-009, US-020)
- **Components:**
  - Stream cards (match, provider, link), Rights banner (geo-block), Error banner (no streams)

### team_player_details.html
- **Purpose:** Detailed team and player info on demand (US-007)
- **Components:**
  - Team info (logo, stadium, manager), Player stats grid (goals, assists, matches, cards)
  - Error banner for unavailable info

### settings.html
- **Purpose:** Personalization, theme, notifications, account controls (US-004, US-013, US-014, US-017, US-024)
- **Components:**
  - Theme switch (dark/light), News channel selection, Notification toggles, GDPR/account actions

## Section 4: Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

- **Visual Hierarchy:**
  - Large, bold headings (Inter font, 2rem/1.5rem)
  - Accent colors for CTAs and highlights (light blue, green)
  - Spacious card layouts, clear separation of sections
- **Accessibility:**
  - Sufficient color contrast (dark backgrounds, light text)
  - Large touch targets, focus indicators, ARIA roles (where applicable)
  - Error/empty states for all data-driven modules
  - All forms and controls are keyboard accessible
- **UX Trade-offs:**
  - Side drawer navigation prioritizes content space over persistent nav, ideal for mobile
  - Minimalist design reduces cognitive load but may require onboarding for first-time users
  - Real-time data modules (live ticker, streams) show clear error/offline states to manage user expectations
  - GDPR and privacy controls are surfaced in login and settings for transparency

---

**End of Report**
