# HTML Mockups

Here are HTML mockups for the key screens and interactions described in your user stories and acceptance criteria. Each mockup is focused, wireframe-level, and covers the primary user flows.

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

If you need any of these saved as files or further split by user story, let me know!