# Elicitation Report

## 1. Original Requirements Text

> We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## 2. Stakeholder Q&A History

### Q1. Access model / authentication requirement
- **Question:** What is the required access model for the app: can users browse news, scores, team/player information, and stream links without registering, or is login mandatory before using any core features?
- **Reason asked:** The requirements mention registration/login at app startup and personalization, but do not clearly define whether authentication is required for basic app usage or only for personalized features.
- **Stakeholder answer:** Login is necessary.
- **Confirmed implication:** Authentication is mandatory before users can access core app functionality.

### Q2. Live stream integration behavior
- **Question:** For the integrated live stream links, should the app only deep-link users to external providers such as DAZN or Sky Sport, or should streams ever be played directly inside the app?
- **Reason asked:** The requirements mention integration of live stream links and rights compliance, but do not define whether the app hosts in-app playback or only redirects to licensed provider platforms.
- **Stakeholder answer:** Deep-link.
- **Confirmed implication:** The app should not host or play streams directly; it should redirect users to authorized external providers.

### Q3. Offline functionality scope
- **Question:** When you say the app remains usable offline, which core functions must still work without internet access?
- **Reason asked:** Offline usability is a critical product behavior, but the requirements do not specify whether offline mode includes only previously cached content or broader functionality.
- **Stakeholder answer:** Previously cached content only.
- **Confirmed implication:** Offline mode is limited to viewing previously cached data/content; live data refresh and network-dependent features are unavailable offline.

### Q4. Notification trigger scope
- **Question:** What exact events should trigger push notifications when users activate notifications for favorite teams?
- **Reason asked:** The requirements mention a notification system for current events, news, and results, but do not specify the high-level business events that must generate notifications.
- **Stakeholder answer:** Live score updates and news.
- **Confirmed implication:** Push notifications are required for live score updates and news related to favorite teams.

## 3. Documented Assumptions

The following non-critical or secondary gaps were not escalated further and are documented as working assumptions for downstream analysis and design:

1. **Personalization scope**
   - Users can follow favorite clubs/teams and preferred sports channels.
   - No additional personalization dimensions were explicitly confirmed.

2. **Login method**
   - The document requires login but does not specify authentication methods.
   - Assumption: a standard email/password login flow is sufficient unless another identity provider or social login is later mandated.

3. **Registration timing**
   - Registration and login are described as available at startup.
   - Assumption: onboarding presents authentication immediately on first launch, and successful login is required before reaching the main app experience.

4. **Definition of “real time” live ticker behavior**
   - The exact update interval is not specified.
   - Assumption: updates should appear with minimal practical delay supported by the external live-data API and mobile network conditions.

5. **Coverage breadth for leagues and competitions**
   - “All leagues and competitions, national and international” is stated broadly.
   - Assumption: the system intends broad coverage based on whatever competitions are available from the chosen external data/news/content providers, subject to licensing and provider availability.

6. **Country-based transmission rights enforcement**
   - The document requires streams to be shown only where rights are fulfilled, but does not specify the enforcement mechanism.
   - Assumption: stream-link visibility is controlled using location/country eligibility information from the content provider, backend rules, or user region detection.

7. **Sharing scope**
   - Users can share news and game reports via social media.
   - Assumption: sharing is limited to outbound native share actions and does not require in-app social posting or social account integration.

8. **Limited-network behavior**
   - The app must function reliably under poor connectivity, but degradation rules are not defined.
   - Assumption: the app should degrade gracefully by showing cached content, retrying failed requests, and informing users when live/network-dependent functions are unavailable.

9. **Scalability statement interpretation**
   - The requirement states support for up to 100,000 simultaneous users without performance loss.
   - Assumption: this is primarily a backend/service scalability target for peak match-day usage rather than a device-side concurrency feature.

10. **Performance requirement interpretation**
    - The app should be fully loaded and ready to use within two seconds after starting.
    - Assumption: this target applies to typical supported devices under normal network conditions, with essential UI available quickly even if some dynamic content continues loading afterward.

11. **GDPR scope**
    - GDPR compliance is required for personal data processing.
    - Assumption: this includes lawful basis/consent where needed, data minimization, privacy notice availability, and user data handling processes consistent with GDPR obligations.

12. **External dependencies**
    - Live data comes from an external API and stream access depends on third-party providers.
    - Assumption: availability, freshness, and completeness of certain app features depend on third-party service uptime and licensing coverage.

## 4. Summary of Critical Clarifications Resolved

- Login is mandatory to use the app.
- Live stream integration uses deep-links only; no in-app playback is required.
- Offline usability is limited to previously cached content.
- Push notifications must cover live score updates and news for favorite teams.

## 5. Residual Risks / Open Areas to Monitor

These items were not raised as critical stakeholder questions due to prioritization limits, but they remain important for later specification stages:

- Exact supported authentication methods and account recovery flow.
- Supported countries/regions and localization expectations.
- Detailed definition of favorite team setup and limits.
- Cache retention policy for offline content.
- Exact load/performance measurement conditions for the 2-second startup target.
- Detailed service-level expectations for the external live-data API.
- Compliance details for GDPR operations such as data deletion/export requests.
