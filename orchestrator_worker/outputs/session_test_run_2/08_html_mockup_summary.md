# HTML Mockups

## Interaction Design Overview

### 1. Screen Architecture & Mapping
| Screen / File Name           | Mapped User Story / Requirement | Key Interactions & States Visualized                |
|-----------------------------|---------------------------------|-----------------------------------------------------|
| `startup_splash_mockup.html`| US-001, FR-001                  | Cold/warm startup splash, loading indicator         |
| `auth_mockup.html`          | US-002, FR-008                  | Registration/login toggle, form validation, errors, password toggle |

### 2. UI/UX Design Notes & Trade-offs
- **Startup Splash (US-001):** A minimal, centered splash with logo and animated loader visually communicates fast startup. No extra navigation or content is shown, supporting the 2-second load goal. The loader and note reinforce performance expectations.
- **Registration/Login (US-002):** Unified card with tabbed toggle for Register/Login reduces cognitive load and startup friction. Inline error states are shown for failed registration (invalid email, short password, mismatch). Password visibility toggle improves usability. Only required fields are present, per acceptance criteria. No social login or extra flows are added, as not specified.
- **State Handling:** Error states are visually distinct with red borders/messages. Default and error forms are both present for clarity. All forms use semantic labels and accessible controls.

### 💾 Saved HTML Mockups
- `startup_splash_mockup.html`
- `auth_mockup.html`