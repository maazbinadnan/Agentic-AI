# Requirements Elicitation Report

## 1. Discovered Target Personas

### Football Fan (Primary)
Wants to stay informed about football news, live results, and favorite teams. Likely to follow multiple teams, leagues, and competitions. Motivated by real-time updates, live streams, and personalized content.

### Casual Sports Viewer (Secondary)
Occasionally checks scores, news, or streams for major events. Less likely to personalize deeply, but values quick access and reliability.

### Social Sharer (Secondary)
Interested in sharing news and game reports via social media. Motivated by social engagement and spreading football content.

## 2. High-Level User Needs

### UN-001: I need to receive real-time news, live results, and updates about my favorite teams and leagues.
- **Target User Group :** UN-001: Primary
- **Target Persona:** Football Fan
- **User Journey Context:** User opens the app, selects favorite teams, and receives personalized news and live updates.

- **User Need Demand:** High

### UN-002: I need to watch live streams of football matches when available and permitted in my country.
- **Target User Group :** UN-002: Primary
- **Target Persona:** Football Fan
- **User Journey Context:** User navigates to a match, checks for live stream availability, and accesses the stream if rights are fulfilled.

- **User Need Demand:** High

### UN-003: I need the app to load quickly and run smoothly, even under high user load or poor network conditions.
- **Target User Group :** UN-003: Overarching
- **Target Persona:** All Users
- **User Journey Context:** User launches the app and expects it to be ready within two seconds, regardless of network or server load.

- **User Need Demand:** High

### UN-004: I need to personalize my app experience by selecting favorite teams, leagues, and notification preferences.
- **Target User Group :** UN-004: Primary
- **Target Persona:** Football Fan
- **User Journey Context:** User registers/logs in, selects preferences, and configures notifications for news and results.

- **User Need Demand:** High

### UN-005: I need to share football news and match reports directly to social media platforms from the app.
- **Target User Group :** UN-005: Secondary
- **Target Persona:** Social Sharer
- **User Journey Context:** User reads a news article or match report and uses the share function to post on social media.

- **User Need Demand:** Medium

### UN-006: I need assurance that my personal data is handled securely and in compliance with GDPR.
- **Target User Group :** UN-006: Overarching
- **Target Persona:** All Users
- **User Journey Context:** User registers, provides personal data, and expects privacy and data protection.

- **User Need Demand:** High

### UN-007: I need the app to remain usable and provide access to key information even when offline or with limited connectivity.
- **Target User Group :** UN-007: Overarching
- **Target Persona:** All Users
- **User Journey Context:** User loses network connection but continues to access cached news, results, or team info.

- **User Need Demand:** High

## 3. Elicitation Clarifying Questions & Stakeholder Responses

### Question [Q-01] - Topic: Live Stream Rights and Availability
- **Context / Reason:** The requirements mention compliance with transmission rights and country-based availability, but do not specify the mechanism or update frequency for rights management.
- **Question Posed:** How is the app determining whether live stream rights are fulfilled for a user’s country? Is there a real-time check or a static list, and how often is this updated?
- **Stakeholder Answer:** *test*

### Question [Q-02] - Topic: Offline Functionality Scope
- **Context / Reason:** The document states the app remains usable offline but does not clarify which modules or data are available without connectivity.
- **Question Posed:** Which specific features and data should remain accessible to users when the app is offline (e.g., cached news, live ticker, team/player info)?
- **Stakeholder Answer:** *test*

### Question [Q-03] - Topic: Personalization Limits
- **Context / Reason:** Personalization is mentioned, but the scope and constraints (if any) are not defined.
- **Question Posed:** Are there any limits to the number of favorite teams, leagues, or channels a user can select for personalization?
- **Stakeholder Answer:** *test*

### Question [Q-04] - Topic: Notification Preferences
- **Context / Reason:** Notification system is referenced, but granularity and user control over notifications are not specified.
- **Question Posed:** Can users customize the types of notifications they receive (e.g., only goals, only news, only match start/end), and can they set quiet hours or do-not-disturb periods?
- **Stakeholder Answer:** *test*

### Question [Q-05] - Topic: Social Media Integration
- **Context / Reason:** The document mentions sharing via social media but does not specify supported platforms or content limitations.
- **Question Posed:** Which social media platforms are supported for sharing news and reports, and are there any restrictions on the content that can be shared?
- **Stakeholder Answer:** *test*

### Question [Q-06] - Topic: Registration and Login Methods
- **Context / Reason:** Registration and login are described as uncomplicated, but the specific methods and options are not detailed.
- **Question Posed:** What authentication methods are supported for registration and login (e.g., email/password, social login, biometric)?
- **Stakeholder Answer:** *test*

### Question [Q-07] - Topic: Data Retention and User Control
- **Context / Reason:** GDPR compliance is stated, but data retention policies and user controls are not described.
- **Question Posed:** How long is user data retained, and what options do users have to view, export, or delete their data in compliance with GDPR?
- **Stakeholder Answer:** *test*

### Question [Q-08] - Topic: High Load Handling
- **Context / Reason:** The requirement for high concurrent usage is stated, but technical approaches for scalability and reliability are not specified.
- **Question Posed:** What specific strategies or technologies will be used to ensure performance and stability when serving up to 100,000 simultaneous users?
- **Stakeholder Answer:** *test*
