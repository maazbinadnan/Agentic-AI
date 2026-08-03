# 7. UI Mockups and Interaction Design

## HTML Mockup-to-User Story Mapping Table

| HTML File           | Mapped User Stories         | Visualizations / Core UI Components                       |
|---------------------|----------------------------|----------------------------------------------------------|
| `home.html`         | US-001                     | CAZ info section, benefits, navigation bar                |
| `map.html`          | US-002, US-007             | Interactive map, CAZ selector, legend                     |
| `compliance.html`   | US-003, US-004             | Vehicle compliance form, result display                   |
| `payment.html`      | US-005                     | Payment form, confirmation message                        |
| `exemption.html`    | US-006                     | Exemption check/apply form, confirmation                  |
| `support.html`      | US-008                     | FAQ list, contact info                                    |
| `alternatives.html` | US-009                     | Alternatives list                                         |
| `signposting.html`  | US-010                     | Road sign image, description                              |
| `refund.html`       | US-011                     | Refund form, confirmation                                 |
| `pcn.html`          | US-012                     | PCN form, guidance display                                |

---

## Screen Layout Specifications

- **Navigation:** Persistent top navigation bar on all screens for quick access to all core features.
- **Home:** Introduction to CAZ, benefits, and links to all main features.
- **Map:** Central interactive map area, CAZ selector, activation times, and legend.
- **Compliance:** Simple form for vehicle details, clear result display (compliant/non-compliant).
- **Payment:** Form for reg, CAZ, date, and payment action; confirmation message on success.
- **Exemption:** Form for reg and exemption type, with eligibility check and application submission.
- **Support:** FAQ section and contact details for technical help.
- **Alternatives:** List of alternative options to paying a CAZ charge.
- **Signposting:** Visuals of road signs and boundaries, with explanations.
- **Refund:** Form for payment reference and reason, confirmation on submission.
- **PCN:** Form for PCN reference, guidance display after submission.

---

## UI/UX Trade-offs and Rationale

- **Simplicity vs. Feature Depth:** Prioritized clear, simple forms and navigation to minimize user admin time and cognitive load, in line with user needs for quick, easy interactions.
- **Accessibility:** High-contrast colors, large clickable areas, and mobile responsiveness are used throughout. Further accessibility (e.g., ARIA labels) should be added in implementation.
- **Consistency:** All screens use a unified navigation bar and consistent layout for familiarity and ease of use.
- **Feedback:** Confirmation and result messages are provided for all user actions (e.g., payment, exemption, refund, PCN guidance).
- **Scalability:** The design supports adding more CAZs, exemption types, and alternative options without major UI changes.
- **Edge Cases:** Forms prevent unnecessary actions (e.g., payment for exempt vehicles) and provide clear error/confirmation states.

---

## Recommendations for Further UI/UX Refinement

- Add ARIA roles and keyboard navigation for full accessibility compliance.
- Consider user onboarding or guided tours for first-time users.
- Implement real-time validation and error handling for all forms.
- Add multi-language support if required by stakeholders.
- Integrate notifications (email/SMS) for payments, exemptions, and PCNs if needed.
