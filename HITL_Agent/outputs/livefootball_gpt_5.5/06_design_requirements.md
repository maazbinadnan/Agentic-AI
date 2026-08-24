# Visual & UI Design Requirements Specification

## 1. Executive Summary & Design Vision
- **Product Name**: LiveFootball
- **Product Type**: Native/cross-platform mobile football app for Android and iOS.
- **Product Aesthetic Tone**: Premium broadcast-style with sporty condensed typography, high-contrast live score emphasis, and fast match-day information scanning.
- **Target Experience**: Mobile-first football hub for live scores, personalized news, team/player details, rights-compliant live stream deep links, notifications, sharing, authentication, and GDPR-compliant personalization.
- **Core Design Principle**: Users must be able to open the app, identify current match status, access favorite team updates, and navigate to live/news/streams within seconds.
- **Performance-Aware UI Vision**: Visual design must support the operational requirement that the app is fully loaded and ready to use within a maximum of two seconds after startup. UI should use lightweight assets, skeleton loading states, cached content rendering, and restrained animation.

## 2. Color Theme & Palette
- **Mode Preference**: System-adaptive theme, automatically following device light/dark mode.
- **Primary Color**: Broadcast Navy `#07111F` for premium football/broadcast identity, top app surfaces, and dark-mode foundations.
- **Secondary / Accent Colors**:
  - Electric Pitch Green `#00C853` for live status, success, active selections, and positive match events.
  - Signal Red `#FF3B30` for urgent alerts, red cards, errors, and critical notification states.
  - Fixture Gold `#FFC107` for featured matches, highlights, premium/broadcast emphasis, and warning states.
  - Link Blue `#2F80ED` for stream deep links, external provider links, and interactive text links.
- **Dark Theme Background & Surface**:
  - App Background: `#07111F`
  - Primary Surface/Card: `#101B2D`
  - Elevated Surface: `#16243A`
  - Divider/Border: `#2A3A52`
  - Primary Text: `#F8FAFC`
  - Secondary Text: `#CBD5E1`
  - Muted Text: `#94A3B8`
- **Light Theme Background & Surface**:
  - App Background: `#F5F7FA`
  - Primary Surface/Card: `#FFFFFF`
  - Elevated Surface: `#EEF2F7`
  - Divider/Border: `#D7DEE8`
  - Primary Text: `#0F172A`
  - Secondary Text: `#475569`
  - Muted Text: `#64748B`
- **Live Match Color Rules**:
  - Live indicator: Electric Pitch Green `#00C853`, paired with text label `LIVE` for accessibility.
  - Goal event: Fixture Gold or green highlight depending on context; never rely on color alone.
  - Red card: Signal Red `#FF3B30` with card icon and accessible label.
  - Offline/stale data: Amber `#F59E0B` with explicit status message such as `Offline - showing cached updates`.
- **Contrast Requirements**:
  - All text and icons must meet WCAG 2.1 AA contrast minimums.
  - Critical live score and notification indicators should target enhanced contrast where practical.

## 3. Typography & Hierarchy
- **Stakeholder Preference**: Sporty condensed typography.
- **Primary Font Family**: `Roboto Condensed` for headings, scores, tabs, and football-data-heavy UI labels.
- **Fallback Fonts**: `Inter`, `Roboto`, `SF Pro`, `Arial`, sans-serif.
- **Body Font Recommendation**: Use `Inter` or platform-native system font for longer news article bodies if `Roboto Condensed` reduces readability in dense paragraphs.
- **Heading Hierarchy**:
  - H1 / Screen Title: 2rem / 32px, Bold, condensed, tight but readable line-height.
  - H2 / Section Title: 1.5rem / 24px, Semi-bold.
  - H3 / Card Title: 1.25rem / 20px, Semi-bold.
  - Match Score: 2rem-2.5rem / 32-40px, Bold, tabular numerals where available.
  - Body: 1rem / 16px, Regular.
  - Metadata / Timestamp: 0.875rem / 14px, Medium or Regular.
  - Bottom Navigation Label: 0.75rem / 12px, Medium.
- **Numeral Guidance**:
  - Use tabular numerals for scores, timers, standings, statistics, and match clocks to prevent layout shift during live updates.
- **Readability Rules**:
  - Do not use condensed fonts below 12px.
  - Preserve dynamic type/font scaling for accessibility.
  - Avoid all-caps body copy; reserve all-caps for short labels such as `LIVE`, `FT`, `HT`, and competition codes.

## 4. Layout & UI Structure
- **Navigation Style**: Bottom tab navigation.
- **Recommended Bottom Tabs**:
  1. Home
  2. Live
  3. News
  4. Teams
  5. Profile
- **Secondary Access Pattern**:
  - Stream links, settings, notification preferences, saved clubs, privacy/GDPR settings, and channel preferences should be accessible from contextual cards or Profile/Settings.
  - Search should be available from the Home and Teams areas, preferably via a top search icon or search bar.
- **Density**: Premium broadcast-style with moderately compact match data and spacious content cards. Use compact rows for live ticker lists, but provide enough padding for thumb-friendly interaction.
- **Card & Container Style**:
  - Card-based content layout with 12-16px border radius.
  - Subtle elevation/shadow in light mode.
  - Low-contrast borders and layered surfaces in dark mode.
  - Avoid heavy glassmorphism because performance and readability are higher priorities.
- **Mobile Layout Rules**:
  - Single-column primary layout for phones.
  - Bottom navigation must respect iOS safe areas and Android gesture navigation insets.
  - Primary tap targets must be at least 44x44pt / 48x48dp.
  - Critical live match information should be visible above the fold where possible.
  - Use sticky match headers for detailed live ticker pages.
- **Responsive Behavior**:
  - Small phones: prioritize live score, team names/logos, match minute, and status; collapse secondary statistics.
  - Large phones: show richer cards with more metadata and inline actions.
  - Tablets/foldables, if supported: use adaptive two-column layouts for news/live list plus detail view.

## 5. Component Guidelines

### 5.1 Authentication & Onboarding
- Login/registration should be visually simple and fast, available at startup without blocking casual browsing unless required.
- Use clear football-themed but lightweight visuals.
- Personalization onboarding should ask users to select favorite clubs, leagues, competitions, and sports channels with searchable multi-select chips.

### 5.2 Personalized Home Feed
- Use card-based modules: favorite team live status, top news, upcoming fixtures, recent results, and recommended streams when legally available.
- Provide visible personalization affordances: `Following`, `Manage Teams`, `Manage Channels`.
- News cards should include source/channel, timestamp, thumbnail, headline, and share action.

### 5.3 Live Ticker & Match Detail
- Live ticker screen must emphasize immediacy and scannability.
- Use a high-contrast `LIVE` pill, match clock, score block, and event timeline.
- Events should combine icon + label + color, e.g., goal icon, yellow/red card icon, substitution icon.
- Live updates should animate subtly without distracting or hurting performance.
- When network is limited, show `Reconnecting...` or `Showing cached data from [time]`.

### 5.4 Team, Player, League & Competition Detail Pages
- Use a consistent broadcast-style header with team/player image, badge, name, country/league, and follow button.
- Tabs may include Overview, Fixtures, Results, Squad, Stats, News.
- Tables for standings and stats should use compact rows, clear dividers, and sticky headers where appropriate.

### 5.5 Rights-Compliant Stream Deep Links
- Stream cards must clearly identify the provider, availability country/region, start status, and whether the stream is live.
- If rights are unavailable, show an explanatory disabled state rather than hiding context entirely where legally acceptable.
- External stream links should use Link Blue and include provider logo/name, e.g., DAZN or Sky Sport.

### 5.6 Notifications
- Notification settings should support favorite-team news, live score events, kickoff reminders, goals, full-time results, and breaking news.
- Use clear opt-in language and respect platform permission patterns.
- Notification status should be visually understandable through icons and toggles.

### 5.7 Sharing
- News and match report sharing should use platform-native share sheets.
- Share buttons should be available on article pages and key match-report cards.
- Ensure shared content does not expose private personalization data.

### 5.8 Offline & Limited Connectivity States
- Offline mode must be explicitly represented with persistent but non-intrusive status banners.
- Use stale-content labels such as `Last updated 14:32`.
- Cached items should remain readable, while unavailable real-time features should show clear disabled or reconnecting states.
- Avoid blank screens; use cached/skeleton/error fallback states.

### 5.9 GDPR, Privacy & Security UI
- Privacy settings must be easy to locate from Profile/Settings.
- Consent screens must use plain language and avoid dark patterns.
- Provide visible controls for personalization data, notification preferences, and account management.
- Security and GDPR-related messages should use professional, trust-building styling with clear confirmation states.

## 6. Accessibility Requirements
- **Standard**: Target WCAG 2.1 AA compliance for mobile UI.
- **Color Accessibility**:
  - Never communicate live states, goals, cards, errors, or offline status using color alone.
  - Pair color with iconography and text labels.
- **Touch Accessibility**:
  - Minimum touch target: 44x44pt on iOS and 48x48dp on Android.
  - Maintain comfortable spacing around bottom navigation and live ticker controls.
- **Text Accessibility**:
  - Support dynamic font scaling.
  - Avoid truncating team names without accessible full labels.
  - Provide readable line heights for news content.
- **Screen Reader Support**:
  - Live score updates should announce important events without overwhelming users.
  - Team badges, provider logos, and status icons must have meaningful accessible labels.
- **Motion Accessibility**:
  - Respect reduced-motion settings.
  - Live update animations should be subtle and optional.
- **Status Clarity**:
  - Online, reconnecting, offline, cached, stream unavailable, and rights-restricted states must be textually explicit.

## 7. Visual Style Rules
- **Preferred Style**: Premium broadcast-style.
- **Mood Keywords**: Fast, live, sporty, trustworthy, premium, data-rich, accessible.
- **Imagery**:
  - Use team badges, player photos, league marks, and provider logos where rights permit.
  - Use optimized images and lazy loading to protect startup speed.
- **Iconography**:
  - Use consistent line or filled icon style across tabs, event types, and actions.
  - Football-specific icons should be immediately recognizable: ball, whistle, card, substitution, stadium, TV/stream, bell.
- **Animation**:
  - Use minimal micro-interactions for tab changes, live event insertion, pull-to-refresh, and favorite toggles.
  - Avoid heavy transitions that delay perceived performance.
- **Brand Feel**:
  - Interface should feel closer to a professional sports broadcast companion than a casual social media feed.

## 8. Stakeholder Q&A History
| # | Topic | Question | Recorded Response |
|---|-------|----------|-------------------|
| 1 | Color Theme | What color theme should LiveFootball use: dark-first, light-first, or system-adaptive, and do you have any preferred primary brand color? | System adaptive |
| 2 | Typography | What typography style do you prefer for LiveFootball: modern sans-serif, sporty condensed, or a specific font family? | Sporty condensed |
| 3 | Navigation Layout | What navigation layout should the mobile app use: bottom tab navigation, top header navigation, hamburger menu, or another pattern? | Bottom tab navigation |
| 4 | Visual Style & Density | What overall visual style and screen density should LiveFootball use: clean sporty minimal, vibrant dynamic, premium broadcast-style, compact, spacious, or another preference? | Premium broadcast-style |

## 9. Documented Default Assumptions
- Since no specific brand color was provided, a premium broadcast palette is assumed: Broadcast Navy `#07111F`, Electric Pitch Green `#00C853`, Signal Red `#FF3B30`, Fixture Gold `#FFC107`, and Link Blue `#2F80ED`.
- Since no exact font family was named, `Roboto Condensed` is selected as the primary sporty condensed font, with `Inter`/system font fallbacks for long-form readability.
- Since no exact tab list was specified, the default bottom tabs are Home, Live, News, Teams, and Profile.
- Since no explicit density preference was provided beyond premium broadcast-style, the app should use moderately compact match-data layouts and spacious cards for news/detail content.
- Since accessibility specifics were not provided by the stakeholder, WCAG 2.1 AA, dynamic type support, sufficient touch targets, reduced-motion support, and non-color-only status communication are required.
- Since mobile responsive behavior was not specified in detail, the design assumes phone-first single-column layouts with adaptive enhancements for larger phones, tablets, and foldables.
- Since offline UI specifics were not provided, the design assumes clear offline/reconnecting/stale-data indicators and cached content fallback states.
- Since performance is a critical operational requirement, the design assumes lightweight assets, lazy loading, skeleton states, and restrained animation to support a two-second startup target.

## 10. Final Design Acceptance Criteria
- The app visually supports system-adaptive light and dark mode.
- Bottom tab navigation provides fast access to primary modules.
- Live score information is visually dominant, high-contrast, and accessible.
- News, teams, players, leagues, streams, notifications, and profile settings share consistent card and typography patterns.
- Offline, reconnecting, stale data, rights restriction, and notification permission states are explicitly represented.
- UI components remain usable on small mobile screens and scalable to larger devices.
- All primary flows maintain a premium sports broadcast feel without compromising app speed, clarity, or GDPR/privacy trust.
