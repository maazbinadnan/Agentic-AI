# Elicitation Report: Mobile Football App Requirements Audit

## Section 1: Original Requirements Text

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

## Section 2: Stakeholder Q&A History

1. **Q:** When you state that the app must be 'fully loaded and ready to use within a maximum of two seconds after starting,' what specific content or features must be available to the user within this time frame (e.g., news feed, live ticker, team info, or just the main interface)?
   **A:** Main interface

2. **Q:** Which specific features or content should remain accessible to users when the app is offline (e.g., previously loaded news, team info, live ticker, notifications, etc.)?
   **A:** Previously loaded team info and scores

3. **Q:** Are there any specific leagues or competitions that are excluded from the app’s coverage, or is the intention to include all national and international football leagues and competitions without exception?
   **A:** All first team competitions

4. **Q:** Is user registration mandatory to use the app, and what authentication methods are supported (e.g., email, social login, guest access)?
   **A:** Yes it is mandatory and uses email and social login of Gmail and Facebook

5. **Q:** How does the app determine whether a user is eligible to view a live stream in their country, and what happens if a user tries to access a stream for which rights are not fulfilled?
   **A:** It is fetched from an external API that will be setup and it throws an authorization error message

## Section 3: Documented Assumptions

- The app will serve up to 100,000 users simultaneously globally, not per region or server, unless otherwise specified.
- Data retention, storage location, and user data access/deletion rights will follow standard GDPR-compliant practices, as no further details were provided.
- The notification system will only function when the device is online, as offline notification delivery is not feasible.
- Social media sharing will use standard platform integrations (e.g., Android/iOS share sheets) unless otherwise specified.
- The term "uncomplicated" registration is interpreted as a streamlined process with minimal required fields.
