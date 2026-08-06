# Visual & UI Design Requirements Specification

## 1. Executive Summary & Design Vision
- **Product Aesthetic Tone**: Clean Minimalist, sports-focused mobile interface
- **Target Experience**: Mobile-first football companion app for Android and iOS with fast access to news, live ticker, notifications, favorites, and sharing
- **Design Priorities**:
  - Fast scanning and low-friction interaction to support the 2-second load target
  - Clear hierarchy for live scores, match updates, and news content
  - Consistent, touch-friendly navigation optimized for one-handed mobile use
  - Readability under variable mobile network conditions and intermittent offline access

## 2. Color Theme & Palette
- **Mode Preference**: Light Mode
- **Primary Color**: #16A34A (modern football-inspired green, selected as default due to no brand color provided)
- **Secondary / Accent Colors**:
  - #2563EB (action/link blue)
  - #F59E0B (live/highlight amber)
  - #EF4444 (alerts, score/event emphasis)
- **Background & Surface**:
  - App Background: #F8FAFC
  - Primary Surface/Card: #FFFFFF
  - Secondary Surface: #F1F5F9
  - Border/Divider: #E2E8F0
- **Text Colors**:
  - Primary Text: #0F172A
  - Secondary Text: #475569
  - Disabled Text: #94A3B8
- **Usage Guidance**:
  - Use green as the primary brand/action color for key CTAs and selected states
  - Use amber sparingly for live ticker and in-progress match indicators
  - Use red only for critical alerts, breaking moments, or event urgency
  - Maintain strong contrast for accessibility and outdoor mobile viewing

## 3. Typography & Hierarchy
- **Primary Font Family**: Inter
- **Rationale**: Selected as a modern mobile-friendly default because the stakeholder requested a mobile default rather than a specific font family
- **Fallback Stack**: Inter, Roboto, SF Pro Text, Helvetica Neue, Arial, sans-serif
- **Heading Hierarchy**:
  - H1: 2rem (32px), Bold
  - H2: 1.5rem (24px), Semi-bold
  - H3: 1.25rem (20px), Semi-bold
  - H4: 1.125rem (18px), Medium
  - Body Large: 1rem (16px), Regular
  - Body: 0.9375rem (15px), Regular
  - Caption/Meta: 0.8125rem (13px), Regular
  - Micro Label: 0.75rem (12px), Medium
- **Typography Rules**:
  - Prioritize legibility over decorative styling
  - Use semibold weights for match titles, team names, and key headlines
  - Keep line lengths short on mobile screens to improve scanning
  - Use tabular numerals where available for scores, timers, and statistics

## 4. Layout & UI Structure
- **Navigation Style**: Bottom Tab Navigation
- **Recommended Primary Tabs**:
  - Home
  - News
  - Live
  - Favorites
  - Profile
- **Density**: Compact-to-balanced mobile density for quick scanning without visual clutter
- **Screen Structure**:
  - Sticky top app bar per screen for title, search, filter, or contextual actions
  - Bottom tab bar for primary navigation
  - Scrollable content feed with modular cards
- **Card & Container Style**: Rounded 12px cards, subtle shadow, light borders, clean flat surfaces
- **Spacing System**:
  - Base spacing unit: 8px
  - Standard padding: 16px
  - Card gap: 12px
- **Interaction Design**:
  - Touch targets minimum 44x44px
  - Pull-to-refresh on news and live data views
  - Skeleton loaders for news lists and match feeds
  - Clear offline/limited connectivity status banners
- **Content Prioritization**:
  - Live scores and current match states should appear above secondary metadata
  - Favorites should influence home feed ordering
  - News cards should emphasize source, timestamp, team association, and share action

## 5. Component Guidelines
- **Buttons**:
  - Primary: Filled green (#16A34A), white text, rounded 10px
  - Secondary: White/neutral surface with green border or text
  - Tertiary: Text-only for less prominent actions
- **Tabs & Navigation**:
  - Active state uses primary green with strong icon-label contrast
  - Inactive state uses muted slate text/icons
- **Cards**:
  - Use for news stories, live matches, team/player summaries, and stream-link modules
  - Important live cards may include amber status chips
- **Badges/Chips**:
  - Live: Amber background or outline
  - Breaking/Alert: Red accent
  - League/Filter chips: Neutral surface with active green state
- **Forms**:
  - Login/registration should remain visually simple with minimal fields and progressive disclosure
  - Input fields should use 10px radius, clear labels, and inline validation states
- **Notifications UI**:
  - Distinguish breaking match events from general news using iconography and accent color
  - Allow quick toggles for favorite clubs and event categories
- **Offline/Low Network States**:
  - Show cached content with clear “last updated” timestamps
  - Use unobtrusive warning banners rather than blocking modals where possible

## 6. Accessibility & Performance-Oriented Design Notes
- Maintain WCAG-appropriate contrast, especially for live indicators and text over cards
- Avoid visually heavy effects such as glassmorphism or large blur layers to support performance on mobile devices
- Keep animation minimal and purposeful to preserve responsiveness under constrained conditions
- Ensure iconography is recognizable and paired with labels in navigation
- Support dynamic content expansion without breaking hierarchy during live updates

## 7. Stakeholder Q&A History
| # | Topic | Question | Recorded Response |
|---|-------|----------|-------------------|
| 1 | Color Theme | What visual theme do you want for the app: light, dark, or both, and is there a preferred primary brand color? | Light mode requested; no primary brand color specified |
| 2 | UI Style | What overall UI style should the app have—for example clean minimal, sporty dynamic, corporate professional, or something else? | Clean minimal |
| 3 | Typography | Do you have a preferred font family for the app, or should I choose a modern mobile-friendly default? | Mobile default |
| 4 | Layout & Navigation | For the app structure, do you prefer bottom tab navigation, a top header style, or should I select the most suitable mobile layout? | Bottom tab navigation |

## 8. Documented Default Assumptions
- Since no brand color was specified, a modern football-appropriate green (#16A34A) is selected as the primary color.
- Since the stakeholder requested a mobile default font rather than naming one, Inter is selected as the primary font family.
- Secondary and semantic accent colors were assigned to support sports content clarity: blue for links/actions, amber for live states, and red for alerts.
- A compact-to-balanced density was chosen to help users scan live scores, news, and updates quickly on mobile.
- Rounded cards, subtle shadows, and clean flat surfaces were selected to align with the requested clean minimal style while preserving performance.
- A sticky top app bar within screens was added in combination with bottom tabs as the most suitable mobile structure for content-heavy football workflows.

## 9. Final Design Direction Summary
The LiveFootball app should use a **light-mode, clean minimal, mobile-first visual system** with **bottom tab navigation**, **Inter typography**, and a **sports-inspired green primary palette**. The UI should emphasize rapid content scanning, high readability, lightweight rendering performance, and clear distinction between news, live match events, notifications, and personalized favorites.