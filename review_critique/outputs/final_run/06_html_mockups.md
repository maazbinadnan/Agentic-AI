## HTML Mockups for LiveFootball App

The following lightweight HTML mockups are illustrative wireframes grounded in the supplied requirements. They are non-functional prototypes intended to support design discussions.

### Mockup 1: Startup / Login Screen

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Welcome</title>
  <style>
    body { font-family: Arial, sans-serif; background:#111827; color:#fff; margin:0; }
    .container { padding:24px; max-width:420px; margin:0 auto; }
    .card { background:#1f2937; border-radius:16px; padding:20px; margin-top:40px; }
    input, button { width:100%; padding:12px; margin-top:12px; border-radius:10px; border:none; }
    button { background:#22c55e; color:#08120b; font-weight:bold; }
    .secondary { background:#374151; color:#fff; }
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <h1>LiveFootball</h1>
      <p>Fast football updates, live ticker, news, and streams.</p>
      <input type="email" placeholder="Email address" />
      <input type="password" placeholder="Password" />
      <button>Log In</button>
      <button class="secondary">Register</button>
    </div>
  </div>
</body>
</html>
```

### Mockup 2: Home Dashboard

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Home</title>
  <style>
    body { font-family: Arial, sans-serif; margin:0; background:#f3f4f6; }
    header { background:#0f172a; color:#fff; padding:16px; }
    .section { padding:16px; }
    .card { background:#fff; border-radius:12px; padding:16px; margin-bottom:12px; box-shadow:0 2px 8px rgba(0,0,0,0.08); }
    .tag { display:inline-block; background:#dcfce7; color:#166534; padding:4px 8px; border-radius:999px; font-size:12px; }
    nav { position:fixed; bottom:0; left:0; right:0; background:#fff; display:flex; justify-content:space-around; padding:12px; border-top:1px solid #ddd; }
  </style>
</head>
<body>
  <header>
    <h1>LiveFootball</h1>
    <p>Your personalized football hub</p>
  </header>
  <div class="section">
    <div class="card">
      <span class="tag">Favorites</span>
      <h3>Manchester City</h3>
      <p>Latest news and match alerts enabled.</p>
    </div>
    <div class="card">
      <span class="tag">News</span>
      <h3>Team update headline</h3>
      <p>Current football news from selected channels.</p>
    </div>
    <div class="card">
      <span class="tag">Live</span>
      <h3>Arsenal vs Liverpool</h3>
      <p>Live ticker: 67' - Goal scored.</p>
    </div>
  </div>
  <nav>
    <span>Home</span>
    <span>News</span>
    <span>Live</span>
    <span>Profile</span>
  </nav>
</body>
</html>
```

### Mockup 3: Live Ticker Screen

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Live Ticker</title>
  <style>
    body { font-family: Arial, sans-serif; background:#0b1020; color:#fff; margin:0; }
    .wrap { padding:20px; }
    .score { font-size:32px; font-weight:bold; margin:12px 0; }
    .event { background:#172036; padding:12px; margin:10px 0; border-radius:10px; }
    .live { color:#22c55e; font-weight:bold; }
  </style>
</head>
<body>
  <div class="wrap">
    <p class="live">LIVE</p>
    <h1>Barcelona vs Real Madrid</h1>
    <div class="score">2 - 1</div>
    <div class="event">12' Goal - Barcelona</div>
    <div class="event">48' Equalizer - Real Madrid</div>
    <div class="event">67' Goal - Barcelona</div>
  </div>
</body>
</html>
```

### Mockup 4: Preferences and Notifications

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Preferences</title>
  <style>
    body { font-family: Arial, sans-serif; background:#f9fafb; margin:0; }
    .container { max-width:480px; margin:0 auto; padding:20px; }
    .panel { background:#fff; border-radius:12px; padding:16px; margin-bottom:16px; }
    label { display:block; margin:10px 0; }
    button { background:#16a34a; color:#fff; border:none; padding:12px 16px; border-radius:10px; width:100%; }
  </style>
</head>
<body>
  <div class="container">
    <div class="panel">
      <h2>Favorite Teams</h2>
      <label><input type="checkbox" checked /> Bayern Munich</label>
      <label><input type="checkbox" /> PSG</label>
      <label><input type="checkbox" checked /> Chelsea</label>
    </div>
    <div class="panel">
      <h2>Preferred Channels</h2>
      <label><input type="checkbox" checked /> Sky Sport</label>
      <label><input type="checkbox" /> DAZN</label>
    </div>
    <div class="panel">
      <h2>Notifications</h2>
      <label><input type="checkbox" checked /> Match results</label>
      <label><input type="checkbox" checked /> Team news</label>
    </div>
    <button>Save Preferences</button>
  </div>
</body>
</html>
```

### Mockup Notes

- These mockups align with startup/login, personalized dashboard, live ticker, and personalization/notification requirements.
- Stream rights logic, offline behavior, and real-time API updates are not represented functionally in static HTML.
- If needed, these can be expanded into clickable prototypes or split into separate `.html` files in a later iteration.
