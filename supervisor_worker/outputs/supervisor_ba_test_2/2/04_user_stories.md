# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a football fan, I want the app to load and display the main dashboard within 2 seconds so that I can quickly access news and live scores.

- **Source:** FR-001, NFR-001, UN-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Successful fast app launch**
  - **Given:** the app is installed on a supported device and closed
  - **When:** the user launches the app
  - **Then:** the main dashboard with news, live scores, and team/player info is fully loaded within 2 seconds
- **Scenario: App launch under poor network conditions**
  - **Given:** the device has limited connectivity
  - **When:** the user launches the app
  - **Then:** the dashboard loads previously cached data within 2 seconds
- **Scenario: API latency tolerance**
  - **Given:** the app is online and API response time is up to 500ms
  - **When:** the user launches the app
  - **Then:** the dashboard loads and displays current data within 2 seconds

### US-002
**User Story:** As a user, I want to select my favorite teams, sports channels, notification preferences, and news types so that I receive personalized news and live updates.

- **Source:** FR-002, UN-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Selecting favorite teams, channels, and preferences**
  - **Given:** the user is logged in
  - **When:** the user navigates to preferences and selects teams, channels, notification types, and news categories
  - **Then:** the app saves the preferences and displays personalized content
- **Scenario: Selecting notification types granularity**
  - **Given:** the user is editing notification preferences
  - **When:** the user selects or deselects notification types (goals, cards, match start, match end, news, transfers)
  - **Then:** the app updates the notification settings accordingly

### US-003
**User Story:** As a user, I want to receive real-time notifications about my favorite teams according to my preferences so that I never miss important news or results.

- **Source:** FR-003, UN-003, UN-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Receiving a notification for a favorite team**
  - **Given:** the user has enabled notifications and selected favorite teams and notification types
  - **When:** a relevant news or result event occurs (goal, card, match start, match end, news, transfer)
  - **Then:** the user receives a push notification on their device

### US-004
**User Story:** As a user, I want to access live stream links for matches when available and permitted so that I can watch games directly from the app.

- **Source:** FR-004, NFR-006, UN-004
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Live stream available and permitted**
  - **Given:** the user is in a country with broadcast rights and a live match is ongoing
  - **When:** the user opens the match details
  - **Then:** the app displays the live stream link
- **Scenario: Live stream not permitted in region**
  - **Given:** the user is in a country without broadcast rights
  - **When:** the user opens the match details
  - **Then:** the app does not display the live stream link

### US-005
**User Story:** As a user, I want to share news and match reports via Facebook, Twitter, WhatsApp, and Instagram so that I can engage with my friends.

- **Source:** FR-005, UN-005
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Sharing a news article**
  - **Given:** the user is viewing a news article
  - **When:** the user taps the share button and selects Facebook, Twitter, WhatsApp, or Instagram
  - **Then:** the article is shared to the selected platform

### US-006
**User Story:** As a user, I want the app to remain usable and display cached news, scores, and team/player information for up to 7 days even when offline so that I can access information anytime.

- **Source:** FR-006, NFR-005, UN-006, UN-012, FR-013
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Offline access to cached data**
  - **Given:** the user has previously loaded news, scores, and team/player info
  - **When:** the device is offline and the user opens the app
  - **Then:** the app displays the cached news, scores, and team/player info from the past 7 days
- **Scenario: Cached data older than 7 days**
  - **Given:** the user has not connected to the internet for more than 7 days
  - **When:** the user opens the app offline
  - **Then:** the app notifies the user that cached data is outdated and prompts to reconnect
- **Scenario: Automatic cache refresh when online**
  - **Given:** the device is online and cached data is older than the latest available
  - **When:** the user opens the app
  - **Then:** the app automatically refreshes news, scores, and team/player info
- **Scenario: Manual cache refresh**
  - **Given:** the device is online
  - **When:** the user taps the manual refresh button
  - **Then:** the app fetches and updates news, scores, and team/player info
- **Scenario: API latency tolerance for offline refresh**
  - **Given:** the device is online and API response time is up to 500ms
  - **When:** the user triggers a manual or automatic refresh
  - **Then:** the app updates cached data and remains responsive

### US-007
**User Story:** As a product manager, I want the app to support up to 100,000 concurrent users without performance loss so that we can handle high traffic on match days.

- **Source:** FR-007, NFR-002, UN-007
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: High concurrency during match day**
  - **Given:** 100,000 users are connected simultaneously
  - **When:** users access live scores and news
  - **Then:** the app remains responsive and performant

### US-008
**User Story:** As a user, I want my personal data to be processed securely and in compliance with GDPR so that my privacy is protected.

- **Source:** FR-008, NFR-003, UN-008
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: GDPR-compliant data processing**
  - **Given:** the user registers and uses the app
  - **When:** personal data is transmitted or stored
  - **Then:** the data is encrypted and processed according to GDPR

### US-009
**User Story:** As a new user, I want to register and log in quickly at app startup using email/password or third-party authentication so that I can start using the app without delay.

- **Source:** FR-009, UN-009
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Successful registration and login with email/password**
  - **Given:** the user opens the app for the first time
  - **When:** the user completes the registration/login form with email and password
  - **Then:** the user is logged in and directed to the main dashboard
- **Scenario: Successful registration and login with third-party authentication**
  - **Given:** the user opens the app for the first time
  - **When:** the user selects Google, Apple, or Facebook login and completes authentication
  - **Then:** the user is logged in and directed to the main dashboard

### US-010
**User Story:** As a product manager, I want the app to be thoroughly tested and improved based on user feedback so that malfunctions are minimized and user satisfaction increases.

- **Source:** FR-010, UN-010
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Pre-release testing**
  - **Given:** the app is ready for release
  - **When:** QA testing is performed
  - **Then:** all critical issues are resolved before launch
- **Scenario: Continuous improvement from in-app feedback**
  - **Given:** the app is live and users submit feedback via in-app forms
  - **When:** feedback is received
  - **Then:** feedback is reviewed and prioritized for future releases
- **Scenario: Continuous improvement from app store reviews**
  - **Given:** the app is live and receives app store reviews
  - **When:** reviews are analyzed
  - **Then:** improvements are planned and implemented in future releases

### US-011
**User Story:** As a user, I want to use the app in English, German, Spanish, French, or Italian so that I can interact with the app in my preferred language.

- **Source:** FR-011, UN-011
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Language selection during onboarding**
  - **Given:** the user opens the app for the first time
  - **When:** the app detects or prompts for language selection
  - **Then:** the app displays all content and UI in the selected language
- **Scenario: Changing language in settings**
  - **Given:** the user is logged in
  - **When:** the user changes the language in app settings
  - **Then:** the app updates all content and UI to the new language

### US-012
**User Story:** As a user, I want live stream links to open in an in-app browser or native player so that I have a seamless viewing experience.

- **Source:** FR-012, UN-013
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Opening live stream in-app**
  - **Given:** the user taps a live stream link
  - **When:** the stream is available and permitted
  - **Then:** the stream opens in an in-app browser or native player, not an external browser
- **Scenario: Advanced playback features out of scope**
  - **Given:** the user is viewing a live stream
  - **When:** the user attempts to use Chromecast, AirPlay, or picture-in-picture
  - **Then:** the app does not provide these features
