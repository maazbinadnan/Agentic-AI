# 4. User Stories & Acceptance Criteria

### US-001
**User Story:** As a football fan, I want to select my favorite teams and sports channels so that I receive personalized news and live results on all my devices.

- **Source:** FR-001
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Selecting and syncing favorite teams and channels**
  - **Given:** the user is logged in and on the preferences screen
  - **When:** the user selects teams and channels and saves preferences
  - **Then:** the system updates the user's profile in the cloud and displays personalized content on all devices

### US-002
**User Story:** As a football fan, I want to view current news about my favorite teams so that I stay informed, even when offline.

- **Source:** FR-002
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Displaying personalized news online**
  - **Given:** the user has selected favorite teams and is online
  - **When:** the user opens the news section
  - **Then:** the system displays news relevant to the selected teams
- **Scenario: Displaying cached news offline**
  - **Given:** the user has previously viewed news and is offline
  - **When:** the user opens the news section
  - **Then:** the system displays the most recently cached news articles

### US-003
**User Story:** As a football fan, I want to follow live results for my favorite teams so that I can track matches in real time and see the latest results even when offline.

- **Source:** FR-003
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Viewing live ticker online**
  - **Given:** the user has selected favorite teams and is online
  - **When:** the user opens the live ticker module
  - **Then:** the system displays real-time match data for those teams
- **Scenario: Viewing cached results offline**
  - **Given:** the user has previously viewed live results and is offline
  - **When:** the user opens the live ticker module
  - **Then:** the system displays the most recently cached results

### US-004
**User Story:** As a football fan, I want to receive push notifications about news and results for my favorite teams and choose which types of notifications I receive so that I only get relevant updates.

- **Source:** FR-004
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Receiving news notifications**
  - **Given:** the user has enabled notifications for news
  - **When:** a relevant news update occurs
  - **Then:** the system sends a push notification to the user
- **Scenario: Receiving results notifications**
  - **Given:** the user has enabled notifications for results
  - **When:** a relevant result update occurs
  - **Then:** the system sends a push notification to the user
- **Scenario: Disabling notification types**
  - **Given:** the user has disabled notifications for news
  - **When:** a news update occurs
  - **Then:** the system does not send a notification for news

### US-005
**User Story:** As a football fan, I want to access live stream links for matches when available and permitted in my country so that I can watch games live, and I want to be sure the links are current and rights-compliant.

- **Source:** FR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Displaying live stream links when rights are fulfilled**
  - **Given:** the user is viewing a match detail, transmission rights are fulfilled, and the live broadcast has begun
  - **When:** the user opens the match detail
  - **Then:** the system displays the current live stream link
- **Scenario: Hiding live stream links when rights are not fulfilled**
  - **Given:** the user is in a country without rights for the stream
  - **When:** the live broadcast has begun
  - **Then:** the system does not display the live stream link
- **Scenario: Updating live stream links**
  - **Given:** a live stream provider updates the link
  - **When:** the provider's API sends a new link
  - **Then:** the system updates the link in the app in real time

### US-006
**User Story:** As a football fan, I want to view detailed information about teams and players so that I can learn more about them, even when offline.

- **Source:** FR-006
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Viewing team and player details online**
  - **Given:** the user is online and on a team or player profile page
  - **When:** the user selects a team or player
  - **Then:** the system displays detailed information about the selection
- **Scenario: Viewing cached team and player details offline**
  - **Given:** the user has previously viewed a team or player profile and is offline
  - **When:** the user selects the same team or player
  - **Then:** the system displays the most recently cached information

### US-007
**User Story:** As a football fan, I want to share news and game reports via Facebook, Twitter, or WhatsApp so that I can inform my friends.

- **Source:** FR-007
- **Priority:** Medium

**Acceptance Criteria:**
- **Scenario: Sharing news via supported platforms**
  - **Given:** the user is viewing a news article or game report
  - **When:** the user taps the share button and selects Facebook, Twitter, or WhatsApp
  - **Then:** the system shares the content via the chosen platform

### US-008
**User Story:** As a football fan, I want to register and log in quickly at app startup using email/password or my Google, Apple, or Facebook account so that I can access the app without delay.

- **Source:** FR-008
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Quick registration and login with email/password**
  - **Given:** the user has just installed the app
  - **When:** the user opens the app for the first time and chooses email/password
  - **Then:** the system presents a simple registration/login process and grants access to main features
- **Scenario: Quick registration and login with third-party authentication**
  - **Given:** the user has just installed the app
  - **When:** the user opens the app for the first time and chooses Google, Apple, or Facebook
  - **Then:** the system authenticates via the selected provider and grants access to main features

### US-009
**User Story:** As a football fan, I want to access all main features from a unified interface so that I can easily navigate the app.

- **Source:** FR-009
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Unified interface navigation**
  - **Given:** the user is logged in
  - **When:** the user opens the app
  - **Then:** the system displays a user interface with direct access to news, live ticker, streams, and team/player info

### US-010
**User Story:** As a user, I want to request export, deletion, or correction of my personal data so that I can exercise my GDPR rights.

- **Source:** NFR-005
- **Priority:** High

**Acceptance Criteria:**
- **Scenario: Requesting data export**
  - **Given:** the user is logged in and navigates to the privacy settings
  - **When:** the user requests a data export
  - **Then:** the system provides the user with a downloadable file containing their personal data
- **Scenario: Requesting data deletion**
  - **Given:** the user is logged in and navigates to the privacy settings
  - **When:** the user requests deletion of their account and data
  - **Then:** the system deletes the user's account and personal data in compliance with GDPR
- **Scenario: Requesting data correction**
  - **Given:** the user is logged in and navigates to the privacy settings
  - **When:** the user submits a correction request
  - **Then:** the system processes the correction and updates the user's data
