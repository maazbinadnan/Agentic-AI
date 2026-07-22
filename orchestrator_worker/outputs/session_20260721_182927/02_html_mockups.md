# HTML Mockups

Here are HTML mockups for the key user flows and screens described in your user stories and acceptance criteria. Each mockup is focused, wireframe-level, and covers the primary interactions.

---

### 1. Splash/Loading Screen (App Performance)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Football App - Loading</title>
  <style>
    body { margin:0; display:flex; align-items:center; justify-content:center; height:100vh; background:#222; color:#fff; font-family:sans-serif;}
    .loader { text-align:center;}
    .logo { font-size:2em; margin-bottom:20px;}
    .spinner { border:6px solid #444; border-top:6px solid #fff; border-radius:50%; width:48px; height:48px; animation:spin 1s linear infinite; margin:0 auto;}
    @keyframes spin { 100% { transform: rotate(360deg); } }
  </style>
</head>
<body>
  <div class="loader">
    <div class="logo">⚽ Football App</div>
    <div class="spinner"></div>
    <div style="margin-top:16px;">Loading...</div>
  </div>
</body>
</html>
```

---

### 2. Registration & Login

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Football App - Login/Register</title>
  <style>
    body { background:#f5f5f5; font-family:sans-serif; display:flex; align-items:center; justify-content:center; height:100vh; margin:0;}
    .container { background:#fff; padding:32px 24px; border-radius:8px; box-shadow:0 2px 8px #0002; width:320px;}
    h2 { margin-top:0;}
    .tabs { display:flex; margin-bottom:16px;}
    .tab { flex:1; text-align:center; padding:8px; cursor:pointer; border-bottom:2px solid #eee;}
    .tab.active { border-bottom:2px solid #007bff; color:#007bff;}
    form { display:flex; flex-direction:column;}
    input { margin-bottom:12px; padding:8px; border:1px solid #ccc; border-radius:4px;}
    button { background:#007bff; color:#fff; border:none; padding:10px; border-radius:4px; cursor:pointer;}
    button:active { background:#0056b3;}
  </style>
  <script>
    function showTab(tab) {
      document.getElementById('loginForm').style.display = tab === 'login' ? 'block' : 'none';
      document.getElementById('registerForm').style.display = tab === 'register' ? 'block' : 'none';
      document.getElementById('loginTab').classList.toggle('active', tab === 'login');
      document.getElementById('registerTab').classList.toggle('active', tab === 'register');
    }
  </script>
</head>
<body>
  <div class="container">
    <div class="tabs">
      <div id="loginTab" class="tab active" onclick="showTab('login')">Login</div>
      <div id="registerTab" class="tab" onclick="showTab('register')">Register</div>
    </div>
    <form id="loginForm">
      <h2>Login</h2>
      <input type="email" placeholder="Email" required>
      <input type="password" placeholder="Password" required>
      <button type="submit">Log In</button>
    </form>
    <form id="registerForm" style="display:none;">
      <h2>Register</h2>
      <input type="text" placeholder="Name" required>
      <input type="email" placeholder="Email" required>
      <input type="password" placeholder="Password" required>
      <button type="submit">Register</button>
    </form>
  </div>
  <script>showTab('login');</script>
</body>
</html>
```

---

### 3. Personalization: Favorite Teams & Channels

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Select Favorites</title>
  <style>
    body { background:#f5f5f5; font-family:sans-serif; margin:0; }
    .container { max-width:400px; margin:40px auto; background:#fff; padding:24px; border-radius:8px; box-shadow:0 2px 8px #0002;}
    h2 { margin-top:0;}
    .section { margin-bottom:24px;}
    .list { display:flex; flex-wrap:wrap; gap:8px;}
    .item { background:#eee; padding:8px 12px; border-radius:16px; cursor:pointer;}
    .item.selected { background:#007bff; color:#fff;}
    button { width:100%; background:#007bff; color:#fff; border:none; padding:12px; border-radius:4px; font-size:1em; cursor:pointer;}
    button:active { background:#0056b3;}
  </style>
  <script>
    function toggleSelection(el) { el.classList.toggle('selected'); }
  </script>
</head>
<body>
  <div class="container">
    <h2>Personalize Your Experience</h2>
    <div class="section">
      <div><strong>Select Favorite Teams:</strong></div>
      <div class="list">
        <div class="item" onclick="toggleSelection(this)">FC Barcelona</div>
        <div class="item" onclick="toggleSelection(this)">Manchester United</div>
        <div class="item" onclick="toggleSelection(this)">Bayern Munich</div>
        <div class="item" onclick="toggleSelection(this)">Juventus</div>
        <div class="item" onclick="toggleSelection(this)">Real Madrid</div>
      </div>
    </div>
    <div class="section">
      <div><strong>Select Preferred Channels:</strong></div>
      <div class="list">
        <div class="item" onclick="toggleSelection(this)">DAZN</div>
        <div class="item" onclick="toggleSelection(this)">Sky Sport</div>
        <div class="item" onclick="toggleSelection(this)">ESPN</div>
      </div>
    </div>
    <button>Continue</button>
  </div>
</body>
</html>
```

---

### 4. News Section (Personalized News)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Football News</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .header { background:#222; color:#fff; padding:16px; text-align:center;}
    .news-list { max-width:600px; margin:24px auto; }
    .news-item { background:#fff; margin-bottom:16px; padding:16px; border-radius:8px; box-shadow:0 1px 4px #0001;}
    .news-title { font-weight:bold; margin-bottom:8px;}
    .news-meta { color:#888; font-size:0.9em; margin-bottom:8px;}
    .news-actions { margin-top:8px;}
    .share-btn { background:#007bff; color:#fff; border:none; padding:6px 12px; border-radius:4px; cursor:pointer; font-size:0.9em;}
    .share-btn:active { background:#0056b3;}
  </style>
</head>
<body>
  <div class="header">News for: <strong>FC Barcelona, DAZN</strong></div>
  <div class="news-list">
    <div class="news-item">
      <div class="news-title">Barcelona wins 3-1 against Real Madrid</div>
      <div class="news-meta">La Liga • 2 hours ago</div>
      <div>Barcelona secures a crucial victory in El Clásico. Messi scores twice.</div>
      <div class="news-actions">
        <button class="share-btn">Share</button>
      </div>
    </div>
    <div class="news-item">
      <div class="news-title">DAZN to broadcast Champions League final</div>
      <div class="news-meta">Champions League • 1 hour ago</div>
      <div>DAZN confirms exclusive rights for the upcoming final.</div>
      <div class="news-actions">
        <button class="share-btn">Share</button>
      </div>
    </div>
  </div>
</body>
</html>
```

---

### 5. Live Ticker

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Live Ticker</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .header { background:#222; color:#fff; padding:16px; text-align:center;}
    .ticker { max-width:500px; margin:32px auto; background:#fff; border-radius:8px; box-shadow:0 1px 4px #0001; padding:24px;}
    .match { display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;}
    .teams { font-weight:bold;}
    .score { font-size:1.5em;}
    .minute { color:#007bff;}
    .event { margin-left:24px; color:#444;}
  </style>
</head>
<body>
  <div class="header">Live Ticker - FC Barcelona</div>
  <div class="ticker">
    <div class="match">
      <span class="teams">Barcelona vs Real Madrid</span>
      <span class="score">2 - 1</span>
      <span class="minute">78'</span>
    </div>
    <div class="event">77' ⚽ Goal! Messi scores for Barcelona.</div>
    <div class="event">65' 🟨 Yellow card for Ramos (Real Madrid).</div>
    <div class="event">60' 🔄 Substitution: Fati in, Griezmann out.</div>
  </div>
</body>
</html>
```

---

### 6. Leagues & Competitions Browser

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Leagues & Competitions</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .header { background:#222; color:#fff; padding:16px; text-align:center;}
    .leagues { max-width:500px; margin:32px auto;}
    .league { background:#fff; margin-bottom:12px; padding:16px; border-radius:8px; box-shadow:0 1px 4px #0001; cursor:pointer;}
    .league:hover { background:#e6f0ff;}
    .league-title { font-weight:bold;}
    .league-country { color:#888; font-size:0.9em;}
  </style>
</head>
<body>
  <div class="header">Leagues & Competitions</div>
  <div class="leagues">
    <div class="league">
      <div class="league-title">Premier League</div>
      <div class="league-country">England</div>
    </div>
    <div class="league">
      <div class="league-title">La Liga</div>
      <div class="league-country">Spain</div>
    </div>
    <div class="league">
      <div class="league-title">Bundesliga</div>
      <div class="league-country">Germany</div>
    </div>
    <div class="league">
      <div class="league-title">UEFA Champions League</div>
      <div class="league-country">Europe</div>
    </div>
  </div>
</body>
</html>
```

---

### 7. Team/Player Details

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Team Details</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .container { max-width:500px; margin:32px auto; background:#fff; border-radius:8px; box-shadow:0 1px 4px #0001; padding:24px;}
    .team-header { display:flex; align-items:center; margin-bottom:16px;}
    .team-logo { width:48px; height:48px; background:#eee; border-radius:50%; margin-right:16px; display:flex; align-items:center; justify-content:center; font-size:2em;}
    .team-name { font-size:1.3em; font-weight:bold;}
    .section { margin-bottom:16px;}
    .section-title { font-weight:bold; margin-bottom:4px;}
    .player-list { display:flex; flex-wrap:wrap; gap:8px;}
    .player { background:#f0f0f0; padding:6px 10px; border-radius:12px;}
  </style>
</head>
<body>
  <div class="container">
    <div class="team-header">
      <div class="team-logo">🏟️</div>
      <div class="team-name">FC Barcelona</div>
    </div>
    <div class="section">
      <div class="section-title">Founded:</div>
      1899
    </div>
    <div class="section">
      <div class="section-title">Stadium:</div>
      Camp Nou
    </div>
    <div class="section">
      <div class="section-title">Coach:</div>
      Xavi Hernández
    </div>
    <div class="section">
      <div class="section-title">Players:</div>
      <div class="player-list">
        <div class="player">Lionel Messi</div>
        <div class="player">Ansu Fati</div>
        <div class="player">Frenkie de Jong</div>
        <div class="player">Marc-André ter Stegen</div>
      </div>
    </div>
  </div>
</body>
</html>
```

---

### 8. Match Page with Live Stream Links

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Match Details</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .container { max-width:500px; margin:32px auto; background:#fff; border-radius:8px; box-shadow:0 1px 4px #0001; padding:24px;}
    .match-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;}
    .teams { font-weight:bold;}
    .score { font-size:1.3em;}
    .section { margin-bottom:16px;}
    .stream-links { display:flex; gap:12px;}
    .stream-link { background:#007bff; color:#fff; padding:8px 16px; border-radius:4px; text-decoration:none;}
    .stream-link:active { background:#0056b3;}
    .note { color:#888; font-size:0.9em;}
  </style>
</head>
<body>
  <div class="container">
    <div class="match-header">
      <span class="teams">Barcelona vs Real Madrid</span>
      <span class="score">Live</span>
    </div>
    <div class="section">
      <div><strong>Live Stream:</strong></div>
      <div class="stream-links">
        <a href="#" class="stream-link">Watch on DAZN</a>
        <a href="#" class="stream-link">Watch on Sky Sport</a>
      </div>
      <div class="note">Available in your country</div>
    </div>
    <div class="section">
      <div><strong>Match Events:</strong></div>
      <div>78' ⚽ Messi scores for Barcelona.</div>
      <div>65' 🟨 Yellow card for Ramos.</div>
    </div>
  </div>
</body>
</html>
```

---

### 9. Notification Example (In-app)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Notification Example</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0; height:100vh;}
    .notification { position:fixed; top:24px; right:24px; background:#007bff; color:#fff; padding:16px 24px; border-radius:8px; box-shadow:0 2px 8px #0003; z-index:100;}
    .close-btn { background:none; border:none; color:#fff; font-size:1.2em; position:absolute; top:8px; right:12px; cursor:pointer;}
  </style>
  <script>
    function closeNotif() { document.getElementById('notif').style.display='none'; }
  </script>
</head>
<body>
  <div id="notif" class="notification">
    <button class="close-btn" onclick="closeNotif()">×</button>
    <strong>Goal!</strong> Messi scores for Barcelona (78')
  </div>
</body>
</html>
```

---

### 10. Social Media Sharing (from News)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Share News</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .container { max-width:400px; margin:40px auto; background:#fff; padding:24px; border-radius:8px; box-shadow:0 2px 8px #0002;}
    .news-title { font-weight:bold; margin-bottom:8px;}
    .share-options { display:flex; gap:12px; margin-top:16px;}
    .share-btn { background:#eee; border:none; border-radius:4px; padding:8px 16px; cursor:pointer;}
    .share-btn.facebook { background:#4267B2; color:#fff;}
    .share-btn.twitter { background:#1DA1F2; color:#fff;}
    .share-btn.whatsapp { background:#25D366; color:#fff;}
  </style>
</head>
<body>
  <div class="container">
    <div class="news-title">Barcelona wins 3-1 against Real Madrid</div>
    <div>Barcelona secures a crucial victory in El Clásico. Messi scores twice.</div>
    <div class="share-options">
      <button class="share-btn facebook">Facebook</button>
      <button class="share-btn twitter">Twitter</button>
      <button class="share-btn whatsapp">WhatsApp</button>
    </div>
  </div>
</body>
</html>
```

---

### 11. Offline Usability (Offline Banner)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Offline Mode</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .offline-banner { background:#ff9800; color:#fff; text-align:center; padding:12px; }
    .container { max-width:500px; margin:32px auto; background:#fff; border-radius:8px; box-shadow:0 1px 4px #0001; padding:24px;}
    .news-item { margin-bottom:16px;}
    .news-title { font-weight:bold;}
  </style>
</head>
<body>
  <div class="offline-banner">You are offline. Showing last available information.</div>
  <div class="container">
    <div class="news-item">
      <div class="news-title">Barcelona wins 3-1 against Real Madrid</div>
      <div>Last updated: 2 hours ago</div>
    </div>
    <div class="news-item">
      <div class="news-title">DAZN to broadcast Champions League final</div>
      <div>Last updated: 1 hour ago</div>
    </div>
  </div>
</body>
</html>
```

---

### 12. Feedback Submission

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Submit Feedback</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .container { max-width:400px; margin:40px auto; background:#fff; padding:24px; border-radius:8px; box-shadow:0 2px 8px #0002;}
    h2 { margin-top:0;}
    textarea { width:100%; min-height:80px; margin-bottom:12px; padding:8px; border:1px solid #ccc; border-radius:4px;}
    button { width:100%; background:#007bff; color:#fff; border:none; padding:12px; border-radius:4px; font-size:1em; cursor:pointer;}
    button:active { background:#0056b3;}
  </style>
</head>
<body>
  <div class="container">
    <h2>Send Feedback</h2>
    <form>
      <textarea placeholder="Your feedback or review..." required></textarea>
      <button type="submit">Submit</button>
    </form>
  </div>
</body>
</html>
```

---

### 13. GDPR Consent

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>GDPR Consent</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .gdpr-banner { position:fixed; bottom:0; left:0; right:0; background:#222; color:#fff; padding:20px; text-align:center; z-index:100;}
    .gdpr-banner button { background:#007bff; color:#fff; border:none; padding:8px 16px; border-radius:4px; margin-left:16px; cursor:pointer;}
    .gdpr-banner button:active { background:#0056b3;}
  </style>
</head>
<body>
  <div class="gdpr-banner">
    We value your privacy. Your data is processed in accordance with GDPR. 
    <button>Accept</button>
    <button style="background:#888;">Learn More</button>
  </div>
</body>
</html>
```

---

### 14. Testing & Support (Support Contact)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Support & Testing</title>
  <style>
    body { font-family:sans-serif; background:#f5f5f5; margin:0;}
    .container { max-width:400px; margin:40px auto; background:#fff; padding:24px; border-radius:8px; box-shadow:0 2px 8px #0002;}
    h2 { margin-top:0;}
    .info { margin-bottom:16px;}
    .contact { background:#f0f0f0; padding:12px; border-radius:4px;}
  </style>
</head>
<body>
  <div class="container">
    <h2>Support & Testing</h2>
    <div class="info">
      If you encounter any issues during testing, please contact our support team.
    </div>
    <div class="contact">
      Email: <a href="mailto:support@footballapp.com">support@footballapp.com</a>
    </div>
  </div>
</body>
</html>
```

---

**Next Steps:**  
Let me know if you want any of these saved as files, or if you need further flows or states!