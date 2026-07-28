# UI Mockups & Interaction Design Report

---

## Section 1: Interaction Design Overview & System Screen Architecture

### Main Application Screens

1. **Login & Registration Screen** (`login.html`)
2. **Onboarding / Personalization Screen** (`onboarding.html`)
3. **Main Dashboard (Home)** (`dashboard.html`)
4. **Live Ticker (Live Scores)** (`live_ticker.html`)
5. **Team & Player Details** (`team_player_details.html`)
6. **News & Reports** (`news.html`)
7. **News/Match Report Details & Sharing** (`news_details.html`)
8. **Notification Preferences** (`notifications.html`)
9. **Settings & Account Management** (`settings.html`)
10. **Support & Feedback** (`feedback.html`)
11. **GDPR Consent & Privacy Policy** (`gdpr_consent.html`)

---

## Section 2: HTML Mockups to User Stories Mapping Table

| HTML File                | Mapped User Stories         | Visualizations / Components                                      |
|--------------------------|----------------------------|------------------------------------------------------------------|
| `login.html`             | US-001, US-002, US-015     | Login/registration form, error messages, GDPR consent, forgot password |
| `onboarding.html`        | US-003                     | Team/league selection, progress bar, save preferences button     |
| `dashboard.html`         | US-011, US-012, US-013     | Navigation bar, metrics cards, quick links, offline indicator    |
| `live_ticker.html`       | US-006, US-008, US-013     | Live scores, match events, favorite teams highlight, live stream link, offline banner |
| `team_player_details.html`| US-007, US-013            | Team/player stats, bio, recent matches, offline data             |
| `news.html`              | US-009, US-013             | News cards, filter by favorites, offline banner                  |
| `news_details.html`      | US-010, US-009, US-013     | Article content, share button, social media options, offline banner |
| `notifications.html`     | US-004, US-005             | Notification toggles, event type selectors, save button          |
| `settings.html`          | US-003, US-004, US-015     | Preferences, account management, data export/delete, privacy policy |
| `feedback.html`          | US-016                     | Feedback form, issue reporting, confirmation message             |
| `gdpr_consent.html`      | US-015                     | Consent checkbox, privacy policy link, continue button           |

---

## Section 3: Detailed UI Screen Specifications & Component Breakdowns

### 1. Login & Registration (`login.html`)
- **Components:** Email/password fields, login/register toggle, "Forgot Password" link, error message area, GDPR consent checkbox, continue button.
- **States:** Normal, error (invalid credentials), loading, password reset sent.
- **Accessibility:** Labels for all fields, large touch targets, ARIA roles for error messages.

### 2. Onboarding / Personalization (`onboarding.html`)
- **Components:** Multi-select for teams/leagues (badges or checkboxes), progress indicator, save/continue button.
- **States:** Selection, saving, error (if none selected).
- **Accessibility:** High-contrast, keyboard navigation, screen reader hints.

### 3. Main Dashboard (`dashboard.html`)
- **Components:** Persistent navigation bar (Home, Live, News, Teams, Settings), cards for quick stats (next match, favorite team), offline indicator.
- **States:** Online, offline (cached data), loading.
- **Accessibility:** Tab order, color contrast, focus indicators.

### 4. Live Ticker (`live_ticker.html`)
- **Components:** List of live matches, event timeline, favorite team highlight, live stream link (conditional), offline banner.
- **States:** Live updating, offline (cached), rights-restricted (stream link hidden).
- **Accessibility:** Live region for updates, clear event icons.

### 5. Team & Player Details (`team_player_details.html`)
- **Components:** Team/player photo, stats table, bio, recent matches, favorite toggle.
- **States:** Online, offline (cached), loading.
- **Accessibility:** Table summaries, alt text for images.

### 6. News & Reports (`news.html`)
- **Components:** News cards, filter by favorites, timestamps, offline banner.
- **States:** Online, offline (cached), loading.
- **Accessibility:** Headings, readable font size.

### 7. News/Match Report Details & Sharing (`news_details.html`)
- **Components:** Article content, share button (opens share sheet), social media icons.
- **States:** Online, offline (cached), sharing in progress.
- **Accessibility:** Share button labeled, content readable.

### 8. Notification Preferences (`notifications.html`)
- **Components:** Toggles for event types (goals, news, match start), save button.
- **States:** Saved, unsaved changes, error.
- **Accessibility:** Toggle labels, focusable controls.

### 9. Settings & Account Management (`settings.html`)
- **Components:** Edit preferences, export/delete data, privacy policy link, logout.
- **States:** Confirmation dialogs, error messages.
- **Accessibility:** Button labels, confirmation prompts.

### 10. Support & Feedback (`feedback.html`)
- **Components:** Text area for feedback, category selector, submit button, confirmation message.
- **States:** Submitted, error.
- **Accessibility:** Form labels, confirmation ARIA live region.

### 11. GDPR Consent & Privacy Policy (`gdpr_consent.html`)
- **Components:** Consent checkbox, privacy policy link, continue button.
- **States:** Consent required, error if not checked.
- **Accessibility:** Checkbox label, link focusable.

---

## Section 4: UI/UX Design Decisions & Trade-offs

- **Visual Hierarchy:** Key actions (e.g., live scores, favorite teams) are prioritized at the top of screens. Cards and lists use clear headings and icons.
- **Accessibility:** All screens use high-contrast colors, large touch targets, ARIA roles for dynamic content, and readable fonts. Error states are announced and visually distinct.
- **Responsiveness:** Layouts use flexible grids and media queries for mobile and tablet. Navigation is always accessible at the bottom.
- **Offline Mode:** Offline banners and restricted features are clearly indicated. Cached data is shown with a timestamp.
- **Performance:** Minimal animations, lazy loading for images, and skeleton loaders for data. Main dashboard and live ticker are optimized for <2s load.
- **Error Handling:** All forms and data fetches have clear error messages and retry options.
- **Privacy & GDPR:** Consent is required at registration. Data export/delete is accessible in settings. Privacy policy is always linked.
- **Sharing:** Share sheets use native OS dialogs for accessibility and familiarity.

---

**All HTML mockups are available in the `html/` subfolder.**

---
