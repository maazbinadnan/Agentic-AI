## Assumption-Based HTML Mockup Concepts

> Note: These are low-fidelity, assumption-based mockup concepts created because the request asked for HTML mockups. They are not validated requirements and should not be treated as approved scope until confirmed by stakeholders.

### Mockup 1: Home / Personalized News
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Home</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; background: #f5f5f5; }
    header { background: #0b5; color: white; padding: 16px; }
    nav { display: flex; justify-content: space-around; background: #fff; padding: 12px; border-bottom: 1px solid #ddd; }
    .container { padding: 16px; }
    .card { background: #fff; padding: 12px; margin-bottom: 12px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .tag { display: inline-block; background: #e8f7f0; color: #0b5; padding: 4px 8px; border-radius: 12px; font-size: 12px; }
  </style>
</head>
<body>
  <header>
    <h1>LiveFootball</h1>
    <p>Your personalized football hub</p>
  </header>
  <nav>
    <span>Home</span>
    <span>Live</span>
    <span>Teams</span>
    <span>Profile</span>
  </nav>
  <div class="container">
    <div class="card">
      <span class="tag">Favorite Team</span>
      <h3>Liverpool latest update</h3>
      <p>Current football news filtered by your saved preferences.</p>
    </div>
    <div class="card">
      <span class="tag">Channel: Sky Sport</span>
      <h3>Matchday preview</h3>
      <p>News selected from preferred sports channels.</p>
    </div>
  </div>
</body>
</html>
```

### Mockup 2: Live Ticker
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Live Ticker</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; background: #111; color: #fff; }
    header { background: #1c1c1c; padding: 16px; }
    .container { padding: 16px; }
    .score { font-size: 32px; font-weight: bold; }
    .event { background: #1f1f1f; padding: 10px; margin-bottom: 8px; border-radius: 6px; }
  </style>
</head>
<body>
  <header>
    <h1>Live Ticker</h1>
    <p>Real-time match updates</p>
  </header>
  <div class="container">
    <div class="score">Arsenal 2 - 1 Chelsea</div>
    <div class="event">78' Goal - Arsenal scores from open play.</div>
    <div class="event">81' Yellow Card - Chelsea midfielder booked.</div>
    <div class="event">85' Substitution - Arsenal makes a defensive change.</div>
  </div>
</body>
</html>
```

### Mockup 3: Login / Registration
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LiveFootball - Sign In</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f6f8; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .panel { background: #fff; padding: 24px; border-radius: 8px; width: 320px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    input, button { width: 100%; padding: 10px; margin-top: 10px; }
    button { background: #0b5; color: white; border: none; }
  </style>
</head>
<body>
  <div class="panel">
    <h2>Welcome to LiveFootball</h2>
    <input type="email" placeholder="Email" />
    <input type="password" placeholder="Password" />
    <button>Login</button>
    <button>Create Account</button>
  </div>
</body>
</html>
```

### BA Recommendation
- Validate screen list, navigation model, branding, and interaction priorities before converting these low-fidelity examples into approved UI requirements or production-ready front-end assets.