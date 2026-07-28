# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a football fan, I want to follow live scores and results of my favorite teams in real time so that I stay updated during matches.
- **Source:** FR-001
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: Live Score Update**
  - **Given:** The app is running and the user has selected favorite teams.
  - **When:** A match is ongoing and the live ticker receives new data.
  - **Then:** The app displays updated scores in real time.
- **Scenario: Network Loss**
  - **Given:** The app is running and the network connection is lost.
  - **When:** The user tries to access live scores.
  - **Then:** The app displays cached scores and informs the user of offline mode.

### US-002
**User Story:** As a football fan, I want to view current football news and updates about my favorite teams and leagues so that I stay informed.
- **Source:** FR-002
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: News Feed Display**
  - **Given:** The app is running and the user has selected favorite teams.
  - **When:** The user opens the news section.
  - **Then:** The app displays relevant news articles.
- **Scenario: No News Available**
  - **Given:** The app is running and no news is available.
  - **When:** The user opens the news section.
  - **Then:** The app displays a message indicating no news is available.

### US-003
**User Story:** As a football fan, I want to watch live streams of football matches when available and permitted so that I can view games live.
- **Source:** FR-003
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: Rights Fulfilled**
  - **Given:** A live broadcast is ongoing and rights are fulfilled in the user's country.
  - **When:** The user selects a live stream link.
  - **Then:** The app opens the live stream.
- **Scenario: Rights Not Available**
  - **Given:** A live broadcast is ongoing but rights are not fulfilled.
  - **When:** The user selects a live stream link.
  - **Then:** The app displays a message that the stream is unavailable.

### US-004
**User Story:** As a football fan, I want to personalize my app experience by selecting favorite teams and sports channels so that I receive relevant content.
- **Source:** FR-004
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: Favorite Selection**
  - **Given:** The user is registering or updating settings.
  - **When:** The user selects favorite teams and channels.
  - **Then:** The app saves preferences and updates content.
- **Scenario: No Selection**
  - **Given:** The user skips favorite selection.
  - **When:** The app loads.
  - **Then:** The app displays general content.

### US-005
**User Story:** As a football fan, I want to receive notifications about news, scores, and events related to my favorite teams so that I never miss important updates.
- **Source:** FR-005
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: Notification Opt-In**
  - **Given:** The user has enabled notifications.
  - **When:** A relevant event occurs.
  - **Then:** The app sends a notification.
- **Scenario: Notification Opt-Out**
  - **Given:** The user has disabled notifications.
  - **When:** A relevant event occurs.
  - **Then:** The app does not send a notification.

### US-006
**User Story:** As a football fan, I want to access detailed information about teams and players at any time so that I can learn more about them.
- **Source:** FR-006
- **Priority:** Should Have

**Acceptance Criteria:**
- **Scenario: Team/Player Details**
  - **Given:** The app is running.
  - **When:** The user selects a team or player.
  - **Then:** The app displays detailed information.

### US-007
**User Story:** As a football fan, I want to share news and game reports via social media directly from the app so that I can inform my friends.
- **Source:** FR-007
- **Priority:** Should Have

**Acceptance Criteria:**
- **Scenario: Share News**
  - **Given:** The user is viewing a news article.
  - **When:** The user selects the share option.
  - **Then:** The app opens sharing options for social media.

### US-008
**User Story:** As a football fan, I want to register and log in easily to access personalized features so that I can use the app fully.
- **Source:** FR-008
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: Registration Success**
  - **Given:** The app is at startup.
  - **When:** The user completes registration.
  - **Then:** The app grants access to personalized features.
- **Scenario: Login Failure**
  - **Given:** The app is at startup.
  - **When:** The user enters incorrect credentials.
  - **Then:** The app displays an error message.

### US-009
**User Story:** As a football fan, I want the app to maintain a consistent user interface that connects and manages all modules so that I can navigate easily.
- **Source:** FR-009
- **Priority:** Must Have

**Acceptance Criteria:**
- **Scenario: UI Consistency**
  - **Given:** The app is running.
  - **When:** The user navigates between modules.
  - **Then:** The app maintains consistent layout and navigation.

### US-010
**User Story:** As a football fan, I want the app to evaluate user feedback and app reviews to improve functionality so that my experience gets better over time.
- **Source:** FR-010
- **Priority:** Should Have

**Acceptance Criteria:**
- **Scenario: Feedback Submission**
  - **Given:** The user is in the feedback section.
  - **When:** The user submits feedback.
  - **Then:** The app records feedback for evaluation.
