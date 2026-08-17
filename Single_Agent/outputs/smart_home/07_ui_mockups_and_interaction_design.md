# 7. UI Mockups and Interaction Design Report

## HTML Mockup-to-User Story Mapping Table

| HTML File              | Mapped User Stories      | Visualizations / Core UI Components                       |
|-----------------------|-------------------------|----------------------------------------------------------|
| `login.html`          | US-002                  | Login form, error feedback, responsive layout             |
| `dashboard.html`      | US-001, US-003          | Device list, controls (sliders, switches), error/offline |
| `user_management.html`| US-004                  | User table, add/edit/remove actions, error/empty states   |
| `system_config.html`  | US-005                  | System parameter forms, save, error/empty states          |
| `backup_restore.html` | US-006                  | Backup/restore buttons, status messages, error/empty      |

## Screen Layout Specifications

- **Login Screen:** Centered login form with username/password fields, error feedback, and responsive design for mobile/desktop.
- **Dashboard:** Grid of device cards (thermostat, humidistat, appliances, security alarm) with real-time values, sliders, switches, and error/offline states.
- **User Management:** Table of users with roles and actions (edit/remove), add user button, error and empty states.
- **System Configuration:** Form fields for device simulation parameters (temperature, humidity, gateway range), save button, error/empty states.
- **Backup & Restore:** Simple interface with backup/restore buttons, status messages for success, error, and empty states.

## UI/UX Trade-offs

- **Responsiveness:** All screens use grid layouts and scalable controls for usability on both desktop and mobile devices.
- **Error Handling:** Each screen includes explicit error and empty states to ensure users are informed of system status and failures.
- **Simplicity:** The prototype UI avoids unnecessary complexity, focusing on core flows for the prototype scope.
- **Role-based Access:** Management/configuration screens are designed for Master Users/Technicians, but not shown to General Users.
- **Consistency:** Common visual language (colors, spacing, button styles) across all screens for a cohesive experience.

## Interaction Design Notes

- Device controls (sliders, switches) provide immediate feedback and update values in real time.
- Error and offline states are visually distinct to reduce confusion.
- All forms validate input and provide clear error messages.
- Navigation between screens is assumed via a main menu or sidebar (not shown in mockups for prototype simplicity).
