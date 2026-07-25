# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a football fan, I want to select my favorite teams and sports channels so that I receive personalized news and live results.

- **Source:** FR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Selecting favorite teams and channels**
  - **Given:** Given I am logged into the app
  - **When:** When I navigate to the preferences section and select teams and channels
  - **Then:** Then my selections are saved and reflected in my news and live results feed

### US-002
**User Story:** As a football fan, I want to view current news about my favorite teams so that I stay informed.

- **Source:** FR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Viewing personalized news**
  - **Given:** Given I have selected favorite teams
  - **When:** When I open the news section
  - **Then:** Then I see news articles relevant to my selected teams

### US-003
**User Story:** As a football fan, I want to follow live results for my favorite teams so that I can track matches in real time.

- **Source:** FR-003
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Viewing live ticker**
  - **Given:** Given a match is in progress for my favorite team
  - **When:** When I open the live ticker module
  - **Then:** Then I see real-time updates for the match

### US-004
**User Story:** As a football fan, I want to access live stream links for matches when available and permitted in my country so that I can watch games live.

- **Source:** FR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Accessing live stream link with rights**
  - **Given:** Given a live broadcast is available and rights are fulfilled in my country
  - **When:** When I open the match details
  - **Then:** Then I see and can access the live stream link
- **Scenario: No rights for live stream**
  - **Given:** Given a live broadcast is not permitted in my country
  - **When:** When I open the match details
  - **Then:** Then I do not see the live stream link

### US-005
**User Story:** As a football fan, I want to view detailed team and player information so that I can learn more about them.

- **Source:** FR-004
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Viewing team and player details**
  - **Given:** Given I am on a team or player profile page
  - **When:** When I select a team or player
  - **Then:** Then I see detailed information about the selected team or player

### US-006
**User Story:** As a football fan, I want to share news and game reports via social media so that I can inform my friends.

- **Source:** FR-006
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Sharing news via social media**
  - **Given:** Given I am viewing a news article or game report
  - **When:** When I tap the share button
  - **Then:** Then I can select a social media platform and share the content

### US-007
**User Story:** As a football fan, I want to receive notifications about news and results for my favorite teams so that I stay updated.

- **Source:** FR-007
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Receiving notifications**
  - **Given:** Given I have enabled notifications
  - **When:** When news or results are available for my favorite teams
  - **Then:** Then I receive a push notification

### US-008
**User Story:** As a user, I want to register and log in easily at app startup so that I can access personalized features.

- **Source:** FR-008
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Simple registration and login**
  - **Given:** Given I have installed the app
  - **When:** When I open the app for the first time
  - **Then:** Then I can register or log in with minimal steps

### US-009
**User Story:** As a user, I want the app to load quickly and run smoothly so that I can use it without delays.

- **Source:** NFR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: App launch performance**
  - **Given:** Given the app is installed on my device
  - **When:** When I launch the app
  - **Then:** Then the app is fully loaded and ready within 2 seconds

### US-010
**User Story:** As a user, I want the app to function reliably even with limited network coverage so that I can use it offline.

- **Source:** NFR-003
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Offline usability**
  - **Given:** Given my device has no or limited network connectivity
  - **When:** When I use the app
  - **Then:** Then I can access core features and previously loaded data

### US-011
**User Story:** As a user, I want my personal data to be protected and processed in compliance with GDPR so that my privacy is ensured.

- **Source:** NFR-004
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: GDPR compliance**
  - **Given:** Given I have registered and use the app
  - **When:** When my personal data is processed
  - **Then:** Then it is handled according to GDPR requirements

### US-012
**User Story:** As a user, I want the app to be available on both Android and iOS devices so that I can use it on my preferred platform.

- **Source:** FR-009
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Cross-platform availability**
  - **Given:** Given I have an Android or iOS device
  - **When:** When I search for the app in the app store
  - **Then:** Then I can download and install the app with consistent features
