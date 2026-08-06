# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `startup_auth_mockup.html` | US-005, US-009 | App startup welcome screen, Login form, Registration form, Invalid credential error state, Privacy notice link and consent text, Authenticated entry CTA |
| `home_news_competitions_mockup.html` | US-001, US-002, US-008 | Main app shell with navigation, Personalized news feed, Competition cards, Team and player detail panels, Preferred channels filter chips, Offline banner, Cached content state, Live-content unavailable messaging |
| `preferences_notifications_mockup.html` | US-002, US-006, US-009 | Favorite teams selection, Preferred sports channels selection, Notification toggle, Saved preferences summary, Validation/error hint, Privacy/settings persistence note |
| `live_match_center_mockup.html` | US-003, US-004, US-008 | Live ticker timeline, Auto-update indicator, Live data unavailable state, Eligible live stream link state, Geo-rights restricted/hidden stream state, Offline live-data warning |
| `content_share_mockup.html` | US-007 | News article detail, Match report card, Share action button, Device share sheet modal, No sharing target available error state |

---

## UI/UX Design Decisions & Trade-offs

### Combined Startup Authentication Screen
Login and registration are placed in a tabbed single-screen startup layout to keep the startup flow compact and clearly satisfy quick access requirements. The trade-off is slightly denser presentation, but it reduces navigation overhead for new and returning users.

### Single Home Screen for News, Competitions, Teams, and Players
US-001 is visualized in one dashboard-style screen with modular sections instead of multiple isolated pages. This improves discoverability and demonstrates centralized content access, though individual detail pages are represented as embedded side panels rather than full-page transitions.

### Preferences and Notifications Combined
Favorite teams, preferred channels, and notifications are grouped into one settings screen because the stories are tightly related and share stored account preferences. This simplifies mental models, but creates a longer settings page.

### Live Match Screen Shows Multiple States Together
To cover acceptance criteria efficiently, the live match center includes populated, unavailable, restricted, and offline examples within one mockup. This is useful for specification review, though a production app would show these as separate runtime states.

### Native Share Sheet Represented as Modal Wireframe
Because actual device sharing UI is platform-native, the mockup uses a modal approximation to communicate intent. This preserves story traceability without inventing a custom sharing system.
