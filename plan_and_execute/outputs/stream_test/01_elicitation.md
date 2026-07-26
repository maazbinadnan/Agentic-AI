# Requirements Elicitation Report

## 1. Discovered Target Personas

### Football Fan (Primary)
Wants to stay informed about football news, live results, and team/player information. Motivated by real-time updates, following favorite teams, and accessing live streams.

### Casual Sports Viewer (Secondary)
Occasionally checks scores, news, or streams for major events. Less likely to personalize deeply but values quick access and reliability.

### Social Sharer (Secondary)
Enjoys sharing football news and match reports via social media. Motivated by social engagement and spreading information.

## 2. High-Level User Needs

### UN-001: Stay comprehensively informed about football news, results, and team/player information in real time.
- **Target Persona:** Football Fan
- **User Journey Context:** Opens app to check latest news, live scores, and team updates.

### UN-002: Personalize app experience by selecting favorite teams and preferred sports channels.
- **Target Persona:** Football Fan
- **User Journey Context:** Configures app after registration to follow specific clubs and channels.

### UN-003: Access live stream links for matches when available and permitted in their country.
- **Target Persona:** Football Fan
- **User Journey Context:** Receives notification or browses app to find and watch live streams.

### UN-004: Receive timely notifications about news and results for favorite teams.
- **Target Persona:** Football Fan
- **User Journey Context:** Enables notifications to stay updated on important events.

### UN-005: Share news and match reports via social media directly from the app.
- **Target Persona:** Social Sharer
- **User Journey Context:** Reads an article or report and shares it with friends on social platforms.

### UN-006: Use the app reliably even with limited or no network coverage.
- **Target Persona:** All Users
- **User Journey Context:** Continues to access previously loaded content or basic features when offline.

### UN-007: Register and log in quickly and easily at app startup.
- **Target Persona:** All Users
- **User Journey Context:** Completes registration or login process without friction upon first use.

## 3. Elicitation Clarifying Questions & Stakeholder Responses

### Question [Q-01] - Topic: Live Stream Rights and Availability
- **Context / Reason:** The requirements mention compliance with transmission rights but do not specify the mechanism for checking or updating rights per country, which is critical for legal compliance and user experience.
- **Question Posed:** How is the app determining whether live stream rights are fulfilled in a user's country? Is there a real-time check or a static list, and how often is this updated?
- **Stakeholder Answer:** *real time check through an external API we call*

### Question [Q-02] - Topic: Offline Functionality Scope
- **Context / Reason:** The document states the app remains usable offline but does not clarify the extent of offline capabilities or data retention policies.
- **Question Posed:** Which specific features and data are available to users when the app is offline? For example, can users view previously loaded news, scores, or team information, and for how long is this data cached?
- **Stakeholder Answer:** *only previously loaded news and scores and cached for 24 hours*

### Question [Q-03] - Topic: Notification Preferences
- **Context / Reason:** The requirements mention notifications but do not specify the level of user control over notification types, which impacts user satisfaction and engagement.
- **Question Posed:** Can users customize which types of notifications they receive (e.g., only for favorite teams, only for goals, or for news updates), and how granular is this control?
- **Stakeholder Answer:** *only for favourite teams and the team;'s match updates*

### Question [Q-04] - Topic: User Personalization Limits
- **Context / Reason:** The document mentions personalization but does not specify any constraints, which could affect performance and user experience.
- **Question Posed:** Is there a limit to the number of favorite teams or channels a user can select for personalization?
- **Stakeholder Answer:** *yes upto 5 teams and 3 channels*

### Question [Q-05] - Topic: Social Media Sharing Scope
- **Context / Reason:** The requirements state users can share content via social media but do not specify which platforms are integrated, which affects technical implementation and user expectations.
- **Question Posed:** Which social media platforms are supported for sharing news and match reports directly from the app?
- **Stakeholder Answer:** *instagram and whatsapp only*

### Question [Q-06] - Topic: Data Caching and Privacy
- **Context / Reason:** The document emphasizes GDPR compliance but does not detail local data handling, which is crucial for privacy and legal adherence.
- **Question Posed:** How is user data (such as favorite teams, notification preferences, and cached content) stored and protected on the device, especially in offline mode, to ensure GDPR compliance?
- **Stakeholder Answer:** *it is encrypted*

### Question [Q-07] - Topic: Registration and Login Methods
- **Context / Reason:** The requirements mention uncomplicated registration and login but do not specify supported authentication methods, which impacts usability and security.
- **Question Posed:** What authentication methods are supported for registration and login (e.g., email/password, social login, biometric)?
- **Stakeholder Answer:** *email/password and 0auth using google or facebook accounts*
