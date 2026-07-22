# LiveFootball App Stakeholder Report

---

## Executive Summary

This report compiles the artefacts produced during the requirements analysis and design phase for the LiveFootball mobile app. The app aims to provide football fans with a fast, reliable, and comprehensive platform for news, live results, personalized content, and live streaming, with robust offline and data protection features. The report includes the original user research, detailed user stories and acceptance criteria, HTML mockups for key screens and interactions, and a traceability matrix mapping user stories to their corresponding mockups. This document is intended for stakeholder review and ensures traceability and clarity across all deliverables.

---

## Original User Research

---

We are currently developing a mobile football app that will be available for Android and iOS devices. It is particularly important to us that the app runs quickly and smoothly so that it is fully loaded and ready to use within a maximum of two seconds after starting. With our app, we want to offer football fans a central platform where they can stay comprehensively informed at all times. To achieve this, users can display current football news of their favorite teams and also select preferred sports channels individually. In addition to the news, users can follow the results of their favorite teams live via a live ticker. Our app will offer extensive coverage of all leagues and competitions, both national and international. Detailed team and player information will also be available at any time. Another highlight is the integration of live stream links, for example, from providers such as DAZN or Sky Sport. These are available directly in the app as soon as the live broadcast has begun. Of course, it is ensured that compliance with transmission rights is maintained. Live streams will only be displayed when the respective rights are fulfilled in the country. The LiveFootball app should also give users the option to retrieve the live results of their favorite teams in real time. To implement this function, the app includes an integrated live ticker module that enables the retrieval and display of live data in real time. The user interface is designed so that users can access the information in the app directly. The user interface is a key component of the app and connects various modules that are displayed together and managed via the interface. The live ticker module communicates directly via the interface with the user interface to display and continuously update current match data. The live data is retrieved via an API from an external server. The server is located outside the app and provides the data dynamically so that the live ticker module can access it flexibly. In addition to the live ticker module, the app also offers additional modules that allow users to individually configure the app and connect their own interface to the user interface. Furthermore, the app is linked to a notification system that provides users with information about current events as soon as the notification function is activated. All modules and the user interface are fixed components of the app and remain consistent even with external server updates. Registration and login are designed to be uncomplicated and can be completed directly at app startup. Users have the option to personalize their experience by following favorite clubs and receiving notifications about news or results of their favorite teams. In addition, users can share news and game reports via social media directly from the app. We are aware that many mobile apps have to operate under difficult conditions. Therefore, the app is developed so that it functions reliably even with limited network coverage. The app remains usable offline, even if it temporarily loses connection. On match days with a particularly high number of accesses, our app is designed so that up to 100,000 users can be served simultaneously without performance loss. To prevent technical problems, the app goes through a thorough testing and support process before release to detect and resolve any malfunctions early. In addition, user feedback and app reviews are continuously evaluated to improve functionality. Data protection is our highest priority. All personal data of users are processed in compliance with the GDPR.

---

## User Stories & Acceptance Criteria

---

### 1. App Performance

**User Story:**  
As a football fan, I want the app to load and be ready to use within two seconds so that I can quickly access football information without delay.

**Acceptance Criteria:**  
- **Given** the app is installed on an Android or iOS device  
- **When** the user launches the app  
- **Then** the app is fully loaded and ready to use within two seconds

---

### 2. Personalized News

**User Story:**  
As a football fan, I want to display current football news of my favorite teams so that I can stay informed about the teams I care about.

**Acceptance Criteria:**  
- **Given** the user has selected favorite teams  
- **When** the user opens the news section  
- **Then** news related to the selected favorite teams is displayed

---

### 3. Preferred Sports Channels

**User Story:**  
As a football fan, I want to select preferred sports channels so that I can view news and updates from sources I trust.

**Acceptance Criteria:**  
- **Given** the user is in the channel selection settings  
- **When** the user selects preferred sports channels  
- **Then** news from the selected channels is displayed in the app

---

### 4. Live Ticker for Favorite Teams

**User Story:**  
As a football fan, I want to follow the live results of my favorite teams via a live ticker so that I can stay updated in real time during matches.

**Acceptance Criteria:**  
- **Given** the user has selected favorite teams  
- **When** a match involving a favorite team is ongoing  
- **Then** the live ticker displays real-time match data for the favorite team

---

### 5. Comprehensive Coverage

**User Story:**  
As a football fan, I want access to coverage of all leagues and competitions, both national and international, so that I can follow football events worldwide.

**Acceptance Criteria:**  
- **Given** the user is browsing leagues and competitions  
- **When** the user selects a league or competition  
- **Then** information about the selected league or competition is displayed

---

### 6. Detailed Team and Player Information

**User Story:**  
As a football fan, I want to view detailed information about teams and players so that I can learn more about them.

**Acceptance Criteria:**  
- **Given** the user selects a team or player  
- **When** the user opens the team or player profile  
- **Then** detailed information about the team or player is displayed

---

### 7. Live Stream Links

**User Story:**  
As a football fan, I want to access live stream links for matches so that I can watch live broadcasts directly from the app when available.

**Acceptance Criteria:**  
- **Given** a live broadcast is available and transmission rights are fulfilled in the user's country  
- **When** the user opens the match page during the live broadcast  
- **Then** live stream links from providers (e.g., DAZN, Sky Sport) are displayed

---

### 8. Real-Time Live Results

**User Story:**  
As a football fan, I want to retrieve live results of my favorite teams in real time so that I can stay updated instantly.

**Acceptance Criteria:**  
- **Given** the user has selected favorite teams  
- **When** a match is ongoing  
- **Then** live results are updated in real time via the live ticker module

---

### 9. User Interface Accessibility

**User Story:**  
As a football fan, I want to access all information directly through the user interface so that I can easily navigate and find what I need.

**Acceptance Criteria:**  
- **Given** the app is running  
- **When** the user navigates through the interface  
- **Then** all modules (news, live ticker, team info, etc.) are accessible and displayed together

---

### 10. App Personalization

**User Story:**  
As a football fan, I want to configure the app and connect my own interface to the user interface so that I can personalize my experience.

**Acceptance Criteria:**  
- **Given** the user is in the personalization settings  
- **When** the user configures the app or connects their interface  
- **Then** the personalized settings are applied and reflected in the user interface

---

### 11. Notifications

**User Story:**  
As a football fan, I want to receive notifications about current events, news, and results of my favorite teams so that I am always informed.

**Acceptance Criteria:**  
- **Given** the user has activated notifications  
- **When** a relevant event occurs (news, match result, etc.)  
- **Then** the user receives a notification about the event

---

### 12. Registration and Login

**User Story:**  
As a new user, I want to register and log in easily at app startup so that I can quickly begin using the app.

**Acceptance Criteria:**  
- **Given** the app is launched for the first time  
- **When** the user completes registration or login  
- **Then** the user is granted access to the app

---

### 13. Social Sharing

**User Story:**  
As a football fan, I want to share news and game reports via social media directly from the app so that I can inform others.

**Acceptance Criteria:**  
- **Given** the user is viewing a news article or game report  
- **When** the user selects the share option  
- **Then** the article or report can be shared via social media platforms

---

### 14. Offline Functionality

**User Story:**  
As a football fan, I want the app to remain usable offline so that I can access information even with limited network coverage.

**Acceptance Criteria:**  
- **Given** the device has limited or no network coverage  
- **When** the user opens the app  
- **Then** previously loaded information is accessible and the app remains usable

---

### 15. Scalability

**User Story:**  
As a football fan, I want the app to function reliably even during high traffic (e.g., match days) so that performance is not affected.

**Acceptance Criteria:**  
- **Given** up to 100,000 users are accessing the app simultaneously  
- **When** the app is in use during peak times  
- **Then** the app performs without loss of speed or reliability

---

### 16. Testing and Support

**User Story:**  
As a football fan, I want the app to be thoroughly tested and supported so that technical problems are detected and resolved early.

**Acceptance Criteria:**  
- **Given** the app is in pre-release testing  
- **When** malfunctions are detected  
- **Then** issues are resolved before release

---

### 17. Continuous Improvement

**User Story:**  
As a football fan, I want my feedback and app reviews to be evaluated so that the app’s functionality can be improved over time.

**Acceptance Criteria:**  
- **Given** the user submits feedback or a review  
- **When** feedback is received  
- **Then** it is evaluated for potential improvements

---

### 18. Data Protection

**User Story:**  
As a football fan, I want my personal data to be processed in compliance with GDPR so that my privacy is protected.

**Acceptance Criteria:**  
- **Given** the user provides personal data  
- **When** the app processes the data  
- **Then** all processing is compliant with GDPR regulations

---

#### Ambiguities and Gaps

- The process for connecting "own interface" to the user interface is unclear; further clarification is needed.
- The exact personalization options available to users are not fully specified.
- The method for selecting favorite teams and channels is not described in detail.
- The specifics of offline functionality (e.g., which features are available offline) are not detailed.
- The process for evaluating user feedback and reviews is not described.

---

## HTML Mockups

---

### 1. Splash/Loading Screen (App Performance)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>App Loading</title>
  <style>
    body { display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; background: #222; color: #fff; }
    .loader { text-align: center; }
    .spinner { border: 6px solid #444; border-top: 6px solid #fff; border-radius: 50%; width: 48px; height: 48px; animation: spin 1s linear infinite; margin: 0 auto 16px; }
    @keyframes spin { 100% { transform: rotate(360deg); } }
  </style>
</head>
<body>
  <div class="loader">
    <div class="spinner"></div>
    <div>Loading Football App...</div>
  </div>
</body>
</html>
```

---

### 2. Registration and Login

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login / Register</title>
  <style>
    body { background: #f5f5f5; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .container { background: #fff; padding: 32px 24px; border-radius: 8px; box-shadow: 0 2px 8px #0002; width: 320px; }
    h2 { margin-top: 0; }
    input { width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; }
    button { width: 100%; padding: 10px; background: #007bff; color: #fff; border: none; border-radius: 4px; margin-top: 12px; }
    .switch { text-align: center; margin-top: 16px; font-size: 0.95em; }
    .switch a { color: #007bff; text-decoration: none; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Login</h2>
    <form>
      <input type="email" placeholder="Email" required>
      <input type="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
    <div class="switch">
      New user? <a href="#">Register here</a>
    </div>
  </div>
</body>
</html>
```

---

### 3. Home / Dashboard (UI Accessibility, Modules Overview)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Football App Dashboard</title>
  <style>
    body { margin: 0; font-family: sans-serif; background: #f5f5f5; }
    header { background: #222; color: #fff; padding: 16px; text-align: center; }
    nav { background: #fff; display: flex; justify-content: space-around; border-bottom: 1px solid #ddd; }
    nav a { padding: 12px 0; color: #222; text-decoration: none; flex: 1; text-align: center; }
    nav a.active { border-bottom: 2px solid #007bff; color: #007bff; }
    .modules { display: flex; flex-wrap: wrap; gap: 16px; padding: 16px; }
    .module { background: #fff; flex: 1 1 220px; min-width: 220px; padding: 16px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    .module h3 { margin-top: 0; }
  </style>
</head>
<body>
  <header>
    <h1>Football App</h1>
  </header>
  <nav>
    <a href="#" class="active">Home</a>
    <a href="#">News</a>
    <a href="#">Live Ticker</a>
    <a href="#">Leagues</a>
    <a href="#">Teams</a>
    <a href="#">Settings</a>
  </nav>
  <div class="modules">
    <div class="module">
      <h3>Personalized News</h3>
      <p>Latest news about your favorite teams.</p>
      <a href="#">View News</a>
    </div>
    <div class="module">
      <h3>Live Ticker</h3>
      <p>Real-time results for your favorite teams.</p>
      <a href="#">Open Live Ticker</a>
    </div>
    <div class="module">
      <h3>Leagues & Competitions</h3>
      <p>Browse all national and international leagues.</p>
      <a href="#">Browse Leagues</a>
    </div>
    <div class="module">
      <h3>Teams & Players</h3>
      <p>View detailed info about teams and players.</p>
      <a href="#">Explore Teams</a>
    </div>
    <div class="module">
      <h3>Settings</h3>
      <p>Personalize your app experience.</p>
      <a href="#">Go to Settings</a>
    </div>
  </div>
</body>
</html>
```

---

### 4. News Section (Personalized News, Social Sharing)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Personalized News</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    header { background: #222; color: #fff; padding: 16px; text-align: center; }
    .news-list { max-width: 600px; margin: 24px auto; }
    .news-item { background: #fff; margin-bottom: 16px; padding: 16px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    .news-item h4 { margin: 0 0 8px; }
    .meta { color: #888; font-size: 0.95em; margin-bottom: 8px; }
    .actions { margin-top: 8px; }
    .actions button { background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 6px 12px; cursor: pointer; }
  </style>
</head>
<body>
  <header>
    <h2>News - Your Favorite Teams</h2>
  </header>
  <div class="news-list">
    <div class="news-item">
      <h4>Team A wins the derby!</h4>
      <div class="meta">Source: Sky Sport | 2h ago</div>
      <p>Team A secured a thrilling victory in the city derby, with a last-minute goal by their star striker.</p>
      <div class="actions">
        <button>Share</button>
      </div>
    </div>
    <div class="news-item">
      <h4>Injury update: Team B midfielder</h4>
      <div class="meta">Source: DAZN | 1h ago</div>
      <p>Team B's key midfielder will be out for two weeks due to a minor injury sustained in training.</p>
      <div class="actions">
        <button>Share</button>
      </div>
    </div>
    <!-- More news items... -->
  </div>
</body>
</html>
```

---

### 5. Channel Selection Settings (Preferred Sports Channels)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Channel Selection</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 400px; margin: 40px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    .channels { list-style: none; padding: 0; }
    .channels li { margin-bottom: 12px; }
    label { cursor: pointer; }
    button { margin-top: 16px; background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Select Preferred Sports Channels</h2>
    <form>
      <ul class="channels">
        <li><label><input type="checkbox" checked> Sky Sport</label></li>
        <li><label><input type="checkbox"> DAZN</label></li>
        <li><label><input type="checkbox" checked> ESPN</label></li>
        <li><label><input type="checkbox"> BBC Sport</label></li>
      </ul>
      <button type="submit">Save Preferences</button>
    </form>
  </div>
</body>
</html>
```

---

### 6. Live Ticker (Favorite Teams, Real-Time Results)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Live Ticker</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    header { background: #222; color: #fff; padding: 16px; text-align: center; }
    .ticker { max-width: 500px; margin: 24px auto; background: #fff; border-radius: 8px; box-shadow: 0 1px 4px #0001; padding: 16px; }
    .match-header { display: flex; justify-content: space-between; align-items: center; }
    .score { font-size: 2em; font-weight: bold; }
    .events { margin-top: 16px; }
    .event { border-left: 3px solid #007bff; padding-left: 8px; margin-bottom: 8px; }
    .time { color: #888; font-size: 0.95em; }
  </style>
</head>
<body>
  <header>
    <h2>Live Ticker - Team A</h2>
  </header>
  <div class="ticker">
    <div class="match-header">
      <div>Team A</div>
      <div class="score">2 : 1</div>
      <div>Team B</div>
    </div>
    <div class="events">
      <div class="event"><span class="time">78'</span> Goal! Team A scores (Player X)</div>
      <div class="event"><span class="time">65'</span> Yellow card for Team B</div>
      <div class="event"><span class="time">50'</span> Goal! Team B scores (Player Y)</div>
      <div class="event"><span class="time">30'</span> Goal! Team A scores (Player Z)</div>
    </div>
  </div>
</body>
</html>
```

---

### 7. Leagues & Competitions (Comprehensive Coverage)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Leagues & Competitions</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 600px; margin: 32px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    .leagues { list-style: none; padding: 0; }
    .leagues li { margin-bottom: 12px; }
    .leagues a { color: #007bff; text-decoration: none; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Leagues & Competitions</h2>
    <ul class="leagues">
      <li><a href="#">Premier League (England)</a></li>
      <li><a href="#">La Liga (Spain)</a></li>
      <li><a href="#">Bundesliga (Germany)</a></li>
      <li><a href="#">UEFA Champions League</a></li>
      <li><a href="#">Serie A (Italy)</a></li>
      <!-- More leagues... -->
    </ul>
  </div>
</body>
</html>
```

---

### 8. League/Competition Details

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>League Details</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 600px; margin: 32px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    table { width: 100%; border-collapse: collapse; margin-top: 16px; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background: #f0f0f0; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Premier League</h2>
    <div>Country: England</div>
    <div>Season: 2023/24</div>
    <h3>Standings</h3>
    <table>
      <tr><th>Pos</th><th>Team</th><th>Pts</th></tr>
      <tr><td>1</td><td>Team A</td><td>65</td></tr>
      <tr><td>2</td><td>Team B</td><td>62</td></tr>
      <tr><td>3</td><td>Team C</td><td>59</td></tr>
      <!-- More rows... -->
    </table>
  </div>
</body>
</html>
```

---

### 9. Team/Player Profile (Detailed Info)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Team Profile</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 500px; margin: 32px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    .info { margin-bottom: 16px; }
    .players { margin-top: 16px; }
    .players ul { list-style: none; padding: 0; }
    .players li { margin-bottom: 6px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Team A</h2>
    <div class="info">
      <div>Founded: 1902</div>
      <div>Stadium: City Arena</div>
      <div>Coach: John Smith</div>
    </div>
    <div class="players">
      <h3>Players</h3>
      <ul>
        <li><a href="#">Player X (Forward)</a></li>
        <li><a href="#">Player Y (Midfielder)</a></li>
        <li><a href="#">Player Z (Defender)</a></li>
      </ul>
    </div>
  </div>
</body>
</html>
```

---

### 10. Match Page with Live Stream Links

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Match Page</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 500px; margin: 32px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    .teams { display: flex; justify-content: space-between; align-items: center; font-size: 1.2em; }
    .score { font-size: 2em; font-weight: bold; }
    .live-streams { margin-top: 24px; }
    .live-streams a { display: block; margin-bottom: 8px; color: #007bff; text-decoration: none; }
  </style>
</head>
<body>
  <div class="container">
    <div class="teams">
      <span>Team A</span>
      <span class="score">2 : 1</span>
      <span>Team B</span>
    </div>
    <div class="live-streams">
      <h3>Watch Live</h3>
      <a href="#">DAZN Live Stream</a>
      <a href="#">Sky Sport Live Stream</a>
    </div>
  </div>
</body>
</html>
```

---

### 11. Personalization Settings

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Personalization Settings</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 400px; margin: 40px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    label { display: block; margin: 12px 0 4px; }
    input[type="text"], select { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
    button { margin-top: 16px; background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Personalization</h2>
    <form>
      <label for="theme">Theme</label>
      <select id="theme">
        <option>Light</option>
        <option>Dark</option>
      </select>
      <label for="interface">Connect Interface</label>
      <input type="text" id="interface" placeholder="Enter interface URL or code">
      <button type="submit">Apply Settings</button>
    </form>
  </div>
</body>
</html>
```

---

### 12. Notifications

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Notifications</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 400px; margin: 40px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    .notification { background: #e6f7ff; border-left: 4px solid #007bff; padding: 12px; margin-bottom: 12px; border-radius: 4px; }
    label { display: block; margin: 12px 0 4px; }
    button { margin-top: 16px; background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Notifications</h2>
    <form>
      <label><input type="checkbox" checked> Enable notifications for my favorite teams</label>
      <label><input type="checkbox"> Enable news notifications</label>
      <button type="submit">Save</button>
    </form>
    <div class="notification">
      <strong>Team A scored!</strong> 2:1 vs Team B (Live)
    </div>
    <div class="notification">
      <strong>New article:</strong> Team B signs new midfielder.
    </div>
  </div>
</body>
</html>
```

---

### 13. Feedback / Review Submission (Continuous Improvement)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Feedback</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 400px; margin: 40px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    textarea { width: 100%; min-height: 80px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
    button { margin-top: 16px; background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Submit Feedback</h2>
    <form>
      <textarea placeholder="Your feedback or review..."></textarea>
      <button type="submit">Send</button>
    </form>
  </div>
</body>
</html>
```

---

### 14. Offline Mode

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Offline Mode</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 400px; margin: 40px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; text-align: center; }
    .offline { color: #d9534f; font-weight: bold; margin-bottom: 16px; }
    .info { color: #888; }
  </style>
</head>
<body>
  <div class="container">
    <div class="offline">You are offline</div>
    <div class="info">Previously loaded news and match data are available.<br>Some features may be limited until you reconnect.</div>
  </div>
</body>
</html>
```

---

### 15. GDPR / Data Protection Notice

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Data Protection</title>
  <style>
    body { font-family: sans-serif; background: #f5f5f5; margin: 0; }
    .container { max-width: 400px; margin: 40px auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 4px #0001; }
    h2 { margin-top: 0; }
    .notice { color: #555; font-size: 0.98em; margin-bottom: 16px; }
    button { background: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Data Protection</h2>
    <div class="notice">
      We process your personal data in compliance with GDPR. Your privacy is important to us.
    </div>
    <button>Accept & Continue</button>
  </div>
</body>
</html>
```

---

## Traceability Matrix

---

| User Story # | User Story Title                        | Mockup(s)                                                                                 |
|--------------|-----------------------------------------|-------------------------------------------------------------------------------------------|
| 1            | App Performance                         | Splash/Loading Screen                                                                     |
| 2            | Personalized News                       | News Section, Home/Dashboard                                                              |
| 3            | Preferred Sports Channels               | Channel Selection Settings                                                                |
| 4            | Live Ticker for Favorite Teams          | Live Ticker, Home/Dashboard                                                               |
| 5            | Comprehensive Coverage                  | Leagues & Competitions, League/Competition Details, Home/Dashboard                        |
| 6            | Detailed Team and Player Information    | Team/Player Profile, Home/Dashboard                                                       |
| 7            | Live Stream Links                       | Match Page with Live Stream Links                                                         |
| 8            | Real-Time Live Results                  | Live Ticker                                                                               |
| 9            | User Interface Accessibility            | Home/Dashboard                                                                            |
| 10           | App Personalization                     | Personalization Settings, Home/Dashboard                                                  |
| 11           | Notifications                           | Notifications                                                                             |
| 12           | Registration and Login                  | Registration and Login                                                                    |
| 13           | Social Sharing                          | News Section                                                                              |
| 14           | Offline Functionality                   | Offline Mode                                                                              |
| 15           | Scalability                             | Splash/Loading Screen, Home/Dashboard                                                     |
| 16           | Testing and Support                     | (Not directly mockuped; implied in app flows)                                             |
| 17           | Continuous Improvement                  | Feedback / Review Submission                                                              |
| 18           | Data Protection                         | GDPR / Data Protection Notice                                                             |

---

**End of Report**