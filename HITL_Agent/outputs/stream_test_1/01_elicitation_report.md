# Elicitation Report: LiveFootball Mobile App

## Section 1: Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

---

## Section 2: Stakeholder Q&A History

1. **Q:** Will users need to authenticate with external live stream providers (such as DAZN or Sky Sport) within the app to access live streams, or will the app itself handle any form of subscription or payment for these services?  
   **A:** If the user is logged into our service they can see links to the live streams and it will take them to the respective app.

2. **Q:** What is the maximum acceptable delay (in seconds) for live ticker updates to be considered 'real time' in the app?  
   **A:** 10 seconds

3. **Q:** Is user registration required to access any app features, or can users use the app in a guest mode without registering?  
   **A:** Registration is required.

---

## Section 3: Documented Assumptions

- “Limited network coverage” is assumed to mean the app will provide cached or last-synced data and basic navigation when offline, with live features resuming upon reconnection.
- “Extensive coverage of all leagues and competitions” is assumed to include all major national and international football leagues, but not necessarily every minor or amateur league.
- “Personalization” is assumed to be limited to following favorite teams, selecting preferred channels, and notification preferences, as described.
- “Uncomplicated” registration and login are assumed to mean standard mobile registration flows (email, password, possibly social login).
- “Up to 100,000 users simultaneously” is assumed to refer to concurrent active sessions, not total registered users.
