# Interaction Design (IxD) & Mockup Specifications

## HTML Mockups to User Stories Mapping

| HTML File | Mapped User Stories | Visualizations / Components |
|---|---|---|
| `onboarding_favorites.html` | US-001 | Favorite teams selection grid, Sports channels selection list, Save preferences button, Error/validation state for empty selection |
| `dashboard_news_live.html` | US-002 | Personalized news feed, Live results ticker, Sample populated state, Empty state (no favorites), Error state (network issue) |
| `team_player_profile.html` | US-003 | Team profile card, Player profile card, Detailed stats section, Sample populated state, Empty state (no data) |
| `match_detail_stream.html` | US-004 | Match detail header, Live stream link (if permitted), No rights message (error state), Sample populated state |
| `notifications_settings.html` | US-005 | Notification toggle switch, Favorite teams notification list, Sample notification preview, Error state (push permission denied) |
| `news_share.html` | US-006 | News article preview, Share button, Social media platform selection modal, Error state (share failed) |
| `startup_performance.html` | US-007 | Splash/loading screen, Progress indicator, Loaded state (dashboard) |
| `offline_access.html` | US-008 | Offline banner, Cached content display, Error state (no cached data) |
| `gdpr_compliance.html` | US-009 | GDPR consent modal, Privacy policy link, Sample consent toggle, Error state (consent not given) |
| `high_concurrency.html` | US-010 | Performance status indicator, Simultaneous user count display, Error state (performance degraded) |
| `registration_login.html` | US-011 | Registration form, Login form, Quick access button, Error/validation state (invalid input) |

---

## UI/UX Design Decisions & Trade-offs

### Modal vs. Dedicated Page for GDPR Consent
A modal is used for GDPR consent to avoid disrupting the onboarding flow, but ensures compliance. Pros: Keeps user in context, quick interaction. Cons: May be dismissed too quickly.

### Grid vs. List for Team Selection
Grid layout for favorite teams allows quick visual scanning and selection. Pros: Efficient, visually engaging. Cons: May be less accessible for screen readers.

### Inline Error Messaging
Inline error messages are used for validation (e.g., empty selection, invalid input) to provide immediate feedback. Pros: Reduces user confusion. Cons: May clutter UI if too many errors.

### Offline Banner Placement
Offline banner is placed at the top of the screen for visibility. Pros: Immediate awareness. Cons: May push content down, less space for main content.

### Share Modal vs. Inline Share Buttons
Share modal allows selection of platform after tapping share. Pros: Flexible, supports multiple platforms. Cons: Extra step for user.
