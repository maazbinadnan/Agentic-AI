# HTML Mockups

---ARCH_MAPPING---
| Screen / File Name                | Mapped User Story / Requirement         | Key Interactions & States Visualized                                                                                  |
| :-------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| `splash_startup_mockup.html`      | US-001, FR-001, NFR-001                | Splash/loading indicator, 2s performance note                                                                         |
| `login_register_mockup.html`      | US-006, FR-006, US-012                 | Registration/login toggle, GDPR consent, form validation, error state                                                 |
| `news_feed_mockup.html`           | US-002, FR-002, US-009, FR-009         | News feed (personalized/general), empty state, offline indicator, share button                                        |
| `live_ticker_mockup.html`         | US-003, FR-003, NFR-002, US-009        | Live ticker updates, offline state, last data, favorite team filter                                                   |
| `team_player_info_mockup.html`    | US-004, FR-004                         | Team details, player details, navigation between team/player                                                          |
| `match_page_mockup.html`          | US-005, FR-005, NFR-006                | Live stream link (rights fulfilled), no link (rights not fulfilled), country rights note                              |
| `settings_notifications_mockup.html`| US-007, FR-007, US-002                | Notification toggle, favorite teams/channels selection, notification enabled/disabled states                          |
| `feedback_testing_mockup.html`    | US-011, FR-011                         | Feedback form, feedback log, pre-release test checklist                                                               |
---END_ARCH_MAPPING---

---DESIGN_TRADEOFFS---
- **Startup & Performance (US-001):** Splash screen is minimal, with a centered logo and loading indicator, and a note on 2s load time to emphasize performance. No extra branding or animation to avoid scope creep.
- **Registration/Login & GDPR (US-006, US-012):** Unified form with toggle for login/registration. GDPR consent checkbox is required for registration. Inline error messages for validation and failed login.
- **Personalized News Feed & Offline (US-002, US-009):** News feed adapts to favorite selections; if none, shows general news. Offline state shows cached content with a clear offline banner.
- **Live Ticker (US-003, US-009):** Ticker updates are visually timestamped. Offline state shows last data and an offline indicator. Only favorite teams’ matches are shown if selected.
- **Team/Player Info (US-004):** Card-based layout for team and player details, with navigation between them. No speculative stats or features.
- **Live Stream Rights (US-005):** Match page conditionally shows live stream link or a rights-unavailable message, based on country/rights logic.
- **Notifications & Favorites (US-007, US-002):** Settings page allows toggling notifications and selecting favorites. Disabled state is visually distinct.
- **Feedback & Testing (US-011):** Simple feedback form and a log of submitted feedback. Pre-release checklist is a static list for QA.
---END_DESIGN_TRADEOFFS---

<html_file name="splash_startup_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Splash / Startup Wireframe - US-001</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    .splash-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      background: var(--card-bg);
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(23,43,77,0.04);
      padding: 48px 32px;
      min-width: 320px;
    }
    .logo {
      width: 64px;
      height: 64px;
      background: var(--primary-color);
      border-radius: 50%;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 2rem;
      font-weight: bold;
      letter-spacing: 2px;
      user-select: none;
    }
    .loading {
      margin: 16px 0 8px 0;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .dot {
      width: 10px;
      height: 10px;
      background: var(--primary-color);
      border-radius: 50%;
      animation: bounce 1s infinite alternate;
    }
    .dot:nth-child(2) { animation-delay: 0.2s; }
    .dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes bounce {
      to { transform: translateY(-8px); }
    }
    .startup-note {
      font-size: 0.95rem;
      color: #6b778c;
      margin-top: 12px;
      text-align: center;
    }
  </style>
</head>
<body>
  <main class="splash-container" aria-label="App Startup Splash">
    <div class="logo" aria-label="App Logo">FB</div>
    <div class="loading" aria-label="Loading Indicator">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
    <div class="startup-note">
      Loading...<br>
      <strong>App will be ready in under 2 seconds</strong>
    </div>
  </main>
</body>
</html>
</html_file>

<html_file name="login_register_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login & Registration Wireframe - US-006, US-012</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
      --error-color: #dc3545;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    .auth-card {
      background: var(--card-bg);
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(23,43,77,0.04);
      padding: 40px 32px 32px 32px;
      min-width: 340px;
      display: flex;
      flex-direction: column;
      align-items: stretch;
    }
    .toggle-row {
      display: flex;
      justify-content: center;
      gap: 16px;
      margin-bottom: 24px;
    }
    .toggle-btn {
      background: none;
      border: none;
      color: var(--primary-color);
      font-weight: 600;
      font-size: 1rem;
      cursor: pointer;
      padding: 4px 12px;
      border-bottom: 2px solid transparent;
      transition: border 0.2s;
    }
    .toggle-btn.active {
      border-bottom: 2px solid var(--primary-color);
      color: var(--text-color);
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    label {
      font-size: 0.98rem;
      margin-bottom: 4px;
    }
    input[type="email"], input[type="password"], input[type="text"] {
      padding: 8px 10px;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      font-size: 1rem;
      background: #f8f9fa;
      color: var(--text-color);
    }
    .gdpr-row {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 0.95rem;
      margin-top: -8px;
    }
    .gdpr-row input[type="checkbox"] {
      margin-top: 2px;
    }
    .submit-btn {
      background: var(--primary-color);
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: 10px 0;
      font-size: 1.05rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 8px;
      transition: background 0.2s;
    }
    .submit-btn:active {
      background: #003380;
    }
    .error-msg {
      color: var(--error-color);
      font-size: 0.97rem;
      margin-top: -8px;
      margin-bottom: 4px;
    }
    .success-msg {
      color: #388e3c;
      font-size: 0.97rem;
      margin-top: -8px;
      margin-bottom: 4px;
    }
    .forgot-link {
      font-size: 0.93rem;
      color: var(--primary-color);
      text-decoration: underline;
      cursor: pointer;
      margin-top: -8px;
      align-self: flex-end;
    }
  </style>
</head>
<body>
  <main class="auth-card" aria-label="Login and Registration">
    <div class="toggle-row" role="tablist">
      <button class="toggle-btn active" role="tab" aria-selected="true" aria-controls="login-form">Login</button>
      <button class="toggle-btn" role="tab" aria-selected="false" aria-controls="register-form">Register</button>
    </div>
    <!-- Login Form (default) -->
    <form id="login-form" autocomplete="on">
      <label for="login-email">Email</label>
      <input type="email" id="login-email" name="email" required autocomplete="username" value="fan@example.com">
      <label for="login-password">Password</label>
      <input type="password" id="login-password" name="password" required autocomplete="current-password" value="••••••••">
      <span class="forgot-link" tabindex="0">Forgot password?</span>
      <!-- Error State Example -->
      <div class="error-msg" style="display:block;">Incorrect email or password.</div>
      <button class="submit-btn" type="submit">Login</button>
    </form>
    <!-- Registration Form (hidden by default) -->
    <form id="register-form" style="display:none;">
      <label for="reg-email">Email</label>
      <input type="email" id="reg-email" name="email" required autocomplete="username">
      <label for="reg-password">Password</label>
      <input type="password" id="reg-password" name="password" required autocomplete="new-password">
      <div class="gdpr-row">
        <input type="checkbox" id="gdpr-consent" name="gdpr-consent" required>
        <label for="gdpr-consent">I consent to the processing of my personal data in accordance with GDPR.</label>
      </div>
      <!-- Error State Example -->
      <div class="error-msg" style="display:block;">Please provide consent to continue.</div>
      <button class="submit-btn" type="submit">Register</button>
    </form>
  </main>
  <script>
    // Simple toggle logic for wireframe demo
    const loginBtn = document.querySelectorAll('.toggle-btn')[0];
    const regBtn = document.querySelectorAll('.toggle-btn')[1];
    const loginForm = document.getElementById('login-form');
    const regForm = document.getElementById('register-form');
    loginBtn.onclick = () => {
      loginBtn.classList.add('active');
      regBtn.classList.remove('active');
      loginForm.style.display = '';
      regForm.style.display = 'none';
    };
    regBtn.onclick = () => {
      regBtn.classList.add('active');
      loginBtn.classList.remove('active');
      regForm.style.display = '';
      loginForm.style.display = 'none';
    };
  </script>
</body>
</html>
</html_file>

<html_file name="news_feed_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>News Feed Wireframe - US-002, US-009</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
      --offline-color: #ffecb3;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      font-size: 1.3rem;
      font-weight: 600;
      letter-spacing: 1px;
    }
    .offline-banner {
      background: var(--offline-color);
      color: #7c4700;
      text-align: center;
      padding: 8px 0;
      font-size: 1rem;
      border-bottom: 1px solid #ffe082;
    }
    .feed-container {
      max-width: 600px;
      margin: 32px auto;
      padding: 0 16px;
    }
    .news-card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      margin-bottom: 20px;
      padding: 20px 18px 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      position: relative;
    }
    .news-title {
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 2px;
    }
    .news-meta {
      font-size: 0.93rem;
      color: #6b778c;
      margin-bottom: 6px;
    }
    .news-content {
      font-size: 1rem;
      color: var(--text-color);
    }
    .share-btn {
      background: none;
      border: none;
      color: var(--primary-color);
      font-size: 0.97rem;
      font-weight: 600;
      cursor: pointer;
      align-self: flex-end;
      margin-top: 6px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .share-btn:after {
      content: "🔗";
      font-size: 1.1em;
    }
    .empty-state {
      text-align: center;
      color: #6b778c;
      margin: 48px 0;
      font-size: 1.1rem;
    }
  </style>
</head>
<body>
  <header>Football News Feed</header>
  <!-- Offline State Example -->
  <div class="offline-banner" role="status">Offline: Showing cached news only</div>
  <main class="feed-container" aria-label="News Feed">
    <!-- Personalized News Example -->
    <article class="news-card">
      <div class="news-title">Manchester United Signs New Striker</div>
      <div class="news-meta">Team: Manchester United &middot; Source: Sky Sports &middot; 2h ago</div>
      <div class="news-content">
        Manchester United have completed the signing of John Doe from FC Example for a reported fee of £50m...
      </div>
      <button class="share-btn" aria-label="Share this news">Share</button>
    </article>
    <article class="news-card">
      <div class="news-title">Liverpool Clinches Dramatic Win</div>
      <div class="news-meta">Team: Liverpool &middot; Source: BBC Sport &middot; 1h ago</div>
      <div class="news-content">
        Liverpool secured a last-minute victory over Chelsea in a thrilling encounter at Anfield...
      </div>
      <button class="share-btn" aria-label="Share this news">Share</button>
    </article>
    <!-- Empty State Example -->
    <div class="empty-state">No news available for your selected favorites.<br>Showing general football news.</div>
  </main>
</body>
</html>
</html_file>

<html_file name="live_ticker_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Live Ticker Wireframe - US-003, US-009</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
      --offline-color: #ffecb3;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      font-size: 1.3rem;
      font-weight: 600;
      letter-spacing: 1px;
    }
    .offline-banner {
      background: var(--offline-color);
      color: #7c4700;
      text-align: center;
      padding: 8px 0;
      font-size: 1rem;
      border-bottom: 1px solid #ffe082;
    }
    .ticker-container {
      max-width: 500px;
      margin: 32px auto;
      padding: 0 16px;
    }
    .match-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px 8px 0 0;
      padding: 16px 18px;
      font-size: 1.1rem;
      font-weight: 600;
    }
    .ticker-list {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-top: none;
      border-radius: 0 0 8px 8px;
      padding: 0 18px 12px 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .ticker-event {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 1rem;
    }
    .event-time {
      color: var(--primary-color);
      font-weight: 600;
      min-width: 48px;
      text-align: right;
    }
    .event-desc {
      color: var(--text-color);
    }
    .last-updated {
      font-size: 0.93rem;
      color: #6b778c;
      text-align: right;
      margin-top: 8px;
    }
    .empty-state {
      text-align: center;
      color: #6b778c;
      margin: 48px 0;
      font-size: 1.1rem;
    }
  </style>
</head>
<body>
  <header>Live Ticker</header>
  <!-- Offline State Example -->
  <div class="offline-banner" role="status">Offline: Showing last available match data</div>
  <main class="ticker-container" aria-label="Live Ticker">
    <div class="match-header">
      <span>Manchester United vs Liverpool</span>
      <span>2 - 1</span>
    </div>
    <section class="ticker-list" aria-label="Live Events">
      <div class="ticker-event">
        <span class="event-time">78'</span>
        <span class="event-desc"><strong>Goal!</strong> John Doe (Manchester United) scores. 2-1</span>
      </div>
      <div class="ticker-event">
        <span class="event-time">65'</span>
        <span class="event-desc"><strong>Yellow Card:</strong> Jane Smith (Liverpool)</span>
      </div>
      <div class="ticker-event">
        <span class="event-time">54'</span>
        <span class="event-desc"><strong>Goal!</strong> Alex Brown (Liverpool) scores. 1-1</span>
      </div>
    </section>
    <div class="last-updated">Last updated: 2 min ago</div>
    <!-- Empty State Example -->
    <!-- <div class="empty-state">No live matches for your favorite teams at the moment.</div> -->
  </main>
</body>
</html>
</html_file>

<html_file name="team_player_info_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Team & Player Info Wireframe - US-004</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      font-size: 1.3rem;
      font-weight: 600;
      letter-spacing: 1px;
    }
    .info-container {
      max-width: 600px;
      margin: 32px auto;
      padding: 0 16px;
      display: flex;
      flex-direction: column;
      gap: 32px;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px 20px 20px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .card-title {
      font-size: 1.15rem;
      font-weight: 600;
      margin-bottom: 4px;
    }
    .card-meta {
      font-size: 0.97rem;
      color: #6b778c;
      margin-bottom: 8px;
    }
    .card-content {
      font-size: 1rem;
      color: var(--text-color);
    }
    .player-list {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 8px;
    }
    .player-chip {
      background: #e3eaff;
      color: var(--primary-color);
      border-radius: 16px;
      padding: 4px 12px;
      font-size: 0.97rem;
      cursor: pointer;
      border: none;
      margin-bottom: 4px;
    }
    .player-chip:active {
      background: #c6d6f7;
    }
    .back-link {
      color: var(--primary-color);
      font-size: 0.97rem;
      text-decoration: underline;
      cursor: pointer;
      margin-bottom: 8px;
      align-self: flex-start;
    }
  </style>
</head>
<body>
  <header>Team & Player Info</header>
  <main class="info-container" aria-label="Team and Player Information">
    <!-- Team Details -->
    <section class="card" aria-label="Team Details">
      <div class="card-title">Manchester United</div>
      <div class="card-meta">Founded: 1878 &middot; Stadium: Old Trafford &middot; Coach: Erik ten Hag</div>
      <div class="card-content">
        Manchester United is one of the most successful football clubs in England, with a rich history and a global fanbase.
      </div>
      <div class="player-list" aria-label="Player List">
        <button class="player-chip" aria-label="View player David De Gea">David De Gea</button>
        <button class="player-chip" aria-label="View player Bruno Fernandes">Bruno Fernandes</button>
        <button class="player-chip" aria-label="View player Marcus Rashford">Marcus Rashford</button>
      </div>
    </section>
    <!-- Player Details Example -->
    <section class="card" aria-label="Player Details">
      <span class="back-link" tabindex="0">&larr; Back to Team</span>
      <div class="card-title">Bruno Fernandes</div>
      <div class="card-meta">Position: Midfielder &middot; Age: 28 &middot; Nationality: Portugal</div>
      <div class="card-content">
        Bruno Fernandes is known for his vision, passing, and goal-scoring ability. He joined Manchester United in 2020.
      </div>
    </section>
  </main>
</body>
</html>
</html_file>

<html_file name="match_page_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Match Page Wireframe - US-005</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
      --error-color: #dc3545;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      font-size: 1.3rem;
      font-weight: 600;
      letter-spacing: 1px;
    }
    .match-container {
      max-width: 500px;
      margin: 32px auto;
      padding: 0 16px;
    }
    .match-card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px 20px 20px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .teams-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 8px;
    }
    .match-meta {
      font-size: 0.97rem;
      color: #6b778c;
      margin-bottom: 8px;
    }
    .live-stream-link {
      background: var(--primary-color);
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: 10px 0;
      font-size: 1.05rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 8px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      width: 100%;
    }
    .no-rights-msg {
      color: var(--error-color);
      background: #fff0f0;
      border: 1px solid #f5c2c7;
      border-radius: 4px;
      padding: 10px 12px;
      font-size: 0.98rem;
      margin-top: 8px;
      text-align: center;
    }
    .rights-note {
      font-size: 0.93rem;
      color: #6b778c;
      margin-top: 6px;
      text-align: center;
    }
  </style>
</head>
<body>
  <header>Match Page</header>
  <main class="match-container" aria-label="Match Details">
    <section class="match-card">
      <div class="teams-row">
        <span>Manchester United</span>
        <span>vs</span>
        <span>Liverpool</span>
      </div>
      <div class="match-meta">Premier League &middot; 20:00 GMT &middot; 12 May 2024</div>
      <!-- Rights Fulfilled State -->
      <a href="#" class="live-stream-link" aria-label="Watch live stream">Watch Live Stream</a>
      <div class="rights-note">Available in your country (UK)</div>
    </section>
    <section class="match-card">
      <div class="teams-row">
        <span>Real Madrid</span>
        <span>vs</span>
        <span>Barcelona</span>
      </div>
      <div class="match-meta">La Liga &middot; 21:00 GMT &middot; 13 May 2024</div>
      <!-- Rights Not Fulfilled State -->
      <div class="no-rights-msg" role="alert">
        Live stream not available in your country.
      </div>
      <div class="rights-note">Broadcast rights not fulfilled for your location (Germany)</div>
    </section>
  </main>
</body>
</html>
</html_file>

<html_file name="settings_notifications_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Settings & Notifications Wireframe - US-007, US-002</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
      --disabled-color: #bfc7d1;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      font-size: 1.3rem;
      font-weight: 600;
      letter-spacing: 1px;
    }
    .settings-container {
      max-width: 500px;
      margin: 32px auto;
      padding: 0 16px;
      display: flex;
      flex-direction: column;
      gap: 32px;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px 20px 20px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .card-title {
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 4px;
    }
    .toggle-row {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .toggle-label {
      font-size: 1rem;
      font-weight: 500;
    }
    .switch {
      position: relative;
      display: inline-block;
      width: 44px;
      height: 24px;
    }
    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }
    .slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: var(--disabled-color);
      border-radius: 24px;
      transition: background 0.2s;
    }
    .switch input:checked + .slider {
      background-color: var(--primary-color);
    }
    .slider:before {
      position: absolute;
      content: "";
      height: 18px;
      width: 18px;
      left: 3px;
      bottom: 3px;
      background-color: #fff;
      border-radius: 50%;
      transition: transform 0.2s;
    }
    .switch input:checked + .slider:before {
      transform: translateX(20px);
    }
    .favorites-list {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 6px;
    }
    .favorite-chip {
      background: #e3eaff;
      color: var(--primary-color);
      border-radius: 16px;
      padding: 4px 12px;
      font-size: 0.97rem;
      cursor: pointer;
      border: none;
      margin-bottom: 4px;
    }
    .favorite-chip.selected {
      background: var(--primary-color);
      color: #fff;
    }
    .favorite-chip:active {
      background: #c6d6f7;
    }
    .note {
      font-size: 0.93rem;
      color: #6b778c;
      margin-top: 4px;
    }
  </style>
</head>
<body>
  <header>Settings</header>
  <main class="settings-container" aria-label="Settings and Notifications">
    <section class="card" aria-label="Notifications">
      <div class="card-title">Push Notifications</div>
      <div class="toggle-row">
        <label class="toggle-label" for="notif-toggle">Enable notifications</label>
        <label class="switch">
          <input type="checkbox" id="notif-toggle" checked>
          <span class="slider"></span>
        </label>
      </div>
      <div class="note">You will receive news and results for your favorite teams.</div>
    </section>
    <section class="card" aria-label="Favorites">
      <div class="card-title">Favorite Teams</div>
      <div class="favorites-list">
        <button class="favorite-chip selected" aria-label="Selected: Manchester United">Manchester United</button>
        <button class="favorite-chip" aria-label="Select Liverpool">Liverpool</button>
        <button class="favorite-chip" aria-label="Select Chelsea">Chelsea</button>
        <button class="favorite-chip" aria-label="Select Real Madrid">Real Madrid</button>
      </div>
      <div class="card-title" style="margin-top:12px;">Favorite Channels</div>
      <div class="favorites-list">
        <button class="favorite-chip selected" aria-label="Selected: Sky Sports">Sky Sports</button>
        <button class="favorite-chip" aria-label="Select BBC Sport">BBC Sport</button>
        <button class="favorite-chip" aria-label="Select ESPN">ESPN</button>
      </div>
      <div class="note">Select your favorites to personalize your news feed.</div>
    </section>
  </main>
</body>
</html>
</html_file>

<html_file name="feedback_testing_mockup.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Feedback & Testing Wireframe - US-011</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-color: #f4f5f7;
      --primary-color: #0052cc;
      --text-color: #172b4d;
      --card-bg: #fff;
      --border-color: #dfe1e6;
      --success-color: #388e3c;
    }
    body {
      background: var(--bg-color);
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text-color);
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      font-size: 1.3rem;
      font-weight: 600;
      letter-spacing: 1px;
    }
    .feedback-container {
      max-width: 500px;
      margin: 32px auto;
      padding: 0 16px;
      display: flex;
      flex-direction: column;
      gap: 32px;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px 20px 20px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .card-title {
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 4px;
    }
    .feedback-form label {
      font-size: 0.98rem;
      margin-bottom: 4px;
    }
    .feedback-form textarea {
      width: 100%;
      min-height: 60px;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      padding: 8px 10px;
      font-size: 1rem;
      background: #f8f9fa;
      color: var(--text-color);
      resize: vertical;
    }
    .submit-btn {
      background: var(--primary-color);
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: 10px 0;
      font-size: 1.05rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 8px;
      transition: background 0.2s;
      width: 100%;
    }
    .submit-btn:active {
      background: #003380;
    }
    .success-msg {
      color: var(--success-color);
      font-size: 0.97rem;
      margin-top: -8px;
      margin-bottom: 4px;
    }
    .feedback-log {
      font-size: 0.97rem;
      color: #6b778c;
      margin-top: 8px;
      border-top: 1px solid var(--border-color);
      padding-top: 8px;
    }
    .checklist {
      margin: 0;
      padding-left: 18px;
      font-size: 0.98rem;
    }
    .checklist li {
      margin-bottom: 4px;
    }
  </style>
</head>
<body>
  <header>Feedback & Testing</header>
  <main class="feedback-container" aria-label="Feedback and Testing">
    <section class="card" aria-label="Feedback Form">
      <div class="card-title">Submit Feedback</div>
      <form class="feedback-form">
        <label for="feedback-text">Your feedback</label>
        <textarea id="feedback-text" name="feedback" required placeholder="Describe your issue or suggestion..."></textarea>
        <button class="submit-btn" type="submit">Send Feedback</button>
        <!-- Success State Example -->
        <div class="success-msg" style="display:block;">Thank you for your feedback!</div>
      </form>
      <div class="feedback-log">
        <strong>Recent Feedback:</strong>
        <ul>
          <li>App loads quickly, but live ticker sometimes lags. (QA, 2h ago)</li>
          <li>Would like more notification options. (User, 1d ago)</li>
        </ul>
      </div>
    </section>
    <section class="card" aria-label="Pre-release Testing Checklist">
      <div class="card-title">Pre-release QA Checklist</div>
      <ul class="checklist">
        <li><input type="checkbox" checked disabled> All critical issues resolved</li>
        <li><input type="checkbox" checked disabled> User feedback reviewed</li>
        <li><input type="checkbox" checked disabled> Performance under load tested</li>
        <li><input type="checkbox" checked disabled> GDPR compliance verified</li>
      </ul>
    </section>
  </main>
</body>
</html>
</html_file>
