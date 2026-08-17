# 01_elicitation_report

## 1. Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## 2. Stakeholder Q&A History

### Q1. Authentication scope
- **Question:** Which user actions or features require registration/login, and is anonymous access allowed for browsing news, live scores, and team/player information?
- **Why asked:** The requirements mention uncomplicated registration/login at app startup, but it was unclear whether authentication is mandatory for all users or only for personalization features.
- **Stakeholder answer:** All features require login.

### Q2. Live stream integration scope
- **Question:** What is the business scope of the live stream integration: should the app only deep-link users to external providers like DAZN/Sky Sport, or should it also support in-app playback where rights permit?
- **Why asked:** The requirements mention integration of live stream links and rights compliance, but do not define whether streaming is only a redirect/linking feature or an in-app viewing capability.
- **Stakeholder answer:** Deep links to other streams.

### Q3. Offline functionality scope
- **Question:** When the app is offline or has limited connectivity, which functions must still work: only previously loaded content, or also actions like viewing cached news/team data, favorite selections, and queued notifications?
- **Why asked:** The requirements state the app remains usable offline, but do not define the minimum offline feature set.
- **Stakeholder answer:** Cached news only.

### Q4. Notification trigger scope
- **Question:** What exact event types should trigger notifications for favorite teams—for example match start, goals, half-time, full-time, breaking news, transfer updates, or all available event types?
- **Why asked:** The requirements say users receive notifications about news or results of favorite teams, but the actual notification scope was undefined.
- **Stakeholder answer:** Goals.

## 3. Documented Assumptions

The following assumptions were made for unresolved but non-critical or lower-priority gaps, in line with the question limit and high-level elicitation scope:

### 3.1 Performance and availability assumptions
- The requirement that the app be fully loaded within **two seconds after starting** is assumed to apply under normal supported device and network conditions, not under extreme low-end device scenarios or complete network outage.
- The claim of **real-time** live results is assumed to mean near-real-time delivery dependent on the external live data API, with small provider/network latency tolerated.
- The requirement to support **100,000 simultaneous users without performance loss** is assumed to refer primarily to backend/service capacity and API consumption expectations rather than guaranteed identical client-side response times on all devices.

### 3.2 Coverage and content assumptions
- **Extensive coverage of all leagues and competitions** is assumed to mean the app should display whatever competitions are available from the contracted content/data providers; absolute universal coverage is not guaranteed unless provider data supports it.
- **Detailed team and player information** is assumed to include standard profile/statistical information typically available from the external football data provider.
- Users can choose **favorite teams** and **preferred sports channels** as part of profile personalization after login.

### 3.3 Rights and geo-availability assumptions
- Live stream items are assumed to be displayed only as **deep links** to third-party broadcasters/providers and not streamed natively within the app.
- Rights compliance is assumed to be enforced through country-based availability logic supplied by stream metadata, provider rules, or geo-restriction handling.

### 3.4 Offline and degraded-network assumptions
- Offline usability is limited to **viewing cached news only**.
- Live ticker updates, live scores, stream links validation, and notifications requiring fresh server data are assumed not to function while the device is offline.
- Cached data freshness duration and cache invalidation rules are not specified and are assumed to be determined later during design.

### 3.5 Authentication and user account assumptions
- **Login is mandatory for all features**; anonymous browsing is not supported.
- Registration and login are assumed to be available from app startup as the primary entry path.
- The authentication method (email/password, social login, OTP, etc.) is not specified and is assumed to be decided later.

### 3.6 Notification assumptions
- Notifications for favorite teams are assumed to be limited to **goal events only**.
- Users are assumed to have the ability to enable or disable notifications globally, and possibly at favorite-team level, although the exact settings granularity is not specified.

### 3.7 Social sharing and compliance assumptions
- Social media sharing is assumed to use standard mobile OS sharing capabilities to share links or summaries of news and game reports.
- GDPR compliance is assumed to require appropriate consent, privacy notice, lawful processing, and user data handling controls, though exact compliance workflows are not specified in the source document.

### 3.8 Architectural wording normalization
- Phrases such as users being able to **connect their own interface to the user interface** are treated as imprecise wording and assumed to mean users can configure or personalize modules/widgets within the fixed app interface, not that users can build custom external interfaces.
- The statement that modules and UI remain consistent even with external server updates is assumed to mean server-side content/data changes should not alter the app’s deployed client structure or break module contracts.

## 4. Summary of Key Clarified Business Rules

- The app is for **Android and iOS**.
- The app target is to be **ready to use within 2 seconds** after startup.
- **Login is required for all features**.
- Live stream integration is **deep-link only** to external providers.
- Offline functionality is limited to **cached news only**.
- Notifications for favorite teams are triggered by **goals only**.
- The app must support up to **100,000 simultaneous users** on peak match days.
- Personal data must be processed in compliance with **GDPR**.
