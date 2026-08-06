# 01 Elicitation Report — LiveFootball Mobile App

## Section 1: Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

---

## Section 2: Stakeholder Q&A History

| # | Topic | Clarifying Question | Verified Stakeholder Answer | Requirement Impact |
|---|---|---|---|---|
| 1 | Live streaming scope and rights compliance | For live stream links, should LiveFootball only deep-link users to authorized third-party providers, e.g., DAZN/Sky, rather than hosting or embedding the video stream inside the app? | Deep link. | The app will not host, retransmit, or embed live video streams. It will provide authorized deep links to third-party provider platforms/apps/websites where rights conditions are met. |
| 2 | Authentication and access model | Which core app features must be available to users without registration/login, if any? | None. | Registration/login is mandatory before accessing app features. The user journey should include authentication at app startup before news, live ticker, team/player info, personalization, notifications, sharing, or stream links are usable. |
| 3 | Competition coverage for initial release | For the initial release, what football coverage scope is required: truly all national/international leagues, or a prioritized set of leagues and competitions? | European top leagues only. | The initial release scope is narrowed from “all leagues and competitions” to top European leagues/competitions. “All national and international competitions” should be treated as a future expansion objective, not MVP scope. |
| 4 | Offline mode scope | When the app is offline, should users only be able to view previously loaded/cached content, or must they be able to perform new actions such as changing favorites or queuing notification preferences for later sync? | Only previous loaded/cached content. | Offline usability is read-only and limited to content already fetched/cached on the device. New actions requiring server persistence, such as changing favorites or notification preferences, are not required while offline. |

---

## Section 3: Documented Assumptions

The following assumptions resolve lower-priority ambiguities so downstream requirements engineering can proceed without further stakeholder interruption.

### 3.1 Product Scope and Users

1. **Target users:** The primary users are football fans using Android or iOS smartphones.
2. **User roles:** Only one end-user role is in scope for the mobile app. Administrative/editorial roles for managing content, rights, providers, or support are assumed to be outside the mobile app scope unless covered by a separate back-office system.
3. **Business model:** No paid subscription, in-app purchases, or advertising requirements are stated. The initial requirements are assumed to describe a free-to-use app after mandatory registration/login. Any monetization model should be handled as a future requirement if needed.
4. **Localization:** Because the app covers European football, multi-country usage is expected, but no language list is specified. Initial language support is assumed to be defined separately; English can be treated as the baseline working language unless the product owner states otherwise.

### 3.2 Authentication and Personalization

1. **Mandatory account:** All features require authenticated access based on stakeholder clarification.
2. **Simple registration/login:** “Uncomplicated” registration is assumed to mean a minimal flow using email/password and/or platform-supported sign-in options, subject to later UX/security definition.
3. **Personalized favorites:** Users can follow favorite clubs; favorite players, leagues, or channels are not explicitly confirmed as followable entities except where channels are selected as preferred sports channels.
4. **User profile data:** Stored personal data is assumed to be limited to what is necessary for account access, favorites, channel preferences, notification settings, and GDPR compliance.

### 3.3 News and Sports Channels

1. **News source model:** The app aggregates or displays football news related to favorite teams and preferred sports channels. Exact content providers, editorial workflow, and licensing terms remain to be specified in supplier/content agreements.
2. **News filtering:** News is assumed to be filterable by favorite team and preferred channel.
3. **Sharing:** Social sharing is assumed to use native OS share-sheet capabilities and share links/previews to news or match reports, not full copyrighted article reproduction.

### 3.4 Live Ticker and Match Data

1. **Near-real-time interpretation:** “Real time” live results are assumed to mean near-real-time updates suitable for consumer sports apps, dependent on external data provider latency. Exact update intervals and service-level agreements should be defined with the data supplier.
2. **External API dependency:** Live match, team, player, and competition data are retrieved from one or more external APIs. The app should handle provider outages gracefully, but detailed failover architecture is not specified in the raw requirements.
3. **Displayed live events:** The live ticker is assumed to include core match data such as score, time, match status, goals, cards, substitutions, and key events where provided by the external API.
4. **Data completeness:** Team and player information availability depends on licensed data coverage for the confirmed initial scope of top European leagues.

### 3.5 Competition Coverage

1. **MVP coverage:** Initial launch coverage is top European leagues/competitions only, per stakeholder clarification.
2. **Future expansion:** Broader national and international competition coverage is a roadmap item and should not be treated as a release-blocking requirement for MVP.
3. **Definition still needed for delivery planning:** The exact list of “European top leagues” should be agreed during backlog refinement. Reasonable candidates include Premier League, La Liga, Bundesliga, Serie A, Ligue 1, UEFA Champions League, UEFA Europa League, and UEFA Europa Conference League.

### 3.6 Live Stream Deep Links and Rights

1. **Deep-link only:** The app will direct users to authorized third-party providers rather than host or embed video streams.
2. **Rights gating:** Stream links are displayed only when rights are fulfilled in the user’s country. Country determination is assumed to use account region, device locale, IP/geolocation, or provider metadata subject to legal review.
3. **Provider dependency:** Availability of stream links depends on provider integrations, schedules, rights metadata, and whether the broadcast has begun.
4. **No entitlement management assumed:** The app is not assumed to validate whether the user has an active DAZN/Sky/etc. subscription; entitlement is expected to be handled by the third-party provider after deep-link handoff.

### 3.7 Notifications

1. **Opt-in required:** Notifications are only sent after the user activates notification functionality and grants OS-level permission.
2. **Notification topics:** Notifications are assumed to cover favorite-team news, live results, and important match events. Exact event categories and user controls should be refined later.
3. **Offline impact:** Push notifications require network connectivity and platform push services; offline users may not receive notifications until connectivity is restored.

### 3.8 Offline and Limited Connectivity Behaviour

1. **Offline read-only mode:** Offline mode is limited to previously loaded/cached content, per stakeholder clarification.
2. **No offline mutation queue:** Offline changes to favorites, notification settings, account details, or social sharing are not required for MVP.
3. **Staleness indication:** Cached content should be clearly distinguishable from live/current data where relevant, especially for live scores and match status.
4. **Live ticker offline:** Live updates cannot be guaranteed offline; the last known state can be shown with an indication that the app is offline or data may be outdated.

### 3.9 Performance, Scalability, and Reliability

1. **Startup performance:** The app must be fully loaded and ready to use within a maximum of two seconds after starting. This is assumed to apply under normal device/network conditions and excludes first-time install/setup, OS cold-start variability, and external provider outages unless later specified.
2. **Concurrent usage target:** The backend/external-service architecture should support up to 100,000 simultaneous users on high-traffic match days without material performance degradation. Exact response-time, throughput, and uptime targets should be converted into measurable non-functional requirements later.
3. **Smooth operation:** “Quickly and smoothly” is assumed to mean responsive navigation, acceptable screen-load times, and non-blocking live updates, but detailed UI performance metrics remain undefined.
4. **External dependency risk:** Performance may depend on third-party data APIs, content providers, push services, and deep-link providers; contractual SLAs are needed to guarantee end-to-end performance.

### 3.10 GDPR, Privacy, and Security

1. **GDPR compliance:** The app must support lawful processing, data minimization, privacy notice, consent where required, access/erasure requests, retention controls, and secure handling of personal data.
2. **Security baseline:** Although “secure” is not explicitly defined, authentication, data transmission, and personal data storage are assumed to follow standard mobile security practices, including encrypted transport and secure credential handling.
3. **Analytics and feedback:** Continuous evaluation of user feedback and app reviews is in scope. Any behavioural analytics or crash reporting involving personal data must be disclosed and handled under GDPR.

### 3.11 Testing and Support

1. **Pre-release testing:** Functional, usability, performance, compatibility, security/privacy, and network-condition testing are assumed to be required before release.
2. **Supported platforms:** Android and iOS are in scope; supported OS versions and device classes are not specified and should be defined in a technical specification.
3. **Support process:** “Thorough testing and support process” implies defect detection, triage, and resolution before release, but support SLAs and operational ownership remain unspecified.

---

## Section 4: Key Audit Findings and Residual Risks

1. **Original scope was overbroad:** “All leagues and competitions” was clarified to top European leagues only for initial release, reducing content/data complexity.
2. **Live stream legal risk was clarified:** The app will deep-link only, substantially reducing broadcasting-rights and technical streaming obligations.
3. **Access model is strict:** No unauthenticated feature access is required, which simplifies personalization but makes registration/login a critical dependency for first-use experience.
4. **Offline behaviour is limited:** Offline mode is read-only and cache-based, reducing sync complexity but requiring clear user messaging about stale live data.
5. **Measurable NFRs remain partially undefined:** The two-second startup target and 100,000 concurrent-user target are stated, but detailed measurement conditions, uptime targets, API latency, and degradation thresholds should be refined during non-functional requirements specification.
6. **External supplier dependencies are material:** News, live match data, team/player data, rights metadata, deep-link availability, and push delivery depend on third parties and should be governed through provider contracts and SLAs.
7. **GDPR is a stated requirement but needs operationalization:** Privacy workflows, consent model, data retention, deletion/export rights, and analytics/crash-reporting disclosures need detailed design.

---

## Section 5: Clarified High-Level Requirement Baseline

For downstream requirements engineering, the LiveFootball MVP should be treated as follows:

- A mandatory-login Android/iOS football app for authenticated users.
- Initial content coverage limited to top European leagues and competitions.
- Core features include personalized team news, preferred sports channel selection, live ticker/live results, team and player information, notifications, and social sharing.
- Live stream functionality consists of rights-compliant third-party deep links only; no video hosting or embedded streaming is included.
- Offline mode allows viewing previously loaded/cached content only.
- The app should target a maximum two-second ready-to-use startup time under defined normal conditions and support up to 100,000 concurrent users on match days.
- Personal data processing must comply with GDPR.
