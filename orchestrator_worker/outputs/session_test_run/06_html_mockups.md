# HTML Mockups

## Interaction Design Overview

### 1. Screen Architecture & Mapping

| Screen / File Name           | Mapped User Story / Requirement | Key Interactions & States Visualized                                                                                   |
| :---------------------------| :------------------------------ | :--------------------------------------------------------------------------------------------------------------------- |
| `startup_loading.html`       | US-001, FR-001, NFR-001         | Fast loading indicator, performance alert state                                                                        |
| `login_register.html`        | US-006, FR-007                  | Login/registration form, error/validation state                                                                        |
| `news_feed.html`             | US-002, FR-002                  | News list (populated), empty state, share action (US-007)                                                              |
| `personalization.html`       | US-003, FR-004, FR-008          | Team/channel selection, update state                                                                                   |
| `live_ticker.html`           | US-004, FR-005                  | Live match updates (real-time), API connection lost state                                                              |
| `match_stream.html`          | US-005, FR-006                  | Live stream link (rights fulfilled), rights not fulfilled message                                                      |
| `offline_info.html`          | US-008, FR-010, NFR-003         | Cached data view, no cached data state                                                                                 |
| `feedback.html`              | US-009, FR-011, NFR-006         | Feedback form, submission confirmation, error state                                                                    |

---

### 2. UI/UX Design Notes & Trade-offs

- **Startup & Performance (US-001):** The loading screen uses a simple spinner and a performance alert banner that appears if loading exceeds the target. No extra navigation or branding is added to keep the focus on speed.
- **Login/Register (US-006):** A single form with toggles for login/registration, clear error messaging, and guidance. No social login is included due to lack of requirement detail.
- **News Feed (US-002, US-007):** News items are shown in cards with league tags and a share button. The empty state is clearly indicated. The share action is visualized as a button, but actual platform selection is not shown (per scope).
- **Personalization (US-003):** Teams and channels are selectable via checkboxes. The update state is shown with a confirmation banner. No notification preference granularity is included, as not specified.
- **Live Ticker (US-004):** Real-time updates are represented with a refresh indicator. API connection loss is shown with a status banner and last data.
- **Match Stream (US-005):** If rights are fulfilled, a prominent stream link is shown; otherwise, a rights message replaces the link.
- **Offline Info (US-008):** Cached data is shown in a simple list; if no data, a clear message is displayed.
- **Feedback (US-009):** A feedback form with confirmation and error states. No app store review link, as in-app form is specified.

---

### 3. Generated File Status

- [x] Saved `startup_loading.html` using `write_output_file`
- [x] Saved `login_register.html` using `write_output_file`
- [x] Saved `news_feed.html` using `write_output_file`
- [x] Saved `personalization.html` using `write_output_file`
- [x] Saved `live_ticker.html` using `write_output_file`
- [x] Saved `match_stream.html` using `write_output_file`
- [x] Saved `offline_info.html` using `write_output_file`
- [x] Saved `feedback.html` using `write_output_file`

---

**If you would like to see the HTML for a specific screen, please specify which file(s) to display.**