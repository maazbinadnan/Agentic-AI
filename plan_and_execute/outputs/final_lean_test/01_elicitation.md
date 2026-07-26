# Requirements Elicitation Report

## 1. Discovered Target Personas

### Football Fan (Primary)
Wants to stay informed about football news, live scores, and team/player information. Motivated by real-time updates, following favorite teams, and accessing live streams.

### Casual Sports Viewer (Secondary)
Occasionally checks football news or live scores, may not follow specific teams closely but values easy access to major events and highlights.

### Social Sharer (Secondary)
Enjoys sharing football news and match reports on social media, motivated by social engagement and community interaction.

## 2. High-Level User Needs

### UN-001: Stay up-to-date with real-time football news and live scores for favorite teams and leagues.
- **Target Persona:** Football Fan
- **User Journey Context:** Opens app to check latest news and live results, especially during match days.

### UN-002: Personalize app experience by selecting favorite teams and preferred sports channels.
- **Target Persona:** Football Fan
- **User Journey Context:** Configures app after registration to follow specific clubs and channels.

### UN-003: Access live stream links for ongoing matches, subject to regional rights.
- **Target Persona:** Football Fan
- **User Journey Context:** Receives notification or browses app to find and watch live streams when matches start.

### UN-004: Receive timely notifications about news and results related to favorite teams.
- **Target Persona:** Football Fan
- **User Journey Context:** Enables notifications to get instant updates on team news and match outcomes.

### UN-005: Share football news and match reports via social media platforms.
- **Target Persona:** Social Sharer
- **User Journey Context:** Reads an article or match report and shares it directly from the app.

### UN-006: Use the app reliably even with limited or intermittent network connectivity.
- **Target Persona:** All Users
- **User Journey Context:** Continues to access previously loaded content or basic features when offline or with poor signal.

### UN-007: Register and log in quickly and easily at app startup.
- **Target Persona:** All Users
- **User Journey Context:** Completes registration or login process with minimal steps upon first use.

### UN-008: Trust that personal data is handled securely and in compliance with GDPR.
- **Target Persona:** All Users
- **User Journey Context:** Provides personal information during registration, expecting privacy and data protection.

## 3. Elicitation Clarifying Questions & Stakeholder Responses

### Question [Q-01] - Topic: Offline Functionality
- **Context / Reason:** The document states the app remains usable offline but does not specify which modules or data are available without connectivity.
- **Question Posed:** Which specific features and content should remain accessible to users when the app is offline (e.g., previously loaded news, live ticker, team/player info)?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-02] - Topic: Live Stream Rights Management
- **Context / Reason:** The requirements mention compliance with transmission rights but do not detail the technical or business rules for regional access control.
- **Question Posed:** How should the app determine and enforce live stream availability based on user location and transmission rights? Is there a list of supported countries or a rights management API?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-03] - Topic: User Personalization Limits
- **Context / Reason:** The document allows users to select favorites but does not specify any constraints, which may impact UI and backend design.
- **Question Posed:** Is there a limit to the number of favorite teams or sports channels a user can select and follow?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-04] - Topic: Notification Preferences
- **Context / Reason:** The requirements mention notifications but do not clarify the level of user control over notification types.
- **Question Posed:** Can users customize which types of notifications they receive (e.g., only goals, news, match start/end), and how granular should these preferences be?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-05] - Topic: Social Media Sharing Scope
- **Context / Reason:** The document states users can share content via social media but does not specify which platforms are in scope.
- **Question Posed:** Which social media platforms should be supported for sharing news and match reports directly from the app?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-06] - Topic: Registration Methods
- **Context / Reason:** The requirements mention uncomplicated registration but do not specify the authentication mechanisms.
- **Question Posed:** What registration and login methods should be supported (e.g., email/password, social login, phone number)?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-07] - Topic: Data Retention and Deletion
- **Context / Reason:** The document states GDPR compliance but does not specify user rights or processes for data management.
- **Question Posed:** What are the requirements for user data retention, deletion, and export in compliance with GDPR?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*

### Question [Q-08] - Topic: User Interface Customization
- **Context / Reason:** The requirements mention users can connect their own interface but do not clarify the scope or technical means for customization.
- **Question Posed:** To what extent can users configure or connect their own interface to the app? Are there APIs or themes available for user-driven UI customization?
- **Stakeholder Answer:** *No response provided (Default assumptions applied).*
