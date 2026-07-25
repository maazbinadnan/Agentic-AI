# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a football fan, I want to select my favorite teams and sports channels so that I receive personalized news and results.

- **Source:** FR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Selecting favorite teams and channels**
  - **Given:** Given I am a registered user on the app
  - **When:** When I navigate to the preferences section and select teams and channels
  - **Then:** Then my selections are saved and reflected in my news and results feed

### US-002
**User Story:** As a football fan, I want to view current news about my favorite teams so that I stay informed.

- **Source:** FR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Viewing personalized news feed**
  - **Given:** Given I have selected favorite teams
  - **When:** When I open the news section
  - **Then:** Then I see news articles relevant to my selected teams

### US-003
**User Story:** As a football fan, I want to follow live results of my favorite teams so that I can track matches in real time.

- **Source:** FR-003
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Viewing live ticker for favorite teams**
  - **Given:** Given I have selected favorite teams
  - **When:** When I open the live ticker module
  - **Then:** Then I see real-time match results for my teams

### US-004
**User Story:** As a football fan, I want to access detailed team and player information so that I can learn more about them.

- **Source:** FR-004
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Accessing team/player details**
  - **Given:** Given I am on the team or player page
  - **When:** When I select a team or player
  - **Then:** Then I see detailed information about the selection

### US-005
**User Story:** As a football fan, I want to watch live streams of matches when available and permitted so that I can view games directly.

- **Source:** FR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Accessing live stream links with rights check**
  - **Given:** Given a live broadcast is available and rights are fulfilled in my country
  - **When:** When I open the match page
  - **Then:** Then I see and can access the live stream link
- **Scenario: Live stream not available due to rights**
  - **Given:** Given a live broadcast is not permitted in my country
  - **When:** When I open the match page
  - **Then:** Then I do not see the live stream link

### US-006
**User Story:** As a football fan, I want to register and log in easily at app startup so that I can access personalized features.

- **Source:** FR-006
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Successful registration and login**
  - **Given:** Given I am on the app startup screen
  - **When:** When I enter valid credentials or register
  - **Then:** Then I am logged in and taken to the main dashboard

### US-007
**User Story:** As a football fan, I want to enable or disable notifications for my favorite teams so that I control what alerts I receive.

- **Source:** FR-007
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Managing notification preferences**
  - **Given:** Given I am in the notification settings
  - **When:** When I enable or disable notifications for teams
  - **Then:** Then I receive alerts only for the teams I have enabled

### US-008
**User Story:** As a football fan, I want to share news and game reports via social media so that I can inform my friends.

- **Source:** FR-008
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Sharing news via social media**
  - **Given:** Given I am viewing a news article or game report
  - **When:** When I tap the share button and select a social platform
  - **Then:** Then the content is shared on the selected platform

### US-009
**User Story:** As a football fan, I want to access news, results, and team/player information offline so that I can use the app without internet.

- **Source:** FR-009
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Offline access to cached content**
  - **Given:** Given I have previously loaded content
  - **When:** When I lose internet connection
  - **Then:** Then I can still view cached news, results, and information
