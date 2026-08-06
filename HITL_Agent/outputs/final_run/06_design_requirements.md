# Visual & UI Design Requirements Specification

## 1. Executive Summary & Design Vision
- **Product Aesthetic Tone**: Sporty Dynamic with clean modern mobile patterns
- **Target Experience**: Mobile-first football companion app for Android and iOS focused on fast scanning, live updates, and responsive interaction
- **Design Intent**: Deliver a highly readable, energetic, and trustworthy sports experience that supports live match tracking, news consumption, stream discovery, and quick personalization while remaining performant under high information load.

## 2. Color Theme & Palette
- **Mode Preference**: Light Mode
- **Primary Color**: Green accent, recommended **#16A34A**
- **Secondary / Accent Colors**: **#15803D** (deep green), **#0EA5E9** (live/info accent), **#F59E0B** (alerts/highlights), **#DC2626** (critical/live score emphasis)
- **Background & Surface**: **#F8FAFC** (app background), **#FFFFFF** (primary surface), **#E5E7EB** (subtle borders/dividers)
- **Text Colors**: **#0F172A** (primary text), **#475569** (secondary text), **#94A3B8** (disabled/meta)
- **Usage Guidance**:
  - Use green as the primary CTA and brand highlight color.
  - Reserve red for match-critical alerts, score changes, and urgent statuses only.
  - Use blue sparingly for informational items such as live ticker tags and links.
  - Maintain strong contrast for outdoor mobile usage and quick in-motion scanning.

## 3. Typography & Hierarchy
- **Primary Font Family**: Modern sans-serif
- **Recommended Font**: **Inter** for UI consistency and mobile readability
- **Fallback Stack**: `Inter, Roboto, SF Pro Text, Helvetica Neue, Arial, sans-serif`
- **Heading Hierarchy**:
  - **H1**: 2rem (32px), Bold
  - **H2**: 1.5rem (24px), Semi-bold
  - **H3**: 1.25rem (20px), Semi-bold
  - **Body**: 1rem (16px), Regular
  - **Secondary Body**: 0.875rem (14px), Regular
  - **Caption / Meta**: 0.75rem (12px), Medium
- **Typography Guidance**:
  - Prioritize numeric legibility for scores, match times, league tables, and statistics.
  - Use medium or semi-bold weight for team names and live states.
  - Keep line lengths short and mobile-optimized for rapid reading.

## 4. Layout & UI Structure
- **Navigation Style**: Bottom tab navigation for primary app sections
- **Recommended Tab Structure**: Home, News, Live, Streams, Profile/More
- **Density**: Medium density leaning spacious for readability during live usage
- **Card & Container Style**: Rounded cards (12px radius), subtle shadow, clean layered surfaces
- **Page Structure Guidance**:
  - Sticky top header for context-specific actions such as search, filter, and notifications.
  - Bottom tabs remain persistent for fast one-thumb navigation.
  - Use modular feed cards for news, fixtures, scores, and team/player info.
  - Prioritize live ticker and breaking updates near the top of match-focused screens.
  - Use segmented controls/chips for league, team, and channel filtering.
- **Responsive Mockup Direction**:
  - Mobile-first layouts optimized for narrow screens first.
  - Support responsive HTML mockups for standard phone widths and larger tablet breakpoints.

## 5. UI Aesthetic & Component Guidelines
- **Style Direction**: Sporty Dynamic
- **Visual Character**:
  - Energetic but not cluttered
  - Strong hierarchy for scores, headlines, and live status
  - Clean iconography with subtle motion cues for real-time updates
- **Component Guidelines**:
  - **Buttons**: Rounded pill or 10px radius buttons, green primary CTA, outline secondary actions
  - **Live Tags**: High-contrast badges using green or red depending on state importance
  - **Cards**: Use clear separation, concise metadata, and thumbnail-first layout for news/streams
  - **Lists/Feeds**: Fast-scannable rows with timestamp, team badges, and status chips
  - **Notifications UI**: Compact banners and preference toggles with clear opt-in language
  - **Offline States**: Friendly empty/error states with retry action and cached content labeling
  - **Social Sharing**: Prominent but secondary action placement to avoid distracting from core live content
- **Motion Guidance**:
  - Use subtle transitions only; avoid heavy animation to protect perceived speed and battery performance.
  - Real-time score or ticker updates should animate minimally for change awareness.

## 6. Accessibility & Usability Considerations
- Ensure WCAG-aligned contrast ratios for text and key controls.
- Maintain tap targets of at least 44x44px for mobile accessibility.
- Use color plus text/icon cues for live status, alerts, and match events.
- Support readable states in low connectivity scenarios with visible sync/offline indicators.
- Prioritize information clarity for rapid use during live match contexts.

## 7. Stakeholder Q&A History
| # | Topic | Question | Recorded Response |
|---|-------|----------|-------------------|
| 1 | Color Theme | What color theme do you prefer for the app: light, dark, or both, and is there a primary brand/accent color you want us to use? | Light with a green accent |
| 2 | Typography | What typography style would you like: a specific font family if you have one, or should we use a modern sans-serif? | Sans serif is fine |
| 3 | Layout | For the app layout, do you prefer a bottom-tab mobile navigation with a clean spacious look, or a denser information-rich style? | Bottom tab navigation |
| 4 | Visual Style | What overall visual style do you want for the app: clean minimal, sporty dynamic, premium dark-broadcast inspired, or no strong preference? | Sporty dynamic |

## 8. Documented Default Assumptions
- Exact green brand shade was not specified; **#16A34A** is selected as a modern, energetic, football-appropriate primary green.
- Since no exact font family was named, **Inter** is chosen as the default modern sans-serif for strong mobile readability.
- Content density was not explicitly selected beyond navigation preference; a **medium-density, readability-first** layout is assumed to balance live data and usability.
- Component styling details were not provided; **rounded cards, subtle shadows, and clean modern surfaces** are assumed as the default mobile UI pattern.
- Because the product is a football app with live content, **sporty dynamic styling** is interpreted with strong hierarchy, status badges, quick-scan cards, and restrained motion.
- Responsive HTML mockups are assumed to follow a **mobile-first** design system with scalable behavior across Android and iOS screen sizes.
