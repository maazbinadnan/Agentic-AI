# 07_ui_mockups.md

## 1. Interaction Design Overview & Screen Architecture

The DigitalHome prototype uses a role-aware web interface optimized for desktop and tablet widths while remaining responsive down to mobile-sized mockup frames. The UI architecture is organized around the main tasks surfaced in the user stories:

- **Authentication entry** for sign-in, access denial, and re-entry after logout.
- **Operational dashboard** for real-time monitoring of environment, security, power, gateway, and connectivity state.
- **Climate control views** for thermostat and humidistat readings, set points, and degraded-control feedback.
- **Security and power management views** for contact sensors, alarms, and programmable switch control.
- **Planning and reporting views** for monthly plans, daily presets, scheduled execution, historical reporting, and storage/backup context.
- **Administrative console** for role-restricted user account management, default parameter configuration, system start/stop, and backup initiation.

### Screen Architecture

1. **Login (`login.html`)**
   - Entry point for all protected functions.
   - Shows primary, empty, and failed authentication states.
   - Supports secure session initiation and post-logout re-authentication.

2. **Dashboard / Monitoring (`dashboard_monitoring.html`)**
   - Primary landing page after successful login.
   - Consolidates current temperature, humidity, security, alarm, and power states.
   - Includes role-restricted navigation cues and broadband/gateway status.

3. **Climate Controls (`climate_controls.html`)**
   - Dedicated control surface for thermostat and humidistat interaction.
   - Exposes current readings, set-point forms, and error handling for invalid/out-of-range data.

4. **Security & Power (`security_power.html`)**
   - Displays door/window state, alarm activation, and appliance/lighting switching.
   - Covers normal, inactive sensor, breach, and unreachable command cases.

5. **Plans, Presets & Reports (`plans_reports.html`)**
   - Supports monthly plans, daily presets, scheduled execution states, and historical analytics.
   - Communicates when no plan/report data exists and when scheduled actions fail due to unavailable devices.

6. **Administration Console (`admin_console.html`)**
   - Reserved for Master User and DH Technician flows.
   - Supports account management, parameter updates, system operation changes, and backup operations.
   - Includes a restricted state for General Users.

---

## 2. HTML Mockups to User Stories Mapping Table

| HTML File | Mapped User Stories | Visualizations / Core UI Components |
|---|---|---|
| `login.html` | US-001, US-003 | Login form, username/password fields, remember-device checkbox, sign-in CTA, invalid-credentials error banner |
| `dashboard_monitoring.html` | US-002, US-004, US-005, US-006, US-020, US-021 | Role-aware navigation, logout button, gateway/broadband status banners, current status cards, unavailable-data indicators, restricted admin access panel |
| `climate_controls.html` | US-007, US-008 | Thermostat card, humidistat card, target set-point inputs, regulation status badges, out-of-range warning, unavailable output message |
| `security_power.html` | US-009, US-010, US-011 | Contact sensor list, normal/breach badges, sound/light alarm indicators, power toggle controls, unreachable-device failure messaging |
| `plans_reports.html` | US-012, US-013, US-014, US-015, US-019 | Monthly plan table, daily preset table, scheduled execution status, historical KPI report cards, empty report state, backup context panel |
| `admin_console.html` | US-016, US-017, US-018, US-019 | User account table, add-user action, default parameter form, start/stop controls, backup action, role-based access denied state |

---

## 3. Detailed UI Screen Specifications & Component Breakdowns

### A. Authentication
**Primary goal:** let users sign in securely and block protected functions when authentication fails.

**Key components:**
- Branded header with DigitalHome identity.
- Username and password inputs.
- Remember-device checkbox.
- Primary sign-in CTA.
- Error banner for invalid credentials.
- Guidance text for role-based permissions after login.

**Interaction notes:**
- Successful authentication routes the user to the dashboard appropriate to their role.
- Failed authentication preserves the current page and highlights the error without exposing protected content.
- Logout from authenticated views returns the user to the login page and requires fresh authentication.

### B. Monitoring Dashboard
**Primary goal:** provide a single overview of current home conditions.

**Key components:**
- Side navigation with active module highlighting.
- Status summary cards for temperature, humidity, security, and active power devices.
- Device-level list items for contacts and switches.
- Broadband/gateway health banners.
- Restricted-admin feedback for General Users.

**Interaction notes:**
- Monitoring data cards prioritize the most important home conditions at the top.
- Partial data states preserve available device information while explicitly labeling unavailable values.
- Offline remote states inform users that communication is degraded rather than silently failing.

### C. Climate Controls
**Primary goal:** support direct climate monitoring and set-point submission.

**Key components:**
- Separate thermostat and humidistat cards.
- Current reading visualization with supported range reminder.
- Set-point entry fields and save actions.
- Regulation status pills indicating heating/cooling/regulating conditions.
- Error and degraded-control banners.

**Interaction notes:**
- Thermostat values outside 14°F–104°F are visually rejected and excluded from normal control logic.
- Humidity set points can be stored even when humidifier/dehumidifier outputs are temporarily unavailable.
- Feedback differentiates between “request saved” and “regulation successfully active.”

### D. Security & Power
**Primary goal:** allow users to understand entry security and manage power switches.

**Key components:**
- Contact sensor list with closed, breach, and inactive states.
- Alarm state section with sound and light signals.
- Power-switch command buttons for appliances and lighting.
- Failure message when a switch is unreachable.

**Interaction notes:**
- Inactive sensors are shown neutrally and are not presented as security incidents.
- Breach events elevate red visual priority and display both source and alarm outcomes.
- Power state changes are only shown as successful when confirmed by device state.

### E. Plans, Presets & Reports
**Primary goal:** support scheduled automation and retrospective analysis.

**Key components:**
- Monthly plan table for date-based automation.
- Daily preset table for recurring schedules.
- Historical report KPI cards for average, min/max, and downtime style metrics.
- Empty-state messaging for absent plans or reports.
- Scheduled execution failure panel.

**Interaction notes:**
- Users can distinguish between authored schedules and runtime execution outcomes.
- Historical reporting emphasizes scannable summary metrics before deeper detail.
- Backup context is surfaced near plan/report data to reinforce that stored information is preserved on the home server.

### F. Administration Console
**Primary goal:** give Master Users and Technicians controlled access to system maintenance capabilities.

**Key components:**
- User account table with role labels.
- Add/create account CTA.
- Default parameter form controls.
- Start/stop operation actions.
- Backup initiation action.
- Explicit access-denied state for unauthorized users.

**Interaction notes:**
- Privileged actions are grouped into account management, configuration, operations, and backup sections.
- Restricted users see disabled or blocked controls with explanatory messaging instead of hidden navigation only.
- Backup behavior messaging reflects the requirement to preserve available data without inventing missing data categories.

---

## 4. Visual Hierarchy, Accessibility (WCAG 2.1), & UX Trade-offs

### Visual Hierarchy
- Critical operational conditions use banner-based feedback at the top of screens.
- Summary values use large typography for rapid scanning.
- Device details and forms are grouped in card containers for modular comprehension.
- Restricted or error states use strong contrast and concise language to reduce ambiguity.

### Accessibility Considerations
- Color is paired with text labels such as **Normal**, **Breach**, **Denied**, and **No data** so status is not conveyed by color alone.
- Inputs, buttons, and tables are sized for clear pointer and keyboard interaction.
- Layouts use responsive stacking to maintain readability on narrow viewports.
- Semantic patterns are mirrored in the HTML structure: headings, labels, buttons, and tabular information are presented in screen-reader-friendly ways.
- Contrast choices are designed to align with WCAG 2.1 AA intent, especially for banners, text, and button labels.

### UX Trade-offs
- The dashboard intentionally aggregates several device categories to reduce navigation depth, even though this creates a denser first screen.
- Separate climate and security/power views improve task focus for direct control actions.
- Restricted actions are visibly present but blocked for General Users to improve discoverability of role capabilities and reduce confusion about missing features.
- Multi-state mockups are shown side-by-side in each HTML file to accelerate stakeholder review of normal, empty, and degraded flows in the prototype phase.

### Responsive Strategy
- Every mockup uses a shared responsive grid pattern with `wrap`, `grid`, `phone`, and `screen` containers.
- Auto-fit columns allow multiple states to be reviewed side-by-side on wide screens and stacked on narrow screens.
- Cards and tables are chunked into modular blocks to remain legible during responsive collapse.

---

## Deliverables Generated
- `html/login.html`
- `html/dashboard_monitoring.html`
- `html/climate_controls.html`
- `html/security_power.html`
- `html/plans_reports.html`
- `html/admin_console.html`
- `07_ui_mockups.md`
