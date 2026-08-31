# Visual & UI Design Requirements Specification

## 1. Executive Summary & Design Vision
- **Product Aesthetic Tone**: Energetic sports-focused
- **Target Experience**: Mobile-first football companion app for Android and iOS with fast scanning of live updates, news, team/player data, stream availability, and notifications
- **Design Intent**: Deliver a lively, high-clarity sports experience that feels immediate during match days while maintaining strong usability, performance perception, and touch-friendly interactions.

## 2. Color Theme & Palette
- **Mode Preference**: Light Mode
- **Primary Color**: `#042D13`
- **Secondary / Accent Colors**:
  - Accent Green: `#0B5E2B`
  - Live Action Highlight: `#16A34A`
  - Attention / Score Alert: `#DC2626`
  - Link / Interactive Accent: `#2563EB`
- **Background & Surface**:
  - App Background: `#F8FAFC`
  - Primary Surface / Cards: `#FFFFFF`
  - Secondary Surface: `#EEF2F7`
  - Divider / Border: `#D6DEE8`
- **Text Colors**:
  - Primary Text: `#0F172A`
  - Secondary Text: `#475569`
  - Inverse Text on Dark Green: `#FFFFFF`
- **Usage Guidance**:
  - Use `#042D13` for primary CTAs, active navigation states, and key brand identifiers.
  - Use red sparingly for urgent live match events, score changes, and critical alerts.
  - Maintain high contrast for readability in outdoor/mobile viewing conditions.

## 3. Typography & Hierarchy
- **Primary Font Family**: Inter
- **Typography Style**: Modern sans-serif
- **Heading Hierarchy**:
  - H1: 2rem (32px), Bold
  - H2: 1.5rem (24px), Semi-bold
  - H3: 1.25rem (20px), Semi-bold
  - Body Large: 1.125rem (18px), Regular
  - Body: 1rem (16px), Regular
  - Caption / Meta: 0.875rem (14px), Medium
- **Typography Guidance**:
  - Prioritize strong legibility and quick scanability for live scores, timestamps, league labels, and breaking news.
  - Use tabular numerals where possible for match clocks, scorelines, and statistics.
  - Limit decorative type treatments; emphasis should come from weight, spacing, and color rather than complex styling.

## 4. Layout & UI Structure
- **Navigation Style**: Mobile bottom tab navigation for primary sections, supported by top headers within screens
- **Recommended Primary Tabs**: Home, Live, News, Following, Profile
- **Density**: Spacious mobile layout with larger cards and touch targets
- **Card & Container Style**: Rounded 12px to 16px cards, subtle shadow, clear section separation
- **Touch Target Guidance**:
  - Minimum tap target: 44x44px
  - Larger primary CTAs for stream links, follow actions, and live match entry points
- **Content Structure Guidance**:
  - Home screen should prioritize personalized content modules and current live matches above general news
  - Live ticker screens should surface scoreline, match minute, event timeline, and key actions with minimal visual clutter
  - Team/player detail views should use modular cards for stats, fixtures, squad, and related news
  - Notification and preference controls should be simple, clear, and reachable within a few taps
- **Performance-Oriented UX Guidance**:
  - Use skeleton loaders and progressive content loading to reinforce the app’s fast-start perception
  - Avoid overly heavy visual effects that may reduce perceived responsiveness on lower-end devices

## 5. UI Aesthetic & Component Guidelines
- **Overall Style Direction**: Energetic sports-focused with modern mobile polish
- **Visual Character**:
  - Strong use of brand green as an anchor color
  - Clean layouts balanced with dynamic emphasis for live content
  - Clear hierarchy for urgent vs routine information
- **Component Guidelines**:
  - Buttons: Filled primary buttons in `#042D13`, rounded corners, bold labels
  - Live Badges: Bright green or red-accented pills for live/urgent states
  - News Cards: Large thumbnail, concise headline, source/time metadata
  - Match Cards: Team crests, scoreline, match status, CTA to detailed ticker
  - Chips/Filters: Rounded pills for leagues, teams, channels, and preferences
  - Forms: Minimal fields, large inputs, prominent validation messaging for login/registration
- **Iconography**:
  - Use simple modern line or duotone icons with consistent stroke weight
  - Football-specific icons should remain secondary to text clarity
- **Motion**:
  - Use subtle transitions for score/event updates, tab changes, and state changes
  - Keep animations short and purposeful to support speed and not distract from live content

## 6. Stakeholder Q&A History
| # | Topic | Question | Recorded Response |
|---|-------|----------|-------------------|
| 1 | Visual Style | What overall visual style should LiveFootball have: clean minimal, energetic sports-focused, premium broadcast-style, or another direction? | energetic sports |
| 2 | Color Theme | Do you prefer a dark mode, light mode, or support for both, and is there a primary brand color you want to use? | light and this should be the primary color 042d13 |
| 3 | Typography | What font style would you like for the app—modern sans-serif, more editorial/broadcast feeling, or no preference? | modern |
| 4 | Layout Density | For the mobile layout, do you want a compact information-dense interface or a more spacious layout with larger cards and touch targets? | larger cards and touch targets |

## 7. Documented Default Assumptions
- Because the stakeholder specified only a modern font style and not a named typeface, **Inter** is selected as the default primary font due to strong mobile readability and broad UI suitability.
- Because no secondary palette was specified, a modern sports-app supporting palette was defined around the primary green, with blue for interactive accents and red for urgent live states.
- Because navigation pattern was not specified, a **mobile bottom tab navigation** model is assumed as the most appropriate for Android and iOS football apps with multiple high-frequency sections.
- Because card styling was not specified, rounded cards with subtle shadows are assumed to support touch-friendly, modern mobile presentation.
- Because no dark mode requirement beyond light mode was requested, the app will be designed primarily for **light mode only** at this stage.
- Because the product must feel fast and smooth, heavy glassmorphism or visually expensive effects are excluded by default in favor of lightweight modern UI treatments.
