# Visual & UI Design Requirements Specification

## 1. Executive Summary & Design Vision
- **Product Aesthetic Tone**: Sporty Dynamic with a modern mobile-first presentation
- **Target Experience**: Mobile football companion app for Android and iOS focused on rapid access to live scores, news, club updates, and streaming links
- **Design Intent**: Deliver an energetic, football-centric interface that feels fast, immersive, and easy to scan during live match situations while preserving clarity for news and player/team information

## 2. Color Theme & Palette
- **Mode Preference**: Dark Mode
- **Primary Color**: #16A34A (modern football-inspired green)
- **Secondary / Accent Colors**: #F59E0B (match highlights / alerts), #3B82F6 (links / informational actions), #EF4444 (critical live events / losses / urgent alerts)
- **Background & Surface**:
  - App Background: #0B1220
  - Primary Surface: #111827
  - Secondary Surface: #1F2937
  - Divider / Border: #334155
- **Text Colors**:
  - Primary Text: #F8FAFC
  - Secondary Text: #CBD5E1
  - Muted Text: #94A3B8
- **Usage Guidance**:
  - Green should communicate brand identity, selected states, and positive football actions.
  - Amber should highlight live or in-progress content without overwhelming the interface.
  - Blue should be reserved for links, stream entry points, and secondary call-to-action elements.
  - Red should be used sparingly for urgent alerts, dismissive states, or major match incidents when appropriate.

## 3. Typography & Hierarchy
- **Primary Font Family**: Modern sans-serif
- **Recommended Implementation Font**: Inter (default assumption aligned to stakeholder preference for sans-serif and strong mobile readability)
- **Fallback Fonts**: Roboto, SF Pro Text, Arial, sans-serif
- **Heading Hierarchy**:
  - H1: 2rem (32px), Bold
  - H2: 1.5rem (24px), Semi-bold
  - H3: 1.25rem (20px), Semi-bold
  - Body Large: 1.125rem (18px), Regular
  - Body: 1rem (16px), Regular
  - Secondary / Meta Text: 0.875rem (14px), Regular
  - Caption / Timestamp: 0.75rem (12px), Medium
- **Typography Guidance**:
  - Prioritize high legibility for live scores, timestamps, and ticker updates.
  - Use strong visual contrast between match scores, team names, and contextual metadata.
  - Avoid decorative or condensed fonts due to rapid live-content scanning needs.

## 4. Layout & UI Structure
- **Navigation Style**: Side Menu
- **Mobile Navigation Recommendation**: Side menu supported by a prominent home/dashboard landing screen and quick-access shortcuts for high-frequency actions such as Live, News, Favorites, and Notifications
- **Density**: Compact-to-balanced for efficient information display on mobile screens
- **Card & Container Style**: Rounded 12px cards, subtle shadow/elevation, high-contrast dark surfaces, strong section separation
- **Content Structure Guidance**:
  - Home screen should prioritize live matches, favorite team updates, and breaking news.
  - Live ticker views should use modular event rows with clear time markers and event icons.
  - Team and player detail screens should use tabbed or segmented sections for overview, squad, fixtures, and stats.
  - Stream links should be visually distinct but rights-sensitive, appearing only when allowed.
- **Interaction Style**:
  - Use fast, responsive transitions with minimal animation overhead to support performance targets.
  - Emphasize tap targets sized for mobile accessibility.
  - Support skeleton loading states for fast perceived performance during data fetches.

## 5. Component Guidelines
- **Buttons**:
  - Primary buttons: solid green fill (#16A34A) with white text
  - Secondary buttons: dark surface with green or blue outline
  - Destructive buttons: red accent used sparingly
- **Match Cards**:
  - Prominently display team crests, score, competition, match status, and kickoff/live indicators
  - Live status badge should use amber or green emphasis
- **News Cards**:
  - Include headline, source, timestamp, thumbnail, and quick-share affordance
- **Notification UI**:
  - Use concise alert chips and grouped notification lists with read/unread distinction
- **Forms / Authentication**:
  - Minimal fields, clear validation states, and social login styling if introduced later
- **Offline States**:
  - Show clear but unobtrusive offline banners and cached content indicators

## 6. Stakeholder Q&A History
| # | Topic | Question | Recorded Response |
|---|-------|----------|-------------------|
| 1 | Color Theme | What visual theme do you prefer for the app: dark, light, or both, and is there a primary brand color you want us to use? | dark |
| 2 | UI Style | What overall UI style should the app convey—for example clean minimal, sporty dynamic, premium broadcast, or corporate professional? | sporty dynamic |
| 3 | Typography | Do you have a preferred font family for the app, or should we choose a modern mobile-friendly sans-serif? | sans serif |
| 4 | Navigation | For the main app structure, would you prefer bottom tab navigation, a side menu, or another mobile navigation pattern? | side menu |

## 7. Documented Default Assumptions
- No explicit primary brand color was provided; a football-associated modern green (#16A34A) has been selected as the primary brand color.
- Because the stakeholder specified only “sans serif,” Inter is assumed as the implementation font due to its readability, clean hierarchy, and cross-platform suitability.
- Secondary accent colors were not specified; amber, blue, and red were chosen to support live states, links, and alerts in a sports context.
- Content density was not specified; a compact-to-balanced density was chosen to suit mobile live-score and news consumption.
- Card styling details were not specified; rounded dark cards with subtle elevation were selected to match a modern sporty dynamic dark interface.
- Although side menu navigation was requested, quick-access shortcuts on the landing screen are assumed to ensure efficient mobile usability for frequently used areas.

## 8. Final Design Direction
The LiveFootball app should adopt a dark, sporty, high-energy visual system optimized for rapid scanning and real-time engagement. The interface should feel modern and performance-conscious, using a green-led palette, readable sans-serif typography, compact mobile layouts, and strong emphasis on live content. The resulting design should balance football excitement with practical usability, especially during active match sessions and under variable network conditions.
