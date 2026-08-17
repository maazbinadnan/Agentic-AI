# 07_ui_mockups.md

## 1. Interaction Design Overview & Screen Architecture

The LiveFootball mobile app interaction design is structured around a fast-start, authenticated, mobile-first experience that prioritises football fans’ most time-sensitive journeys: startup access, personalised news, live results, competition exploration, match detail review, rights-aware stream access, and preference management.

### Design principles
- **Fast first interaction:** the startup screen communicates readiness within the two-second target and provides visible fallback messaging if startup delays occur.
- **Personalised by default:** once authenticated, the home/dashboard prioritises favourite clubs, preferred channels, and live matches.
- **Always-usable interface:** offline, missing-data, and API-failure states preserve navigation and screen stability.
- **Rights-aware transparency:** live-stream affordances appear only when transmission rights are valid in-country.
- **Modular consistency:** news, ticker, settings, and match-detail modules share a common visual grammar to support US-013.
- **Privacy-conscious flows:** authentication and settings surfaces provide GDPR-oriented trust cues and controlled user actions.

### Screen architecture
1. **Startup & Authentication**
   - Entry point at app launch
   - Login/register gating before core content access
   - Startup readiness indicator and delayed-start exception handling
2. **Dashboard / News / Live Ticker**
   - Primary post-login landing area
   - Personalised headlines, selected team chips, preferred channel chips
   - Near real-time score cards and cached-content fallback
3. **Explore / Match Details / Settings**
   - Browsing leagues, teams, players, match-level insights
   - Rights-aware stream link presentation
   - Personalisation settings, notification toggles, and sharing affordances

The HTML mockups were designed as responsive multi-state boards, with each file containing populated, empty, and error/restricted subcases side-by-side in one responsive grid as required.

## 2. HTML Mockups to User Stories Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `login_startup.html` | US-001, US-002, US-012 | Login form, registration CTA, OAuth buttons, remember-me checkbox, startup readiness badge, delay/non-compliance messaging, GDPR privacy notice, authentication error banner |
| `dashboard_news.html` | US-003, US-004, US-010, US-011, US-013 | Personalised dashboard header, favourite team chips, preferred channel filters, live ticker cards, filtered news feed cards, cached news cards, offline banner, API failure message, stable bottom navigation |
| `explore_match_details.html` | US-005, US-006, US-007, US-008, US-009, US-013 | Competition browser, team/player stats cards, rights-aware stream CTA, rights restriction banner, favourite club settings, notification toggles, save-preferences actions, social share sheet, missing data and share-unavailable states |

## 3. Detailed UI Screen Specifications & Component Breakdowns

### 3.1 `login_startup.html`

**Purpose:**
Supports secure access at app startup while visually reinforcing the performance requirement and privacy posture.

**Included subcases:**
- **Populated / Success State:** returning user sees prefilled credentials, successful authentication banner, and startup time under threshold.
- **Empty / First-Time State:** blank login fields, account creation path, loading-shell indicators, and privacy consent messaging.
- **Error / Delayed Startup State:** login failure, startup delay warning, and limited-connectivity fallback.

**Primary components:**
- App branding and value proposition hero
- Email/password fields
- Remember-me checkbox
- Google/Apple sign-in buttons
- Authentication CTAs
- Success/error/warning banners
- Startup performance badge
- GDPR notice block

**Interaction notes:**
- Access to app modules is blocked until authentication succeeds.
- Delay state clarifies that startup breaches are operationally recorded.
- Poor connectivity does not collapse the interface; instead, the shell remains stable.

### 3.2 `dashboard_news.html`

**Purpose:**
Represents the main fan experience after login, combining personalised content discovery with live match awareness and resilient offline access.

**Included subcases:**
- **Populated State:** favourite teams and channels selected, live matches active, filtered headlines available.
- **Empty / Unconfigured State:** no favourites chosen yet, but general coverage remains accessible.
- **Offline / Error State:** cached news shown, live API unavailable messaging, graceful peak-load resilience messaging.

**Primary components:**
- Dashboard greeting and operational status pill
- Hero summary card
- Favourite team chips and sports channel chips
- Live ticker score cards with timestamps
- News feed article cards
- Share/save CTAs
- Offline notification banner
- Bottom navigation

**Interaction notes:**
- Personalisation influences content ranking and filtering but does not create a blank experience when unset.
- Live ticker cards prioritise legibility and update recency.
- Offline mode distinguishes cached content from live content to maintain user trust.
- During high demand, messaging indicates that degradation is handled gracefully instead of leaving the user uncertain.

### 3.3 `explore_match_details.html`

**Purpose:**
Supports deeper football exploration, including detailed entities, live-stream linkage, preference management, notifications, and content sharing.

**Included subcases:**
- **Populated State:** match is live, stream rights valid, detailed stats present, favourites and notifications enabled.
- **Empty / Unconfigured State:** browsing competitions before favourites are set, toggles off by default, sharing unavailable until content is selected.
- **Restricted / Error State:** stream hidden due to rights restriction, data source details unavailable, preference save failure, share mechanism unavailable.

**Primary components:**
- Competition and match context tags
- Stream CTA button with rights status
- Team/player statistic panels
- Favourite-club toggle and notification switches
- Save preferences / edit settings actions
- Share sheet tokens and share availability messaging
- Error and rights-restriction cards

**Interaction notes:**
- Stream links are conditionally displayed only when rights are valid in the user’s country and the provider broadcast is active.
- Settings failures preserve the previously saved state rather than silently discarding user trust.
- Missing entity data affects only the relevant panel, not the entire screen.

## 4. Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

### Visual hierarchy
- **Primary actions** use high-contrast gradient buttons to direct attention to key outcomes: login, save preferences, open stream, select favourites.
- **Secondary actions** remain visually subordinate with bordered dark buttons to reduce accidental taps.
- **State indicators** are colour-coded and grouped near the top of each card: green for success/availability, amber for warning/offline, red for error/restriction.
- **Dense football data** is chunked into cards, chips, and small stat panels to improve scannability on mobile screens.

### Accessibility considerations
- Text/background contrast is designed to remain high on dark surfaces.
- Form controls and buttons are large enough for touch interaction.
- Status banners use both **colour and text labels**, reducing reliance on colour alone.
- Layout remains responsive through `repeat(auto-fit, minmax(320px, 1fr))`, supporting narrow and wider mobile-preview contexts.
- Semantic HTML elements such as form fields, headings, and buttons are used consistently.
- Error messages are visible inline and close to the relevant action context.
- The mockups are compatible with future additions such as `aria-live` regions for live ticker updates and assistive notification announcements.

### UX trade-offs
- **Single-file multi-state screens** improve review efficiency for stakeholders but are not a direct one-to-one runtime navigation model.
- **Dark theme styling** supports sports-media aesthetics and perceived visual focus, but requires careful contrast validation in implementation.
- **Performance messaging** is made explicit for requirements traceability, though production UI may show such details more subtly.
- **Operational resilience messaging** is intentionally more visible in the mockups than in a final polished app to demonstrate compliance with offline and high-load requirements.

### Inferred design requirements from operational context
- Mobile-first for Android and iOS form factors
- Core content available within two seconds after startup under normal conditions
- Stable interface under limited connectivity and external API disruption
- Personalisation controls for teams, channels, and notifications
- Real-time or near-real-time match update presentation
- Compliance-aware deep linking for streams based on geography and rights
- Shareable football content through device-native mechanisms
- GDPR-conscious handling of user account and preference data

## Deliverables generated
- `html/login_startup.html`
- `html/dashboard_news.html`
- `html/explore_match_details.html`
- `07_ui_mockups.md`
