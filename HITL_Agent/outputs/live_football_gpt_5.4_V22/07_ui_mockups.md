# 07 UI Mockups & Interaction Design

## 1. Interaction Design Overview & Screen Architecture

The LiveFootball interaction design is structured as a mobile-first application optimized for Android and iOS usage with fast scanning, large touch targets, and consistent module access through bottom-tab navigation. The visual direction follows the approved energetic sports-focused light theme, using `#042D13` as the brand anchor, Inter as the primary typeface, and rounded cards for quick comprehension during live match usage.

### Core interaction principles
- **Fast perceived startup:** authentication screens use lightweight structure and optional skeleton loaders to support the requirement that the app be ready within two seconds.
- **Consistent mobile shell:** all primary modules remain accessible through a stable navigation framework even if external data refresh fails.
- **Personalization-first content hierarchy:** followed clubs, preferred channels, and notification preferences shape the home/news and live experiences.
- **Clear state communication:** every mockup includes populated, empty, and error/restricted/offline states to demonstrate how the UI avoids misleading users.
- **Rights-aware and network-aware behavior:** live streams only appear when broadcasts have started and regional rights permit access; online-only actions are visually restricted offline.
- **Consistent viewport treatment:** all HTML mockups now use a unified phone frame height and internal screen scrolling so longer states do not change device size across screens.

### Proposed screen architecture
1. **Startup / Authentication**
   - Login
   - Registration
   - Validation / unsupported platform handling
2. **Home / News**
   - Personalized home summary
   - Favorite-team and preferred-channel news feed
   - Offline cached content fallback
3. **Live Ticker**
   - Real-time match detail with event timeline
   - No live matches state
   - API/network interruption state preserving last known data
4. **Discover / Details / Streams**
   - League and competition coverage browsing
   - Read-only team detail and player detail cards
   - Stream-link visibility based on broadcast start and rights eligibility
5. **Following / Profile / Settings**
   - Favorite clubs management
   - Preferred channels
   - Notification settings
   - Share actions and privacy messaging

### Navigation model
- **Primary navigation:** Home, Live, News, Following, Profile
- **Secondary access pattern:** in-screen cards and CTA buttons for team details, player details, fixtures, and provider redirects
- **Persistent interaction shell:** bottom tab bar stays visually consistent across all modules to satisfy the requirement for stable interface structure even when data changes externally

---

## 2. HTML Mockups to User Stories Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `auth_startup.html` | US-001, US-002, US-003, US-004 | Login form, registration form, remember me checkbox, OAuth buttons, startup readiness banner, skeleton loader, validation error state, unsupported platform banner |
| `home_news.html` | US-005, US-006, US-016, US-017, US-022, US-023, US-024, US-027 | Personalized home hero, favorite-team chips, preferred-channel chips, live score card, news cards, empty personalization prompts, offline cached content view, bottom-tab navigation |
| `live_ticker.html` | US-007, US-008, US-015, US-016, US-017, US-022, US-023, US-024, US-028 | Live match score header, real-time event timeline, auto-refresh indicator, followed match summaries, no-live-data placeholder, API/network unavailable banner, preserved last-known data state |
| `discover_details_streams.html` | US-009, US-010, US-011, US-012, US-013, US-014, US-016 | Competition chips, team details card, player spotlight card, stream CTA button, pre-broadcast hidden-link state, geo-restriction message, unavailable data handling |
| `following_profile_settings.html` | US-016, US-018, US-019, US-020, US-021, US-026, US-027 | Favorite clubs list, follow/unfollow controls, preferred channels summary, notification toggles, share sheet options, inactive notification state, GDPR privacy messaging |

---

## 3. Detailed UI Screen Specifications & Component Breakdowns

### 3.1 `auth_startup.html`
**Purpose:** supports first-run access and startup compliance.

**Included states**
- **Populated state:** returning user login with prefilled fields and successful shell readiness banner.
- **Empty state:** new registration flow with blank fields and skeleton loading block.
- **Error/restricted state:** invalid credentials and unsupported environment messaging.

**Key components**
- Branded hero panel with performance positioning
- Large input fields designed for touch entry
- Primary CTA for login / account creation
- Secondary OAuth options
- Validation messaging under individual fields
- Compliance hint for GDPR-aware processing and terms

**Interaction notes**
- Content behind authentication remains inaccessible until login/registration completion.
- Performance perception is reinforced with visible shell and loaders rather than a blank startup screen.
- Fixed-height phone frame with internal vertical scrolling preserves consistent sizing across all states.

### 3.2 `home_news.html`
**Purpose:** provides the personalized landing experience and content feed.

**Included states**
- **Populated state:** followed clubs and preferred channels actively shape content.
- **Empty state:** no preferences saved yet, with setup prompts.
- **Offline state:** cached articles and score snapshots remain usable while online-only features are restricted.

**Key components**
- Personalized hero module
- Team and channel filter chips
- Pinned live ticker card near top of screen
- Editorial news cards with source and recency metadata
- Offline messaging explaining limits of live refresh and stream access

**Interaction notes**
- The screen prioritizes personalized and live-relevant content before general news.
- Empty-state CTAs guide the user toward following clubs and selecting channels.
- Longer content lists remain scrollable inside the standardized device viewport.

### 3.3 `live_ticker.html`
**Purpose:** central real-time match tracking experience.

**Included states**
- **Populated state:** active match with scoreline, minute, and live event updates.
- **Empty state:** no current favorite-team matches live.
- **Error/offline state:** refresh paused, last confirmed data preserved.

**Key components**
- Large score header using strong typography for scanability
- Live badge and competition label
- Chronological event timeline
- Secondary list of other followed matches
- Warning card for unavailable live data

**Interaction notes**
- The interface explicitly avoids showing unverified or fabricated match data.
- When connectivity fails, the screen stays structurally stable and preserves the last known state.
- Additional events can extend vertically without stretching the overall device frame.

### 3.4 `discover_details_streams.html`
**Purpose:** combines browse/discovery and detail-level football information with licensed stream access.

**Included states**
- **Populated state:** coverage browsing, team/player details, and valid stream link.
- **Empty/pre-broadcast state:** stream hidden until the provider broadcast starts.
- **Restricted state:** geo-rights restriction and missing-data handling.

**Key components**
- Competition coverage chips for national/international tournaments
- Read-only team details summary
- Player profile card
- Primary external provider CTA
- Geo-restriction alert block
- Unavailable player/data placeholder

**Interaction notes**
- The stream action is intentionally framed as an external redirect, not in-app playback.
- Rights messaging is clear and compliance-oriented to manage user expectations.
- Scrollable content allows more competition/detail data while maintaining a consistent viewport size.

### 3.5 `following_profile_settings.html`
**Purpose:** houses user-controlled personalization, alerts, sharing, and privacy transparency.

**Included states**
- **Populated state:** clubs, channels, and notifications already configured.
- **Empty state:** nothing followed yet and notifications inactive.
- **Restricted/fallback state:** unavailable third-party share target with system share fallback.

**Key components**
- Follow/unfollow controls
- Preferred channel summaries
- Large notification toggles
- Share action panel using supported device patterns
- GDPR privacy summary
- Confirmation messaging after preference changes

**Interaction notes**
- Notification UI reinforces that alerts are opt-in only.
- Sharing behavior does not depend on the presence of a specific third-party app.
- Preference-heavy views use internal scrolling instead of variable device heights.

---

## 4. Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

### Visual hierarchy
- **Primary green (`#042D13`)** is used for major CTAs, active tabs, and branded headers to create a strong sports identity.
- **Live and urgent states** use green/red badges sparingly to avoid alert fatigue while preserving match-day urgency.
- **Large score typography and clear card segmentation** help users scan headlines, fixtures, and timelines quickly.
- **Hero modules** establish context at the top of each screen before more detailed cards are shown.

### Accessibility considerations
- **Contrast:** dark text on white/light surfaces and white text on dark-green headers aim to support WCAG contrast expectations.
- **Touch targets:** buttons, chips, and toggles are sized to align with the stated 44x44px minimum guidance.
- **Plain-language system states:** offline, unavailable, invalid, and restricted conditions are explicitly described to reduce ambiguity.
- **Structural consistency:** repeated card layouts and stable navigation improve learnability and benefit users with cognitive load sensitivity.
- **Typography:** Inter and spacious line spacing support readability on mobile screens, especially for scores and timeline events.

### UX trade-offs and rationale
- **Grouped multi-state mockups in single files:** chosen to satisfy review efficiency and make acceptance-criteria coverage visible side by side.
- **Bottom-tab navigation over hamburger navigation:** better for high-frequency module switching in sports apps.
- **No embedded live video UI:** aligns with the requirement to deep-link to licensed providers instead of hosting playback in-app.
- **Light mode only at this stage:** prioritized due to stated stakeholder preference and to keep the visual system focused during initial delivery.
- **Minimal motion and lightweight visuals:** supports the non-functional goal of fast startup and responsiveness on a wide range of mobile devices.

### Responsiveness and implementation notes
- All mockups were produced as **self-contained responsive HTML files**.
- Each file uses the required **`wrap` → `grid` → `phone` → `screen`** structure for side-by-side state presentation.
- All screens now use a **standardized phone viewport height** with **internal scrolling** for longer content, ensuring visual consistency across states.
- Designs are suitable for conversion into production mobile components in Flutter, React Native, SwiftUI, or native Android/iOS implementations.

---

## Deliverables Generated
- `html/auth_startup.html`
- `html/home_news.html`
- `html/live_ticker.html`
- `html/discover_details_streams.html`
- `html/following_profile_settings.html`

These mockups collectively cover the primary LiveFootball user flows, major acceptance criteria, and critical edge cases for authentication, personalization, live data, offline behavior, stream compliance, sharing, and notifications.