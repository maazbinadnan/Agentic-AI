## Business Analysis & Requirements Specification

### 5. Requirements & Story Traceability Matrix

| User Need ID | Derived Requirement IDs | Mapped User Story IDs | Primary Domain Area |
|--------------|-------------------------|-----------------------|---------------------|
| UN-001 | FR-001, FR-002, FR-011 | US-001, US-002, US-011 | User Access & Home Control |
| UN-002 | FR-003, FR-004, FR-011 | US-003, US-004, US-011 | Master User Administration |
| UN-003 | FR-003, FR-004, FR-011 | US-003, US-004, US-011 | Technician Operations |
| UN-004 | NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-006, NFR-007, NFR-011 | None | Prototype Governance |
| UN-005 | FR-001 | US-001 | Web Interaction |
| UN-006 | FR-007, FR-008, NFR-010 | US-007, US-008 | Environmental Control |
| UN-007 | FR-009 | US-009 | Security |
| UN-008 | FR-010 | US-010 | Appliance & Lighting Control |
| UN-009 | FR-005, FR-006, NFR-006, NFR-008, NFR-009 | US-005, US-006 | Infrastructure & Communications |
| UN-010 | FR-003, FR-005 | US-003, US-005 | Data & Accounts |

### 6. Gaps & BA Recommendations

- **Authentication Detail Not Specified:** The source confirms login and logout capability but does not define credential rules, password policy, session timeout, or account recovery. Recommend stakeholder clarification before design and security testing.
- **Alarm Business Rules Incomplete:** The source identifies magnetic contacts and sound/light alarms but does not define arming modes, delay periods, acknowledgement behavior, or notification destinations. Recommend elaboration in a future iteration.
- **Appliance and Lighting Scope Ambiguity:** The source includes power control of small appliances and lighting units but does not specify supported device categories, grouping, scheduling, or maximum number of controllable endpoints.
- **Humidity Control Constraints Missing:** The source states humidity monitoring and set-point control but provides no valid operating range, precision, or tolerance for humidity sensors/controllers.
- **Backup and Recovery Process Undefined:** Backup capability is stated, but backup frequency, storage location, restore process, and failure handling are not defined.
- **Simulated Environment Acceptance Criteria Missing:** The source requires a realistic simulation but does not define measurable realism criteria, simulation scenarios, or pass/fail conditions for prototype evaluation.
- **Project Constraint Granularity:** The source defines team size, Director support, and mandated development process as project constraints, but it does not define compliance measurement criteria or escalation procedures for deviation from those constraints.
- **HTML Mockups Requested but Not in Source Scope:** UI mockups can be provided as illustrative artifacts, but they are not requirements unless validated by stakeholders. Recommend treating mockups as non-binding design aids.

### 7. Summary Statistics

- **Total Discovered User Needs:** 10
- **Total Functional Requirements (FR):** 11
- **Total Non-Functional Requirements (NFR):** 11
- **Total User Stories (US):** 11
- **Priority Breakdown:**
  - Must Have: 11
  - Should Have: 0
  - Could Have: 0
  - Won't Have: 0
- **User Needs Coverage:** 10 / 10

### Additional Design Aids: HTML Mockups

#### Mockup 1: Login Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>DigitalHome Login</title>
  <style>
    body { font-family: Arial, sans-serif; background:#f4f7fb; }
    .card { width:360px; margin:60px auto; background:#fff; padding:24px; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,.1); }
    input, button { width:100%; padding:10px; margin:8px 0; }
    button { background:#2d6cdf; color:#fff; border:none; }
  </style>
</head>
<body>
  <div class="card">
    <h1>DigitalHome</h1>
    <h2>Sign In</h2>
    <label>Username</label>
    <input type="text" placeholder="Enter username" />
    <label>Password</label>
    <input type="password" placeholder="Enter password" />
    <button>Login</button>
  </div>
</body>
</html>
```

#### Mockup 2: Dashboard
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>DigitalHome Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; margin:0; background:#eef2f7; }
    header { background:#1f3c88; color:#fff; padding:16px; }
    .grid { display:grid; grid-template-columns: repeat(2, 1fr); gap:16px; padding:16px; }
    .panel { background:#fff; padding:16px; border-radius:8px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
    button { padding:8px 12px; margin-top:8px; }
  </style>
</head>
<body>
  <header><h1>DigitalHome Dashboard</h1></header>
  <section class="grid">
    <div class="panel"><h2>Temperature</h2><p>Current: 22°C</p><p>Set Point: 24°C</p><button>Adjust</button></div>
    <div class="panel"><h2>Humidity</h2><p>Current: 45%</p><p>Set Point: 50%</p><button>Adjust</button></div>
    <div class="panel"><h2>Security</h2><p>Status: Armed</p><p>Door Sensor: Closed</p><button>View</button></div>
    <div class="panel"><h2>Appliances & Lights</h2><p>Coffee Maker: Off</p><p>Living Room Light: On</p><button>Toggle</button></div>
  </section>
</body>
</html>
```

#### Mockup 3: Admin Configuration
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>DigitalHome Admin</title>
  <style>
    body { font-family: Arial, sans-serif; background:#f8fafc; }
    .wrap { width:900px; margin:30px auto; }
    .panel { background:#fff; padding:20px; border-radius:8px; margin-bottom:16px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
    table { width:100%; border-collapse: collapse; }
    th, td { border:1px solid #ddd; padding:8px; }
    input, select, button { padding:8px; margin:6px 0; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="panel">
      <h1>Administration</h1>
      <h2>User Accounts</h2>
      <table>
        <tr><th>Username</th><th>Role</th><th>Status</th></tr>
        <tr><td>jane</td><td>General User</td><td>Active</td></tr>
        <tr><td>admin1</td><td>Master User</td><td>Active</td></tr>
      </table>
      <h3>Add User</h3>
      <input type="text" placeholder="Username" />
      <select><option>General User</option><option>Master User</option><option>Technician</option></select>
      <button>Create User</button>
    </div>
    <div class="panel">
      <h2>System Controls</h2>
      <button>Start System</button>
      <button>Stop System</button>
    </div>
  </div>
</body>
</html>
```