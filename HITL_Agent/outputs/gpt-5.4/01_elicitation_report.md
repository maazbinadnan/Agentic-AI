# 01 Elicitation Report

## 1. Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## 2. Stakeholder Q&A History

### Q1
**Question:** Does the app require users to register/login before they can use core features, or should browsing news, scores, and team/player information also be available to anonymous users with login only needed for personalization features?

**Reason Asked:** The requirements mention uncomplicated registration/login at startup, but do not define whether authentication is mandatory for core access. This affects scope, onboarding, permissions, and data handling.

**Stakeholder Answer:** yes

**Assessment:** Answer was ambiguous and did not fully resolve the decision.

### Q2
**Question:** Should registration/login be mandatory before using the app, with all users required to sign in at startup?

**Reason Asked:** The previous answer was ambiguous ('yes') and did not clearly resolve whether anonymous browsing is allowed or whether authentication is compulsory.

**Stakeholder Answer:** yes it is mandatory

**Verified Outcome:** Registration/login is mandatory for all users before app use.

### Q3
**Question:** What is the business model for live stream access: should the app only deep-link users to third-party providers like DAZN/Sky Sport, or must users be able to watch streams directly inside the app?

**Reason Asked:** The requirements mention integration of live stream links and transmission-rights compliance, but do not clearly define whether streaming occurs in-app or only via external providers. This is a high-impact scope and compliance decision.

**Stakeholder Answer:** deep link

**Verified Outcome:** The app will provide deep links to external streaming providers rather than in-app video playback.

### Q4
**Question:** Which users should receive push notifications: all signed-in users by default, or only users who explicitly opt in and select favorite teams/channels/events for alerts?

**Reason Asked:** The requirements mention an activated notification function and favorite-team personalization, but do not specify the notification eligibility rule. This affects consent, onboarding, user experience, and GDPR compliance.

**Stakeholder Answer:** only users who opt in

**Verified Outcome:** Push notifications are restricted to users who explicitly opt in.

## 3. Documented Assumptions

The following lower-priority gaps were not escalated further because of the 3–5 question limit and the instruction to focus only on critical high-level scope items. Reasonable domain assumptions have been documented for downstream analysis.

1. **Monetization model not specified**  
   Assumption: The initial release has no direct in-app subscription or payment processing requirement; third-party streaming subscriptions remain fully managed by external providers.

2. **Definition of 'fully loaded within two seconds' not operationally specified**  
   Assumption: The two-second target applies to app launch into a usable home screen under normal supported device and network conditions, not worst-case first-install cold start on low-end devices.

3. **'Real time' live ticker update frequency not quantified**  
   Assumption: Live data should be refreshed frequently enough to appear near-real-time to users, subject to provider API latency and mobile network conditions.

4. **Coverage breadth of 'all leagues and competitions' not contractually enumerated**  
   Assumption: Actual coverage depends on licensed or available third-party data sources and may vary by region, competition, and provider availability.

5. **Offline usability scope not explicitly bounded**  
   Assumption: Offline mode supports access to previously cached content, persisted preferences, and graceful degraded browsing, but cannot provide fresh live scores, breaking news, or new stream links without connectivity.

6. **User roles not described beyond end users**  
   Assumption: Only one external business user role exists in scope for the mobile app: registered end user/fan. Administrative, editorial, moderation, and support tooling are out of scope for this requirements set unless covered elsewhere.

7. **Sports channel selection behavior not specified**  
   Assumption: Users can choose preferred channels/topics as personalization filters for content ranking and notification relevance, not as direct broadcast entitlements.

8. **Social sharing destinations not listed**  
   Assumption: Sharing will use the native mobile OS share sheet to post links or summaries to installed social/media apps.

9. **Country-based rights enforcement mechanism not specified**  
   Assumption: Stream-link visibility is controlled using user-country or device-location/market logic plus provider availability metadata supplied by integration services.

10. **Concurrent user target lacks service-level detail**  
    Assumption: The 100,000 simultaneous user requirement is a peak non-functional capacity target for the overall platform during match days, with no detailed per-feature SLA currently defined.

11. **External API ownership and commercial dependency not specified**  
    Assumption: News, team/player data, standings, and live ticker data depend on one or more third-party content/data providers outside the mobile app team's direct control.

12. **Account registration method not specified**  
    Assumption: Email/password is the default mandatory sign-up/login mechanism unless federated identity or phone-based authentication is later introduced.

13. **GDPR controls not elaborated**  
    Assumption: Standard GDPR controls are required, including consent capture where needed, privacy policy access, lawful basis documentation, user data access/deletion support, and secure personal-data handling.

14. **Testing/support process not quantified**  
    Assumption: The project will include functional, performance, compatibility, and regression testing before release, with post-release monitoring and issue triage as standard operational practice.

15. **'Additional modules' and 'connect their own interface to the user interface' are vague**  
    Assumption: This refers to configurable app sections/widgets/settings exposed through the existing UI, not to user-built plugins, custom code, or third-party extension frameworks.

## 4. Consolidated High-Level Gap Analysis Summary

Critical ambiguities resolved during elicitation:
- Authentication is mandatory before app use.
- Streaming is out-of-app via deep links to rights-holding providers.
- Notifications are opt-in only.

High-level areas still broad but manageable via assumption:
- Exact performance measurement criteria for the two-second startup target.
- Precise live update cadence and freshness SLA.
- Enumerated competition coverage and country availability matrix.
- Detailed offline feature boundaries.
- Identity options, consent flows, and retention details under GDPR.

## 5. Finalized Elicitation Outcome

Based on the original requirements and stakeholder clarifications, the current interpreted scope is:
- A cross-platform mobile football app for Android and iOS.
- Mandatory user registration/login at startup for all users.
- Personalized football news, favorite teams, preferred channels, team/player information, and live scores.
- Live ticker driven by external APIs for near-real-time match updates.
- Stream discovery through deep links to external providers such as DAZN or Sky Sport, gated by rights availability in the user’s country.
- Push notifications only for users who explicitly opt in.
- Social sharing support for news and match reports.
- Offline degraded usability through cached/persisted content and preferences.
- Peak scalability target of 100,000 concurrent users.
- GDPR-compliant personal data processing.
