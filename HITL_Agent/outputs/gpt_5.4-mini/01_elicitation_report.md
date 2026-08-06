# Elicitation Report

## 1. Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## 2. Stakeholder Q&A History

### Q1. Offline usability scope
- **Question:** What specific functionality must remain available when the app is offline: previously cached news/team data only, or also any live ticker/results features once connectivity is lost?
- **Why asked:** The requirement states the app remains usable offline, but does not define the minimum offline feature set.
- **Stakeholder answer:** Previously cached news and team data only.
- **Verified outcome:** Offline mode is limited to access to cached news and team information; live ticker and real-time results are not required offline.

### Q2. Live stream integration scope
- **Question:** Are the integrated live stream links only meant to deep-link users out to licensed providers like DAZN or Sky Sport, or must users be able to watch streams directly inside the app?
- **Why asked:** The requirement is ambiguous on whether the app provides playback or only links to external rights holders.
- **Stakeholder answer:** Deep links only.
- **Verified outcome:** The app does not host or embed live stream playback; it only provides rights-aware external links to licensed providers.

### Q3. Registration/login requirement
- **Question:** Is user registration/login mandatory to use the app, or should users be able to browse core content without signing in and only log in for personalization features like favorites and notifications?
- **Why asked:** The requirement mentions registration and login at startup but does not specify whether authentication is mandatory.
- **Stakeholder answer:** Yes it is.
- **Verified outcome:** Registration/login is treated as mandatory before using the app.

## 3. Documented Assumptions

The following non-critical or secondary gaps were not escalated further to stay within the stakeholder question limit. Reasonable domain assumptions are documented here for downstream analysis and validation.

### Functional assumptions
- "Current football news" is assumed to be filtered by a user’s selected favorite teams and chosen sports channels after login.
- "Extensive coverage of all leagues and competitions, both national and international" is assumed to mean broad catalog coverage where supported by the chosen external data/content providers, not a contractual guarantee of every competition worldwide at launch.
- Detailed team and player information is assumed to be read-only informational content sourced from external APIs/content systems.
- The notification system is assumed to support push notifications for selected events such as news updates and match result updates related to followed teams.
- Social media sharing is assumed to use native mobile share capabilities to external social platforms rather than custom in-app social features.
- "Additional modules" and the phrase about users being able to "connect their own interface to the user interface" are assumed to mean configurable app sections/preferences rather than user-developed plug-ins or third-party UI extensions.

### Performance and availability assumptions
- The stated startup performance requirement of "fully loaded and ready to use within a maximum of two seconds after starting" is assumed to apply under normal supported device and network conditions, not under all degraded-network scenarios.
- "Real time" live ticker is assumed to mean near-real-time updates subject to latency of the external live-data API provider and network conditions.
- The app serving up to 100,000 simultaneous users without performance loss is assumed to be a backend/platform scalability target rather than a guarantee that every client-side experience is identical under all peak conditions.
- Reliable operation under limited network coverage is assumed to include graceful degradation, retry behavior, and continued access to previously cached news/team data, but not continued delivery of fresh live events while offline.

### Compliance and security assumptions
- GDPR compliance is assumed to include lawful basis/consent handling, privacy notice availability, user data protection in transit and at rest where applicable, and mechanisms to support data subject rights.
- Rights compliance for live streams is assumed to be enforced through region/country-based entitlement checks before showing external provider links.
- Because registration/login is mandatory, personal account data management, authentication, and consent/privacy flows are assumed to be required from first launch.

### Outstanding ambiguities for future refinement
These were identified during audit but not raised due to the high-level question limit:
- Supported login methods are unspecified (email/password, social login, SSO, etc.).
- Supported countries/markets are unspecified, which affects rights handling, language, privacy notices, and content availability.
- The exact definition of "without performance loss" for 100,000 concurrent users is unspecified.
- No retention policy, deletion workflow, or age restrictions are specified for registered users.
- No explicit source-of-truth/content-provider list is given for news, live scores, team/player data, and stream rights metadata.
- No explicit accessibility, localization, or language requirements are defined.

## 4. Summary of Finalized High-Level Scope
- Mobile app for **Android and iOS**.
- App must start and become ready within **2 seconds** under assumed normal conditions.
- **Mandatory registration/login** is required before app use.
- Core user features include football news, favorite teams, preferred sports channels, live ticker, team/player information, notifications, and social sharing.
- **Offline support** is limited to **previously cached news and team data**.
- Live ticker/live results depend on connectivity and external API availability.
- Live stream functionality is **deep-link only** to licensed providers; no in-app playback.
- Rights compliance is enforced by showing links only where relevant rights exist in the user’s country.
- Backend/platform should support up to **100,000 concurrent users** on peak match days.
- Personal data processing must comply with **GDPR**.
