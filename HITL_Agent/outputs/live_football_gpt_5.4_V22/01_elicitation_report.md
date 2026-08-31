# Elicitation Report

## 1. Original Requirements Text

> We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## 2. Stakeholder Q&A History

### Q1. Offline / Limited Connectivity Scope
- **Question:** What exact user actions and content must remain available when the app is offline or under limited network coverage?
- **Why asked:** The document states the app remains usable offline and under limited coverage, but does not define which features must still work.
- **Stakeholder answer:** cached data like news, stories and scores
- **Verified interpretation:** Offline usage is limited to previously cached content, specifically news, stories, and scores. Real-time refresh and live API retrieval are assumed unavailable without network connectivity.

### Q2. Live Stream Integration Behavior
- **Question:** Are live stream links meant only to redirect users to external providers such as DAZN or Sky Sport, or should any video playback happen inside the app?
- **Why asked:** The requirements mention live stream link integration but do not clarify whether video streaming is embedded or external.
- **Stakeholder answer:** only deep links
- **Verified interpretation:** The app will not host or embed live video playback. It will provide deep links to external licensed streaming providers only.

### Q3. Core User Roles in Scope
- **Question:** Which core user roles are in scope for this release: only end users of the mobile app, or also internal/admin users who manage news sources, leagues, teams, rights availability, or notifications?
- **Why asked:** The product includes configurable content and rights-aware streaming links, but the scope of administrative capabilities is unspecified.
- **Stakeholder answer:** end users
- **Verified interpretation:** Only mobile end users are in scope for this release. No internal/admin portal or content management workflows are included in this requirements set.

### Q4. Authentication Requirement
- **Question:** Must registration/login be mandatory at app startup for all users, or can users browse core content first and sign in only for personalization features such as favorites and notifications?
- **Why asked:** The requirements mention registration and login at startup but do not clearly state whether authentication is mandatory.
- **Stakeholder answer:** yes it is mandarory
- **Verified interpretation:** User registration/login is mandatory at app startup before app usage.

## 3. Documented Assumptions

The following gaps were not escalated as stakeholder questions because they were lower priority than the core scope issues above, or because reasonable domain assumptions can be documented for downstream analysis.

### 3.1 Performance Assumptions
- “Fully loaded and ready to use within two seconds after starting” is interpreted as an app cold-start target under normal supported device/network conditions, not a guarantee under all network states or on all legacy devices.
- “Without performance loss” for 100,000 simultaneous users is interpreted as maintaining core app availability and acceptable response behavior for critical user journeys, not literal zero degradation in all non-critical features.

### 3.2 Real-Time Data Assumptions
- “Real time” live ticker updates are assumed to mean near-real-time updates dependent on the external data provider API rather than deterministic sub-second delivery.
- Match events, scores, and status updates are assumed to be sourced entirely from an external API and are dependent on third-party feed availability and latency.

### 3.3 Content Scope Assumptions
- “All leagues and competitions, both national and international” is treated as a business ambition rather than a guaranteed day-one exhaustive catalog, unless later constrained by licensing, feed availability, and commercial agreements.
- Team and player information is assumed to be read-only informational content for end users.
- News from favorite teams and preferred sports channels is assumed to be filtered/personalized content presentation, not user-generated content.

### 3.4 Notifications Assumptions
- Notifications are assumed to be opt-in and user-controlled, because the requirements say they are sent once the notification function is activated.
- Notification types are assumed to include at least news and result updates for favorited teams.

### 3.5 Rights and Geo-Availability Assumptions
- Stream link visibility is assumed to be controlled by country-based rights rules, likely using device/account region and/or IP-based geo-detection managed by backend/provider logic.
- Compliance with broadcast rights is assumed to be satisfied by only displaying eligible deep links and relying on the external provider for final playback authorization.

### 3.6 Offline Behavior Assumptions
- Offline functionality is limited to access to previously cached content: news, stories, and scores.
- Actions that require live connectivity—such as login validation, fresh live ticker retrieval, opening provider deep links, and receiving push notifications—are assumed unavailable until connectivity returns.

### 3.7 User Management Assumptions
- Registration/login being mandatory at startup implies anonymous browsing is out of scope.
- Supported authentication methods are assumed to be standard app account registration/login unless specified otherwise later; no social login, SSO, or MFA requirement is stated.

### 3.8 Platform and Sharing Assumptions
- The mobile app is assumed to support both Android and iOS native distribution through their standard app stores.
- Social sharing is assumed to use native OS share sheets or equivalent platform-standard mechanisms.

### 3.9 Security and Privacy Assumptions
- GDPR compliance is assumed to require consent management, lawful basis for data processing, user data transparency, and mechanisms for user data rights handling, though these are not explicitly detailed in the source document.
- Personal data is assumed to include at minimum account/profile data, favorites/personalization settings, and notification preferences.

### 3.10 Risks / Notable Remaining Gaps
- The exact list of supported leagues, competitions, countries, and content providers is still unspecified.
- No measurable SLA is defined for live ticker freshness, push notification delivery time, or API recovery behavior.
- No explicit account recovery, password policy, age restrictions, or consent flow requirements are stated.
- No specific supported OS versions, device classes, localization languages, or accessibility targets are defined.
- No source-of-truth process is defined for rights metadata, league metadata, or content moderation/quality control.
- No explicit boundary is given for what “additional modules” and “connect their own interface to the user interface” means; this remains architecturally vague but was treated as non-critical for high-level business scope.

## 4. Summary of Finalized High-Level Requirement Interpretation

- Product is a mobile football app for **Android and iOS**.
- **Only end users** are in scope for this release.
- **Registration/login is mandatory at startup** before users access the app.
- Users can personalize the app via favorite clubs, preferred channels, and notifications.
- The app provides football news, team/player information, live ticker updates, and social sharing.
- Live stream functionality is limited to **deep links to external licensed providers**; no in-app video streaming is required.
- Rights compliance is enforced by showing stream links only where country rights are valid.
- The app should remain usable in poor connectivity, with **cached news, stories, and scores available offline**.
- Live data is retrieved from an **external API/server**.
- The platform should scale to **up to 100,000 simultaneous users** on peak match days.
- User data handling must comply with **GDPR**.
