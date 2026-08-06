# 01 Elicitation Report

## 1. Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## 2. Stakeholder Q&A History

### Question 1
**Topic:** Authentication and access model  
**Question Asked:** Do users need to create an account to use the app, or should core features like browsing news, live scores, and team/player information be available without registration, with login required only for personalization features?  
**Stakeholder Answer:** yes they do

**Verified Interpretation:** User registration/login is mandatory to use the app, including access to core features.

### Question 2
**Topic:** Notification scope  
**Question Asked:** When you say users can receive notifications about news or results of their favorite teams, which notification model is required: only manual opt-in for favorite teams, or should there also be broadcast notifications for major football events regardless of favorites?  
**Stakeholder Answer:** manual opt in for favourite teams

**Verified Interpretation:** Notifications are limited to manual opt-in based on users’ selected favorite teams; no general broadcast notifications are in scope.

### Question 3
**Topic:** Live stream integration behavior  
**Question Asked:** What is the intended behavior of the live stream links: should the app only display eligible external links that open the licensed provider’s stream, or must users be able to watch the stream directly inside the app?  
**Stakeholder Answer:** eligible external links

**Verified Interpretation:** The app will only show eligible external stream links and redirect/open the licensed provider; in-app video streaming is out of scope.

## 3. Documented Assumptions

The following gaps were not escalated further because they were considered secondary to the high-level business scope, or reasonable assumptions could be made within the question limit:

1. **Performance target interpretation**  
   Assumption: The stated “fully loaded and ready to use within two seconds after starting” applies to app launch into an interactive home screen under normal supported device and network conditions, not under all edge conditions such as first install, degraded devices, or no network.

2. **Definition of “real time” live data**  
   Assumption: “Real time” means near-real-time updates from the external API with minimal delay acceptable for consumer sports apps, rather than guaranteed zero-latency event delivery.

3. **Offline behavior scope**  
   Assumption: Offline usability means users can still open the app, view previously cached content/settings, and continue limited navigation, while live scores, fresh news, and live stream links require connectivity.

4. **Coverage breadth for leagues and competitions**  
   Assumption: “All leagues and competitions, national and international” refers to the full set supported by the chosen data/content providers, not literally every football competition worldwide without provider limitations.

5. **Preferred sports channels feature**  
   Assumption: Users can select from supported football-related news/content sources already integrated by the platform; the app does not allow arbitrary third-party channel onboarding by end users.

6. **Rights compliance mechanism**  
   Assumption: Stream-link visibility will be controlled through provider rights metadata and user country/region checks, with only legally eligible external links displayed.

7. **Social sharing scope**  
   Assumption: Social sharing uses native mobile OS share capabilities for app-supported news and match-report content, rather than deep custom integrations with every social platform.

8. **Scalability target interpretation**  
   Assumption: Supporting up to 100,000 users simultaneously refers primarily to backend/system concurrency on peak match days and acceptable service continuity for core app functions.

9. **User roles**  
   Assumption: Only end-user/fan-facing functionality is in scope for this document; no separate admin, editor, or moderator portal is currently required.

10. **Personal data scope under GDPR**  
    Assumption: Personal data includes account information, user preferences/favorite clubs, notification settings, and app usage data needed for service delivery, all handled according to GDPR obligations.

11. **External API dependency**  
    Assumption: Match data, live ticker updates, and related dynamic content depend on one or more third-party external APIs, and the app does not generate original live match event data itself.

12. **UI customization meaning**  
    Assumption: “Additional modules that allow users to individually configure the app” refers to user personalization of content/modules/settings within predefined app capabilities, not unrestricted UI/plugin extensibility.

## 4. Summary of Critical Clarifications Resolved

- Authentication is mandatory for all users, including access to core app functionality.
- Notifications are manual opt-in and tied only to users’ favorite teams.
- Live stream support is limited to eligible external provider links; direct in-app streaming is not required.

## 5. Residual Risk Notes

The requirements still contain some broad qualitative language that may need later specification during downstream analysis or solution design, including:

- what exact device/network conditions are covered by the two-second launch target,
- what service levels define “without performance loss” for 100,000 concurrent users,
- what exact content/data providers supply league coverage, news, player data, and live APIs,
- what cached/offline content must remain available during loss of connectivity.

These were not raised as further stakeholder questions in order to respect the high-priority question limit and because they can be handled as assumptions or elaborated in subsequent specification stages.
