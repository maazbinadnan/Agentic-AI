# Visual & UI Design Requirements Specification

## 1. Executive Summary & Design Vision
- **Product Aesthetic Tone**: Sporty Dynamic with gradients
- **Target Experience**: Mobile-first football companion app for Android and iOS focused on fast access to live scores, news, team details, and streaming links
- **Design Intent**: Deliver a lively, modern football experience that feels energetic and easy to scan while preserving fast perceived performance and readability under frequent real-time updates

## 2. Color Theme & Palette
- **Mode Preference**: Light Mode
- **Primary Color**: Green-cyan accent, recommended base **#14B8A6**
- **Secondary / Accent Colors**:
  - Deep green **#16A34A**
  - Cyan highlight **#06B6D4**
  - Alert/live status red **#EF4444**
  - Neutral dark text **#0F172A**
- **Background & Surface**:
  - App background **#FFFFFF**
  - Secondary surface **#F8FAFC**
  - Card surface **#FFFFFF**
  - Divider/border **#E2E8F0**
- **Gradient Direction**: Use green-to-cyan gradients for hero banners, live match highlights, and selected CTA areas, e.g. **linear-gradient(135deg, #16A34A 0%, #06B6D4 100%)**
- **Usage Guidance**:
  - Use white and very light neutrals for primary backgrounds to maintain clarity
  - Reserve gradients for emphasis areas to avoid visual overload
  - Red should be used sparingly for live indicators, urgent alerts, and score-change emphasis

## 3. Typography & Hierarchy
- **Primary Font Family**: Inter
- **Fallback Font Family**: System UI sans-serif stack for Android/iOS performance resilience
- **Heading Hierarchy**:
  - H1: 2rem (32px), Bold
  - H2: 1.5rem (24px), Semi-bold
  - H3: 1.25rem (20px), Semi-bold
  - H4: 1.125rem (18px), Medium
  - Body: 1rem (16px), Regular
  - Secondary Body: 0.875rem (14px), Regular
  - Caption / Meta: 0.75rem (12px), Medium
- **Typography Guidance**:
  - Prioritize legibility for scorelines, live ticker updates, team names, and match metadata
  - Use bold weights for match state, scores, and section headers
  - Maintain strong contrast for outdoor/mobile viewing conditions

## 4. Layout & UI Structure
- **Navigation Style**: Hamburger menu as the primary global navigation pattern
- **Mobile Layout Orientation**: Card-based mobile feed with modular sections for news, live ticker, fixtures, standings, and streaming links
- **Density**: Spacious by default (applied as a default assumption due to no density preference provided)
- **Card & Container Style**: Rounded 12px cards with light shadow and occasional gradient headers for featured/live content
- **Screen Structure Guidance**:
  - Home screen should prioritize live content and favorite teams
  - Persistent quick-access entry points should be available for news, live scores, leagues, favorites, and settings
  - Use stacked sections with clear separators for scan-friendly browsing
  - Critical live match information should appear above the fold on relevant screens
- **Interaction Guidance**:
  - Large touch targets suitable for mobile use
  - Smooth transitions and lightweight animations only where they support responsiveness
  - Loading states should be skeleton-based and minimal to reinforce the under-2-second startup perception

## 5. Component Guidelines
- **Buttons**:
  - Primary buttons use green-cyan gradient fill with white text
  - Secondary buttons use white or light background with green/cyan outline
  - Border radius: 10px to 12px
- **Live Ticker Elements**:
  - Live badges in red with white text
  - Score updates should use bold typography and color cues for event significance
  - Timeline events should be visually segmented for quick scanning
- **News Cards**:
  - Include club/channel imagery, headline, source, and timestamp
  - Use clean thumbnail-led layouts with concise metadata
- **Team/Player Info Panels**:
  - Emphasize statistics in grouped cards
  - Use tabs or segmented controls for squads, stats, fixtures, and history
- **Streaming Link Presentation**:
  - Clearly indicate provider availability and geo-rights compliance status
  - Use disabled/inactive visual states where streams are unavailable
- **Notifications & Alerts**:
  - Use concise, high-contrast status chips
  - Distinguish informational, success, warning, and live-event states with accessible color coding

## 6. Stakeholder Q&A History
| # | Topic | Question | Recorded Response |
|---|-------|----------|-------------------|
| 1 | Color Theme | What visual theme do you want for the app: light, dark, or both, and do you have a preferred primary brand color? | Light; white background and green accent as primary brand color; green-cyan |
| 2 | Typography | Which typography style do you prefer for the app: a modern sans-serif font like Inter/Roboto, or another font direction? | Inter |
| 3 | UI Style | For the overall UI style, do you prefer a clean minimal look, a sporty dynamic style, or a more corporate/professional look? | Sporty dynamic with gradients |
| 4 | Layout | What navigation and layout pattern do you prefer on mobile: bottom tab navigation, hamburger menu, or another structure, and should the content feel compact or spacious? | Hamburger menu |

## 7. Documented Default Assumptions
- Since no explicit content density preference was provided, the app will use a **spacious** mobile layout to improve scanability for live scores, news, and team content.
- Since no secondary font family or alternative typographic styling was specified, **system sans-serif fallbacks** will be used after Inter for performance and platform consistency.
- Since no explicit component shape language was provided, a **modern rounded card style** with 10px–12px radius and subtle shadows is assumed.
- Since no dark mode requirement was requested, the product will launch with **light-mode-first visual optimization**.
- Since no explicit navigation secondary pattern was specified, the hamburger menu will be complemented by **contextual quick actions and prominent home screen shortcuts** to reduce navigation depth on mobile.

## 8. Final Design Recommendation
The LiveFootball app should adopt a **light, high-contrast, sporty mobile design system** built around **white surfaces, green-cyan brand accents, Inter typography, rounded cards, and selective gradient emphasis**. The visual style should feel energetic and football-centric without sacrificing clarity or speed. Information-heavy modules such as live ticker, results, and team data should remain clean, touch-friendly, and highly readable, ensuring that real-time content is easy to consume even during peak usage or unstable network conditions.
