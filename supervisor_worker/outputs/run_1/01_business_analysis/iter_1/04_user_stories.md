# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a football fan, I want to select, update, and remove my favorite teams and sports channels so that I receive personalized news and live results.

- **Source:** FR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Selecting and updating favorite teams and channels**
  - **Given:** Given I am a registered user on the app
  - **When:** When I navigate to the preferences section and select, update, or remove teams and channels
  - **Then:** Then my selections are saved and reflected in my news and live results feed
- **Scenario: Enforcing selection limits**
  - **Given:** Given I have already selected the maximum number of teams or channels
  - **When:** When I attempt to add another team or channel
  - **Then:** Then I am prevented from exceeding the limit and shown an appropriate message

### US-002
**User Story:** As a football fan, I want to view current news about my favorite teams so that I stay informed.

- **Source:** FR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Displaying personalized news**
  - **Given:** Given I have selected favorite teams
  - **When:** When I open the news section
  - **Then:** Then I see news articles relevant to my selected teams

### US-003
**User Story:** As a football fan, I want to follow live results for my favorite teams so that I can track matches in real time.

- **Source:** FR-003
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Viewing live ticker updates**
  - **Given:** Given a match involving my favorite team is ongoing
  - **When:** When I open the live ticker module
  - **Then:** Then I see real-time updates for the match

### US-004
**User Story:** As a football fan, I want to access detailed information about teams and players so that I can learn more about them.

- **Source:** FR-004
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Accessing team and player profiles**
  - **Given:** Given I am on the team or player section
  - **When:** When I select a team or player
  - **Then:** Then I see detailed statistics and information

### US-005
**User Story:** As a football fan, I want to watch live streams of matches when available and permitted in my country so that I can view games directly.

- **Source:** FR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Accessing permitted live streams**
  - **Given:** Given a live broadcast is available and permitted in my country
  - **When:** When I open the live stream section
  - **Then:** Then I see and can access the live stream link
- **Scenario: Live stream not available due to rights**
  - **Given:** Given a live broadcast is not permitted in my country
  - **When:** When I open the live stream section
  - **Then:** Then I do not see the live stream link

### US-006
**User Story:** As a football fan, I want to receive notifications about news and results for my favorite teams, and choose which types of notifications I receive, so that I am always up to date without being overwhelmed.

- **Source:** FR-006
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Receiving notifications**
  - **Given:** Given I have enabled notifications and selected notification types
  - **When:** When a relevant news or result is available
  - **Then:** Then I receive a push notification of the selected type
- **Scenario: Customizing notification types**
  - **Given:** Given I am in the notification settings
  - **When:** When I select or deselect notification types (e.g., goals, news, match start/end)
  - **Then:** Then only the selected types are sent to me

### US-007
**User Story:** As a football fan, I want to share news and game reports via social media so that I can inform my friends.

- **Source:** FR-007
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Sharing news via social media**
  - **Given:** Given I am viewing a news article or game report
  - **When:** When I tap the share button
  - **Then:** Then I can select a social media platform and share the content

### US-008
**User Story:** As a user, I want to register and log in quickly at app startup using email or social login so that I can start using the app immediately.

- **Source:** FR-008
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Quick registration and login**
  - **Given:** Given I have just installed the app
  - **When:** When I open the app for the first time
  - **Then:** Then I can complete registration or login using email/password or a supported social login within a few steps

### US-009
**User Story:** As a user, I want the app to load and be ready within 2 seconds so that I can access information quickly.

- **Source:** NFR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: App launch performance**
  - **Given:** Given I launch the app on a supported device
  - **When:** When the app starts
  - **Then:** Then the app is fully loaded and ready within 2 seconds

### US-010
**User Story:** As a user, I want the app to function reliably even with poor or lost network connection so that I can continue using it.

- **Source:** NFR-003, FR-011
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Offline usability**
  - **Given:** Given my device loses network connection
  - **When:** When I continue using the app
  - **Then:** Then I can access cached news, results, and team/player information, and the app indicates offline status and last update time

### US-011
**User Story:** As a user, I want the app to remain stable and consistent after server updates so that I do not experience malfunctions.

- **Source:** FR-009, FR-010
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: UI and module consistency after server update**
  - **Given:** Given the external server has been updated
  - **When:** When I use the app
  - **Then:** Then the user interface and all modules remain functional and consistent

### US-012
**User Story:** As a user, I want my personal data to be protected and managed in compliance with GDPR so that I can control my privacy.

- **Source:** NFR-004, FR-012
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Requesting data deletion**
  - **Given:** Given I am a registered user
  - **When:** When I request account deletion
  - **Then:** Then my account and all associated personal data are deleted in compliance with GDPR
- **Scenario: Viewing data protection policy**
  - **Given:** Given I am using the app
  - **When:** When I access the privacy policy section
  - **Then:** Then I see clear information about data processing, retention, and deletion

### US-013
**User Story:** As a user, I want the app to be available for both Android and iOS so that I can use it on my preferred device.

- **Source:** NFR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Platform availability**
  - **Given:** Given I search for the app in the Google Play Store or Apple App Store
  - **When:** When I search for 'LiveFootball'
  - **Then:** Then I can find and install the app on both Android and iOS devices

### US-014
**User Story:** As a user, I want the app to remain responsive and performant even when many users are online so that I have a smooth experience.

- **Source:** NFR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: High concurrency performance**
  - **Given:** Given there are up to 100,000 users online simultaneously
  - **When:** When I use the app
  - **Then:** Then the app remains responsive and does not degrade in performance

### US-015
**User Story:** As a user, I want the app to be thoroughly tested and supported so that I can rely on its stability and receive help if needed.

- **Source:** NFR-006
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: App stability and support**
  - **Given:** Given I am using the app
  - **When:** When I encounter an issue
  - **Then:** Then the app has been tested to minimize malfunctions and I can access support resources
